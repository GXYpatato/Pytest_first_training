from pytest_training.core.api_util import api_util
from pytest_training.utils.process_utils import process_response
from pytest_training.utils.read_data import base_data
import pytest

data = base_data.read_data()


def shop_carts():
    json = {
        "goods": data['shop_carts']['goods'],
        "nums": data['shop_carts']['nums']
    }
    response = api_util.shopping_cart(json=json)
    return process_response(response)