from pytest_excise.core.api_util import api_util
from pytest_excise.utils.process_utils import process_response


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
