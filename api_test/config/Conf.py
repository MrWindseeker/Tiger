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

    # 获取需要的信息
    def get_conf_url(self):
        return self.config['BASE']['test']['url']

    # 获取lbs_apikey
    def get_lbs_apikey(self):
        return self.config['BASE']['lbs_api']['api_key']    

    # 获取lbs_api的url
    def get_lbs_api(self):
        return self.config['BASE']['lbs_api']['api_url']
    
    # 获取转经纬度接口
    def get_to_lnglat(self):
        return self.config['BASE']['lbs_api']['to_lnglat']

    # 获取转地址接口
    def get_to_local(self):
        return self.config['BASE']['lbs_api']['to_local']

    # 获取ocr_apikey
    def get_ocr_apikey(self):
        return self.config['BASE']['ocr_api']['api_key']

    # 获取ocr_secretkey
    def get_ocr_secretkey(self):
        return self.config['BASE']['ocr_api']['secret_key']

    # 获取ocr_api的url
    def get_ocr_api(self):
        return self.config['BASE']['ocr_api']['api_url']

    # 获取access_token接口
    def get_ocr_accesstoken(self):
        return self.config['BASE']['ocr_api']['access_token']

    # 获取accurate_basic接口
    def get_ocr_accurate(self):
        return self.config['BASE']['ocr_api']['accurate_basic']

    # 获取general_basic接口
    def get_ocr_general(self):
        return self.config['BASE']['ocr_api']['general_basic']

    # 获取idcard识别接口
    def get_ocr_idcard(self):
        return self.config['BASE']['ocr_api']['idcard']

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
    # print(conf_read.get_lbsapi_url())
    url = conf_read.get_lbs_api() + '/geocoding/v3/?address={}&output=json&ak={}&callback=showLocation'

    # print(conf_read.get_lbs_apikey())
    # print(conf_read.get_lbs_api())
    # print(conf_read.get_to_lnglat())
    # print(conf_read.get_to_local())
    # print(conf_read.get_excel_sheet())
    email_info = conf_read.get_email_info()
    print(email_info)
    to_recv = conf_read.get_email_info()['to_recv']
    print(to_recv)
    cc_recv = conf_read.get_email_info()['cc_recv']
    # print(cc_receiver)
    if not cc_recv:
        print('OK')