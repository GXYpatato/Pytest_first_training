from pytest_training.utils.log_util import logger
from pytest_training.utils.mysql_util import db
import os
import pytest
from pytest_training.api.user_api import login
from pytest_training.utils.read_data import base_data


def get_data():
    return base_data.read_data()

#获取验证码
def get_code(mobile):
    sql = "select code from users_verifycode where mobile = '%s' order by id desc limit 1;" % mobile
    result = db.select_db_one(sql)
    logger.info(f'sql执行结果：{result}')
    return result['code']

#删除用户
def delete_user(mobile):
    sql = "delete from users_userprofile where mobile='%s' ;"% mobile
    result = db.execute_db(sql)
    logger.info(f'sql执行结果：{result}')

#删除用户手机号
def delete_code(mobile):
    sql = "delete from users_verifycode where mobile = '%s' ;" % mobile
    result = db.execute_db(sql)
    logger.info(f'sql执行结果：{result}')

def get_user_id(mobile):
    sql = "select id from users_userprofile where mobile='%s';"%mobile
    result = db.select_db_one(sql)
    logger.info(f'sql执行结果：{result}')
    return result['id']

def get_shop_cart(userid,goods_id):
    sql ="select nums from trade_shoppingcart where user_id= '%s' and goods_id= '%s'" %(userid,goods_id)
    result = db.select_db_one(sql)
    logger.info(result)
    return result['nums']

def delete_shop_cart(userid,goods_id):
    sql = "update trade_shoppingcart set nums=0 where user_id= '%s' and goods_id= '%s' "%(userid,goods_id)
    result =db.execute_db(sql)
    logger.info(result)
    logger.info(f'sql执行结果：{result}')

@pytest.fixture(scope='function')
def login_token():
    result=login()
    headers={
        "Authorization": "JWT " + result.body['token']
    }

    return headers