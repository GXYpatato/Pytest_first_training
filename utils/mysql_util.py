import pymysql

from pytest_training.utils.log_util import logger
from pytest_training.utils.read_data import base_data

data = base_data.read_ini()['mysql']

DB_CONF = {
    'host': data['MYSQL_HOST'],
    'port': int(data['MYSQL_PORT']),
    'user': data['MYSQL_USER'],
    'password': data['MYSQL_PASSWD'],
    'database': data['MYSQL_DB'],

}


class MysqlDb:
    def __init__(self):
        # mysql连接
        self.conn = pymysql.connect(**DB_CONF, autocommit=True)
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 释放资源
    def __del__(self):
        self.conn.close()
        self.cur.close()

    def select_db_one(self, sql):
        logger.info(f"执行sql:{sql}")
        self.cur.execute(sql)
        result = self.cur.fetchone()
        # 获取数据
        logger.info(f"执行结果:{sql}")
        return result  # fetch获取数据,fetchone,获取一条

    def select_db_all(self, sql):
        logger.info(f"执行sql:{sql}")
        self.cur.execute(sql)
        # 获取数据
        result = self.cur.fetchall()
        logger.info(f"sql执行结果:{sql}")
        return result  # fetchall获取所有数据

    def execute_db(self, sql):
        try:
            logger.info(f"执行sql:{sql}")
            self.cur.execute(sql)  # excute执行sql语句
            self.conn.commit()  # commit,提交数据
        except Exception as e:
            logger.info("执行sql出错{}".format(e))


db = MysqlDb()

if __name__ == '__main__':
    db = MysqlDb()
    result = db.select_db_all('select code from users_verifycode where mobile = 15959996163 order by id desc limit 1')
    print(result[0]["code"])
