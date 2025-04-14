import pymysql
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.LogUtil import LogUtil


class MysqlUtil:
    """ Mysql数据库工具类 """

    def __init__(self, host, user, passwd, database, port = 3306, charset = 'utf8' ):
        """ 初始化Mysql数据库连接 """
        self.log = LogUtil.sys_log('mysql_log')

        self.conn = pymysql.connect(
            host = host,
            port = port,
            user = user,
            passwd = passwd,
            database = database,
            charset = charset
            )

        # 创建光标对象
        # cursor = pymysql.cursors.DictCursor  返回数据格式为字典,默认为元组
        self.cursor = self.conn.cursor(cursor = pymysql.cursors.DictCursor)

    # 创建查询,执行方法
    # 单个查询
    def fetchone(self, sql):
        """ 执行单个查询 """
        self.sql_execute(sql)
        return self.cursor.fetchone()

    # 多个查询
    def fetchall(self, sql):
        """ 执行多个查询 """
        self.sql_execute(sql)
        return self.cursor.fetchall()

    # 执行sql
    def sql_execute(self, sql):
        """ 执行sql语句 """
        try:
            if self.conn and self.cursor:
                self.cursor.execute(sql)
                self.conn.commit()
        except Exception as e:
            self.log.error('Mysql 执行失败！')
            self.log.error(e)
            self.conn.rollback()
            return False
        return True

# 关闭对象
    def __del__(self):
        """ 关闭对象 """
        # 关闭光标对象
        if self.cursor:
            # print('关闭光标')
            self.cursor.close()
        
        # 关闭连接对象
        if self.conn:
            # print('关闭连接')
            self.conn.close()

if __name__ == '__main__':
    mysql = MysqlUtil('localhost', 'root', '123456', 'test')
    sql = 'select name from test.student'
    res = mysql.fetchone(sql)
    # sql_2 = 'update test.student set age = 444 where id = 1'
    # 关闭连接或者关闭光标后，后续数据库操作均无法执行
    # del mysql.conn
    # del mysql.cursor
    # mysql.sql_execute(sql_2)
    res_2 = mysql.fetchone(sql)
    print(res)
    for i in res:
        print(i)
    # print(res_2)
    # MysqlUtil类执行完成后，__del__自动关闭连接和光标
    # 执行del时报错，已无数据库连接或者光标
    # del mysql.conn
    # del mysql.cursor
    