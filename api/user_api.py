from pytest_training.core.api_util import api_util
from pytest_training.utils.process_utils import process_response
from pytest_training.utils.read_data import base_data


def send_code(json_data):
    response = api_util.get_code(json=json_data)
    return process_response(response)


def register(mobile, code):
    json_data = {
        "code": str(code),
        "password": "123456",
        "username": str(mobile)
    }
    response = api_util.register_mobile(json=json_data)
    return process_response(response)


def login():
    data=base_data.read_data()['test_login']
    json_data = {
        "username": str(data['username']),
        "password": str(data['password'])
    }
    response = api_util.login(json=json_data)
    return process_response(response)
