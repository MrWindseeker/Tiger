import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.YamlUtil import YamlUtil

# 1、获取项目基本目录
cur_path = os.path.abspath(__file__)
# print(cur_path)

BASE_DIR = os.path.dirname(os.path.dirname(cur_path))
# print(BASE_DIR)

# 定义Ph_Config目录的路径
_config_path = os.path.join(BASE_DIR, 'config')

# 定义ph_conf.yml文件的路径
_ph_conf_file = os.path.join(_config_path, 'ph_conf.yml')

def get_config_path():
    return _ph_conf_file

# 2、读取配置文件
class Ph_ConfigYaml:
    # 初始yaml读取配置文件
    def __init__(self):
        self.config = YamlUtil(get_config_path()).data()

    # 获取测试环境url
    def get_test_url(self):
        return self.config['API']['Test_Env']

    # 获取快捷登录图形验证码imgtoken接口
    def get_imgtk_sms(self):
        return self.config['API']['Url']['App_User']['ImgToken_Sms']

    # 获取图片验证码接口
    def get_vrfimg(self):
        return self.config['API']['Url']['App_User']['VerifyImg']

    # 获取手机验证接口
    def get_vrfph(self):
        return self.config['API']['Url']['App_User']['VerifyPhone']

    # 获取短信验证码登录接口
    def get_login_vrfcd(self):
        return self.config['API']['Url']['App_User']['Login_VerifyCode']

    # 获取密码登录接口
    def get_login_pwd(self):
        return self.config['API']['Url']['App_User']['Login_PassWord']

    # 获取首页信息接口
    def get_mainpage_info(self):
        return self.config['API']['Url']['App_MainPage']['MainPage_Info']
    
    # 获取用户主状态信息接口
    def get_mainstatus_info(self):
        return self.config['API']['Url']['App_MainPage']['MainStatus_Info']

if __name__ == '__main__':
    conf_test = Ph_ConfigYaml()
    print(conf_test.get_test_url())
    print(conf_test.get_imgtk_sms())
