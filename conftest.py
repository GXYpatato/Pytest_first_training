import requests
import pytest
from pytest_training.utils.read_data import base_data




@pytest.fixture(scope='function')
def login_fixture()-> requests.Session:
    data = base_data.read_data()
    session = requests.Session()
    headers = {'Content-Type': 'application/json'}
    try:
        response = session.post(
            url='http://admin.5istudy.online/login/',
            json=data['test_login'],
            headers=headers
        )
        token = response.json().get('token')

        if not token:
            raise ValueError(f"未找到token字段，响应: {response_data}")

        # 添加认证头
        session.headers.update({'Authorization': f'JWT {token}'})

        print(f"✅ 登录成功，用户: {data['test_login']['username']}")
        from pytest_training.core.api_util import api_util
        api_util.session = session  # 直接替换会话对象

        return session

    except requests.exceptions.RequestException as e:
        session.close()
        pytest.fail(f"登录请求失败: {str(e)}")
    except ValueError as e:
        session.close()
        pytest.fail(f"Token提取失败: {str(e)}")
