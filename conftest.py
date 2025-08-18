import requests
import pytest


@pytest.fixture(scope='function')
def login():
    res = requests.Session()
    headers = {'Content-Type': 'application/json'}
    r=res.post(
        url='http://127.0.0.1:8080/account/login',
        json={'username': 'gxy', 'password': 'gxy040720'},
        headers=headers
    )
    print(f"Response Body: {r.text}")
    return res
