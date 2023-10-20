from unittest.mock import patch
import pytest
import eniscope.eniscope_creds as esc

# pach decoration is used for mocking the keyring.set_password function
@patch("eniscope.eniscope_creds.keyring.set_password")
def test_generate_key(mock_set_password):
    """
    Test that the key is generated and saved in keyring.
    """

    # Call the function under test
    key = esc.generate_key()

    # Assert that keyring.set_password was called with the expected arguments
    mock_set_password.assert_called_once_with("eniscope", "encryption_key", key.decode())
    

    # Assert the returned key is a bytes and of correct length
    assert isinstance(key, bytes)
    assert len(key) == 44  # Fernet keys are base64-encoded, which takes up 44 bytes

# test function for eniscope/eniscope_creds.get_key(). Mocking the keyring.get_password function
@patch("eniscope.eniscope_creds.keyring.get_password")
@patch("eniscope.eniscope_creds.keyring.set_password")
def test_get_key(mock_set_password, mock_get_password):
    """
    Test that the key is retrieved from keyring.
    """

    # Configure the mock to return the mock_key
    mock_get_password.return_value = None

    # Call the function under test
    key = esc.get_key()

    # Assert that keyring.get_password was called with the expected arguments
    mock_get_password.assert_called_once_with("eniscope", "encryption_key")
    mock_set_password.assert_called_once()

    # Assert the returned key is a bytes and of correct length
    assert isinstance(key, bytes)
    assert len(key) == 44

@patch("eniscope.eniscope_creds.get_key")
def test_encrypt_decrypt_data(mock_get_key):
    """
    Test that the data is encrypted.
    """

    # Configure the mock to return the mock_key
    mock_get_key.return_value = b"1234567890123456789012345678901234567890123="

    # Call the function under test
    test_data = "test data"
    encrypted_data = esc.encrypt_data(test_data)
    decrypted_data = esc.decrypt_data(encrypted_data.decode()).decode()
    mock_get_key.call_count == 2

    # Assert the returned encrypted_data is a bytes and of correct length
    assert isinstance(encrypted_data, bytes)
    assert isinstance(decrypted_data, str)
    assert decrypted_data == test_data