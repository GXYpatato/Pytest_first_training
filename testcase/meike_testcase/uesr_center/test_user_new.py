import pytest

from pytest_training.core.Api_Service import ApiService
from pytest_training.utils.YamlUtil import YamlUtil


class TestUser:
    @pytest.mark.parametrize("data", YamlUtil().extract_case("user_center.yaml", 'user_login_new'))
    def test_user_new(self, data):

        response = ApiService().handle_case(data)

        print(response)


