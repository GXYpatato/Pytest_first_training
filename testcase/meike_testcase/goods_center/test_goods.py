import allure
from pytest_training.api.goods_api import *
from pytest_training.testcase.meike_testcase.conftest import get_user_id, get_shop_cart, delete_shop_cart
from pytest_training.utils.read_data import base_data
from pytest_training.core.Api_Service import ApiService
from pytest_training.utils.YamlUtil import YamlUtil


class TestGoods:
    def test_shopping_cart(self,login_fixture):
        data = base_data.read_data()
        user_id = get_user_id(data['test_login']['username'])
        goods_id = data['shop_carts']['goods']
        delete_shop_cart(user_id,goods_id)
        result = shop_carts()
        nums=get_shop_cart(user_id,data['shop_carts']['goods'])
        print(result.body['nums'])
        assert result.body['nums'] == nums

    @pytest.mark.parametrize("data2", YamlUtil().extract_case("goods_center.yaml", 'get_banner'))
    def test_banner_new(self,data2):
        ApiService().handle_case(data2)
        


