import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.YamlUtil import YamlUtil

# 1、获取项目基本目录
# 获取当前项目的绝对路径，__file__表示了当前文件的path
cur_path = os.path.abspath(__file__)
# print(cur_path)
# print(os.path.dirname(cur_path))

BASE_DIR = os.path.dirname(os.path.dirname(cur_path))
# D:\Python\Tiger\api_test
# print(BASE_DIR)

# 定义config目录的路径
# os.sep，Linux上代表'/'，Windows上代表'\'
_config_path = BASE_DIR + os.sep + 'config'
# 定义data目录的路径
_data_path = BASE_DIR + os.sep + 'data'
# 定义conf.yml文件的路径
_config_file = _config_path + os.sep + 'conf.yml'
# 定义db_conf.yml路径
_db_config_file = _config_path + os.sep + 'db_conf.yml'
# 定义excel_conf.conf路径
_excel_conf_file = _config_path + os.sep + 'excel_conf.conf'
# 定义log文件路径
_log_path = BASE_DIR + os.sep + 'logs'
# 定义pytest_report文件路径
_report_path = BASE_DIR + os.sep + 'report'
# 定义pytest_html路径
_pytest_path = BASE_DIR + os.sep + 'report' + os.sep + 'pytest_html'
# 定义allure_html路径
_allure_path = BASE_DIR + os.sep + 'report' + os.sep + 'allure_html'
# 定位open_allure文件路径
_allure_open = BASE_DIR + os.sep + 'report' + os.sep + 'generateAllureReport.bat'
# 定义压缩文件放置路径
_output_path = BASE_DIR + os.sep + 'report' + os.sep + 'allurereport'
# 定义case文件路径
_case_path = BASE_DIR + os.sep + 'Tiger_ui'


def get_case_path():
    """ 获取测试用例路径 """
    return _case_path

def get_config_path():
    """ 获取配置文件路径 """
    return _config_path

def get_data_path():
    """ 获取测试数据路径 """
    return _data_path

def get_config_file():
    """ 获取配置文件路径 """
    return _config_file

def get_db_config_file():
    """ 获取数据库配置文件路径 """
    return _db_config_file

def get_excel_config_file():
    """ 获取excel配置文件路径 """
    return _excel_conf_file

def get_log_path():
    """ 获取日志路径 """
    return _log_path

def get_report_path():
    """ 获取pytest报告路径 """
    return _report_path

def get_pytest_path():
    """ 获取pytest_html路径 """
    return _pytest_path

def get_allure_path():
    """ 获取allure_html路径 """
    return _allure_path

def get_allure_open():
    """ 获取allure_open路径 """
    return _allure_open

def get_output_path():
    """ 获取allure_open路径 """
    return _output_path


# 2、读取配置文件
class ConfigYaml:
    """ 配置文件读取类 """
    # 初始yaml读取配置文件
    def __init__(self):
        """ 初始化配置文件 """
        self.config = YamlUtil(get_config_file()).data()
        self.db_config = YamlUtil(get_db_config_file()).data()

    # 获取测试用例名称
    def get_test_case(self):
        """ 获取测试用例名称 """
        return self.config['BASE']['test']['test_case']

    # 获取测试用例sheet
    def get_case_sheet(self):
        """ 获取测试用例sheet """
        return self.config['BASE']['test']['case_sheet']
    
    # 获取测试用户文件
    def get_test_data(self):
        """ 获取测试用户文件 """
        return self.config['BASE']['test']['test_data']
    
    # 获取测试用户数据
    def get_data_sheet(self):
        """ 获取测试用户数据 """
        return self.config['BASE']['test']['data_sheet']

    # 获取日志级别
    def get_conf_log_level(self):
        """ 获取日志级别 """
        return self.config['BASE']['log_level']

    # 获取文件扩展名
    def get_conf_log_extension(self):
        """ 获取文件扩展名 """
        return self.config['BASE']['log_extension']

    # 获取数据库配置信息
    def get_db_conf_info(self, db_env):
        """ 获取数据库配置信息 """
        return self.db_config[db_env]

    # 获取邮件配置信息
    def get_email_info(self):
        """ 获取邮件配置信息 """
        return self.config['Email']

if __name__ == '__main__':
    conf_read = ConfigYaml()
    # print(conf_read.config)
    # print(conf_read.get_conf_url())
    # print(conf_read.get_conf_log_level())
    # print(conf_read.get_conf_log_extension())
    # print(conf_read.get_db_conf_info('db1'))
    # print(type(conf_read.get_db_conf_info('db1')))
    # print(conf_read.get_excel_file())
    # print(conf_read.get_test_data())
    # print(conf_read.get_data_sheet())
    # email_info = conf_read.get_email_info()
    # print(email_info)
    # to_recv = conf_read.get_email_info()['to_recv']
    # print(to_recv)
    # cc_recv = conf_read.get_email_info()['cc_recv']
    # # print(cc_receiver)
    # if not cc_recv:
    #     print('OK')
    db_local_info = conf_read.get_db_conf_info('msdb2')

    print(db_local_info)