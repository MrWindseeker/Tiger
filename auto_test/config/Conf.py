import os
import sys

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
# 定义log文件路径
_log_path = BASE_DIR + os.sep + 'logs'
# 定义report文件路径
_report_path = BASE_DIR + os.sep + 'report'
# 定义allure_report路径
_allure_path = BASE_DIR + os.sep + 'report/html'
# 定位open_allure文件路径
_allure_open = BASE_DIR + os.sep + 'report/generateAllureReport.bat'
# 定义压缩文件放置路径
_output_path = BASE_DIR + os.sep + 'report/allurereport'

def get_config_path():
    return _config_path

def get_data_path():
    return _data_path

def get_config_file():
    return _config_file

def get_db_config_file():
    return _db_config_file

def get_log_path():
    return _log_path

def get_report_path():
    return _report_path

def get_allure_path():
    return _allure_path

def get_allure_open():
    return _allure_open

def get_output_path():
    return _output_path


# 2、读取配置文件
class ConfigYaml:
    # 初始yaml读取配置文件
    def __init__(self):
        self.config = YamlUtil(get_config_file()).data()
        self.db_config = YamlUtil(get_db_config_file()).data()

    # 获取测试用例名称
    def get_excel_file(self):
        return self.config['BASE']['test']['case_file']

    # 获取测试用例sheet
    def get_excel_sheet(self):
        return self.config['BASE']['test']['case_sheet']

    # 获取日志级别
    def get_conf_log_level(self):
        return self.config['BASE']['log_level']

    # 获取文件扩展名
    def get_conf_log_extension(self):
        return self.config['BASE']['log_extension']

    # 获取数据库配置信息
    def get_db_conf_info(self, db_env):
        return self.db_config[db_env]

    # 获取邮件配置信息
    def get_email_info(self):
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
    # print(conf_read.get_excel_sheet())
    # print(conf_read.get_excel_sheet())
    email_info = conf_read.get_email_info()
    print(email_info)
    to_recv = conf_read.get_email_info()['to_recv']
    print(to_recv)
    cc_recv = conf_read.get_email_info()['cc_recv']
    # print(cc_receiver)
    if not cc_recv:
        print('OK')