import pymysql
import os
import sys
from pymysql.cursors import DictCursor

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.LogUtil import LogUtil


class MysqlUtil:
    """MySQL 数据库工具类，支持上下文管理，封装基本操作"""

    def __init__(self, host, user, passwd, database, port=3306, charset='utf8'):
        """初始化连接"""
        self.log = LogUtil.sys_log()
        self.conn = None
        self.cursor = None

        try:
            self.conn = pymysql.connect(
                host=host,
                port=port,
                user=user,
                passwd=passwd,
                database=database,
                charset=charset
            )
            self.cursor = self.conn.cursor(cursor=DictCursor)
            self.log.info("数据库连接成功")
        except Exception as e:
            self.log.error("数据库连接失败")
            self.log.exception(e)
            raise

    def fetchone(self, sql):
        """执行单条查询"""
        if self.sql_execute(sql):
            return self.cursor.fetchone()
        return None

    def fetchall(self, sql):
        """执行多条查询"""
        if self.sql_execute(sql):
            return self.cursor.fetchall()
        return []

    def execute(self, sql):
        """执行 SQL，返回是否成功"""
        return self.sql_execute(sql)

    def sql_execute(self, sql):
        """执行 SQL，内部调用"""
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            return True
        except Exception as e:
            self.log.error(f"SQL 执行失败: {sql}")
            self.log.exception(e)
            self.conn.rollback()
            return False

    def close(self):
        """关闭数据库连接"""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        self.log.info("数据库连接已关闭")

    def __enter__(self):
        """支持 with 语法"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出时自动关闭"""
        self.close()

    def __del__(self):
        """析构函数自动关闭连接"""
        self.close()