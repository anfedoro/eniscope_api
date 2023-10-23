import base64
import hashlib
import keyring
from cryptography.fernet import Fernet
import getpass, sys, os

SERVICE_NAME = "eniscope"


def generate_key():
    """
    Generates a key and saves it using keyring.
    """
    key = Fernet.generate_key()
    keyring.set_password(
        SERVICE_NAME, "encryption_key", key.decode()
    )  # save encryption key in keyring
    return key


def get_key():
    """
    Retrieves the key from keyring.
    """
    key = keyring.get_password(SERVICE_NAME, "encryption_key")
    if key is None:
        return generate_key()
    return key.encode()


def encrypt_data(data):
    """
    Encrypts the data.
    """
    key = get_key()
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data


def decrypt_data(encrypted_data):
    """
    Decrypts the data.
    """
    key = get_key()
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data.encode())
    return decrypted_data


def store_user_credentials(user_email, user_password):
    """
    Encrypts and stores the user credentials in keyring.
    Parameters:
        user_email (str): The user email.
        user_password (str): The user password.
    Returns:
        None
    """
    # MD5 hash the password
    md5_password = hashlib.md5(user_password.encode()).hexdigest()

    # Encode the credentials as base64 for further use in the API Authorization header
    encoded_credentials = base64.b64encode(
        f"{user_email}:{md5_password}".encode()
    ).decode()

    # Encrypt the credentials
    encrypted_credentials = encrypt_data(encoded_credentials).decode()

    # Store the encrypted credentials in keyring
    keyring.set_password(SERVICE_NAME, "user_credentials", encrypted_credentials)


def store_api_key(service_name, api_key):
    """
    Stores the API key in keyring.
    Parameters:
        service_name (str): The service name.
        api_key (str): The API key.
    Returns:
        None
    """
    keyring.set_password(service_name, "api_key", api_key)


def retrieve_api_key(service_name):
    """
    Retrieves the API key from keyring.
    Parameters:
        service_name (str): The service name.
    Returns:
        api_key (str): The API key.
    """
    api_key = keyring.get_password(service_name, "api_key")
    if api_key is None:
        print("No API key found for", service_name)
        print
    return api_key


def retrieve_user_credentials(service_name):
    """
    Retrieves the user credentials from keyring.
    Parameters:
        None
        Returns:
    """
    encrypted_credentials = keyring.get_password(service_name, "user_credentials")
    if encrypted_credentials is None:
        print("No user credentials found")
        return None
    decrypted_credentials = decrypt_data(encrypted_credentials)
    return decrypted_credentials.decode()


def main():
    is_stored = False

    if sys.platform == "linux":
        from keyrings.cryptfile.cryptfile import CryptFileKeyring
        kr = CryptFileKeyring()
        kr.keyring_key = os.environ.get('KEYRING_CRYPTFILE_PASSWORD') or getpass.getpass("Enter keyring password: ")
        keyring.set_keyring(kr)

    user_email = input("Enter user email: ")
    user_password = getpass.getpass("Enter user password: ")
    if user_password == "" and user_email != "":
        print("No user password entered, please ensure you don't use empty password")

    elif user_email != "" and user_password != "":
        store_user_credentials(user_email, user_password)
        is_stored = True

    api_key = input("Enter API key: ")
    if api_key != "":
        store_api_key(SERVICE_NAME, api_key)
        is_stored = True

    if is_stored:
        print("Credentials encrypted and stored safely.")
    else:
        print("Exit.")


if __name__ == "__main__":
    main()
