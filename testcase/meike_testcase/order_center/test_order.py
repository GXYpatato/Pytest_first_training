import pytest

from pytest_training.core.Api_Service import ApiService
from pytest_training.utils.YamlUtil import YamlUtil


class TestOrder:
    @pytest.mark.parametrize("data", YamlUtil().extract_case("order_center.yaml", 'order_list'))
    def test_order_list(self, data,login_token):
        response = ApiService().handle_case(data,login_token)
        print(response)

    @pytest.mark.parametrize("data", YamlUtil().extract_case("order_center.yaml", 'order_detail'))
    def test_order_detail(self, data, login_token):
        ApiService().handle_case(data, login_token)



