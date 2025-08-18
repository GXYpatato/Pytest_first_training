from pytest_training.utils.read_data import base_data
from pytest_training.testcase.meike_testcase.conftest import get_user_id, get_shop_cart

def test_login_fixture(login_fixture):
    session=login_fixture
    assert 'Authorization' in session.headers
    assert session.headers['Authorization'].startswith('JWT')
    assert len(session.headers['Authorization']) > 10  # token应该有内容

    print(f"✅ Session认证头: {session.headers['Authorization']}")
    print("✅ 夹具工作正常")