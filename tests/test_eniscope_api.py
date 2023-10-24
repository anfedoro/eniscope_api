from unittest.mock import patch
import pytest,requests
import eniscope.eniscopeapi as es

# empty test function
def test_empty():
    client = es.EniscopeAPIClient()
    assert isinstance(client, es.EniscopeAPIClient)

#test fucntion for user autherntication
def test_user_auth():
    client = es.EniscopeAPIClient()
    authenticated  = client.authenticate_user()
   
    assert authenticated == True
    assert client.auth_data is not None
    assert client.headers is not None

