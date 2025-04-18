import pymysql, sys, os
from pymysql.cursors import DictCursor
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.LogUtil import LogUtil


class MysqlUtil:
    """ Mysql数据库工具类 """
    def __init__(self, host, user, passwd, database, port = 3306, charset = 'utf8' ):
        """
        初始化Mysql数据库连接
        :param host: 数据库地址
        :param user: 用户名
        :param passwd: 密码
        :param database: 数据库名
        :param port: 端口号
        :param charset: 编码
        """
        self.log = LogUtil.sys_log()
        self.conn = None
        self.cursor = None

        try:
            self.conn = pymysql.connect(
                host = host,
                port = port,
                user = user,
                passwd = passwd,
                database = database,
                charset = charset
            )
            self.cursor = self.conn.cursor(cursor = DictCursor)
            self.log.info('数据库连接成功')
        except Exception as e:
            self.log.error('数据库连接失败')
            self.log.exception(e)
            raise

    # 创建查询,执行方法
    # 单个查询
    def query_one(self, sql, params = None):
        """ 执行单个查询 """
        if self.__sql_execute(sql, params):
            return self.cursor.fetchone()
        return None

    # 多个查询
    def query_batch(self, sql, params = None):
        """ 执行多个查询 """
        if self.__sql_execute(sql, params):
            return self.cursor.fetchall()
        return []
    
    def insert(self, sql, params = None):
        """ 执行单条插入操作 """
        return self.__sql_execute(sql, params)

    def insert_batch(self, sql, param_list):
        """ 批量插入操作 """
        try:
            self.log.debug('批量执行 SQL: {}, 参数列表: {}'.format(sql, param_list))
            self.cursor.executemany(sql, param_list)
            self.conn.commit()
            return True
        except Exception as e:
            self.log.error('批量插入失败: {}'.format(sql))
            self.log.exception(e)
            self.conn.rollback()
            return False
    
    def execute_raw(self, sql, params = None):
        """ 执行任意 SQL，返回是否成功 """
        return self.__sql_execute(sql, params)

    def update(self, sql, params = None):
        """ 执行单条更新操作 """
        return self.__sql_execute(sql, params)

    def delete(self, sql, params = None):
        """ 执行单条删除操作 """
        return self.__sql_execute(sql, params)

    # 执行sql
    def __sql_execute(self, sql, params = None):
        """ 执行 SQL 语句，可选参数绑定，返回是否成功 """
        try:
            self.log.debug('执行 SQL: {}, 参数: {}'.format(sql, params))
            self.cursor.execute(sql, params)
            self.conn.commit()
            return True
        except Exception as e:
            self.log.error('SQL 执行失败: {}, 参数: {}'.format(sql, params))
            self.log.exception(e)
            self.conn.rollback()
            return False  

    def __close(self):
        """ 关闭数据库连接 """
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        self.log.info('数据库连接已关闭')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__close()


if __name__ == '__main__':
    from config import Conf

    conf_read = Conf.ConfigYaml()
    db_local_info = conf_read.get_db_conf_info('mysql-local')
    host = db_local_info['db_host']
    user = db_local_info['db_user']
    passwd = db_local_info['db_passwd']
    database = db_local_info['db_database']
    port = db_local_info['db_port']
    charset = db_local_info['db_charset']
    # 创建MysqlUtil对象
    with MysqlUtil(host, user, passwd, database, port, charset) as mysql_util:
        current_max_code = 'select * from dealer_master order by dealer_code desc limit 1'
        # sql = 'select * from china_region limit 10'
        res = mysql_util.query_one(current_max_code)
        to_be_max_code = res['dealer_code']
        mysql_util.log.info(to_be_max_code)