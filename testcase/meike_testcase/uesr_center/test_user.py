import allure
from pytest_training.api.user_api import send_code, register, login
from pytest_training.testcase.meike_testcase.conftest import get_code, delete_user, delete_code
from pytest_training.utils.read_data import base_data


class TestUser:
    def test_register(self):
        # 发送验证码
        json_data = base_data.read_data()['test_register']

        # 删除验证码，规避提示：距离上次发送还没超过1分钟
        delete_code(json_data['mobile'])
        result = send_code(json_data)
        assert result.success is True

        # 获取验证码
        mobile = result.body['mobile']
        code = get_code(mobile)
        print(code)

        register_result = register(mobile, code)
        assert register_result.success is True

        # 删除用户
        # delete_user(mobile)
        delete_user('15959996163')

    def test_login(self):
        login_result = login()
        assert login_result.success is True

