from pytest_excise.utils.read_data import base_data
import requests
import allure
from pytest_excise.utils.log_util import logger

# #paramsetrize+yaml多参数
# @pytest.mark.parametrize("username,pwd", data['userinfo'])
# def test_user(username,pwd):
#     print(f'{username}的密码是{pwd}')
#
# #paramsetrize+yaml单参数
# @pytest.mark.parametrize("drink", data['drink'])
# def test_drink(drink):
#     print(f'{drink}')


# parametrize+yaml+requests

# @pytest.mark.parametrize("username,pwd",data['userinfo'])
# def test_login(username,pwd):
#     headers = {'Content-Type': 'application/json'}
#     r =requests.post(
#         url='http://127.0.0.1:8080/account/login',
#         json={'username': username, 'password': pwd},
#         headers=headers)
#     print(f"Response Body: {r.text}")
#     assert r.status_code == 200

# logger.info("测试开始")
# # @allure.epic("Fastapi_reviewer接口测试")
# # @allure.feature("登录登出以及首页测试")
# class TestLogin:
#     # @allure.story("测试登录，username是gxy,密码保密，且gxy是已注册用户，登录信息是正确的，为正向测试")
#     # @allure.title("登陆测试")
#     def test_login(self, login):
#         self.r = login.get(url='http://127.0.0.1:8080/index')
#         print(self.r.text)
#         assert self.r.status_code == 200
#
#     # @allure.story("测试登出，已经登录，为正向测试")
#     # @allure.title("登出测试")
#     def test_logout(self, login):
#         self.r = login.get(url='http://127.0.0.1:8080/account/logout')
#         print(self.r.text)
#         assert self.r.status_code == 200
#
#
#     # @allure.title("登陆后的访问首页测试")
#     def test_index(self,login):
#         self.r = login.get(url='http://127.0.0.1:8080/index')
#         print(self.r.text)
#         assert self.r.status_code == 200
# #json.dump()数据转储为json格式
#
# logger.info("测试结束")

def test_01():
    assert 1==1