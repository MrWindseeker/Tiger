import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.YamlUtil import YamlUtil

# 1、获取项目基本目录
cur_path = os.path.abspath(__file__)
# print(cur_path)

BASE_DIR = os.path.dirname(os.path.dirname(cur_path))
# print(BASE_DIR)

# 定义Tiger_Config目录的路径
_config_path = os.path.join(BASE_DIR, 'config')

# 定义tiger_conf.yml文件的路径
_tiger_conf_file = os.path.join(_config_path, 'tiger_conf.yml')

def get_config_path():
    return _tiger_conf_file

# 2、读取配置文件
class Tiger_ConfigYaml:
    # 初始yaml读取配置文件
    def __init__(self):
        self.config = YamlUtil(get_config_path()).data()

    # 获取pre_uat环境url
    def get_preuat_url(self):
        return self.config['Tiger_Api']['PreUat_Env']

    # 后台管理系统登录接口
    def get_admin_login(self):
        return self.config['Tiger_Api']['Url']['AdminApi']['Login']

    # 后台管理数据权限接口
    def get_admin_datarole(self):
        return self.config['Tiger_Api']['Url']['AdminApi']['datarole']

    # 工时系统首页接口
    def get_ts_home(self):
        return self.config['Tiger_Api']['Url']['Timesheet']['ts_home']

    # 工时系统工时列表接口
    def get_ts_list(self):
        return self.config['Tiger_Api']['Url']['Timesheet']['ts_list']

    # 工时系统工时详情接口
    def get_ts_info(self):
        return self.config['Tiger_Api']['Url']['Timesheet']['ts_info']

    # 工时系统项目查询接口
    def get_ts_eng_list(self):
        return self.config['Tiger_Api']['Url']['Timesheet']['ts_eng_list']
    
    # 工时系统工时提交接口
    def get_ts_submit(self):
        return self.config['Tiger_Api']['Url']['Timesheet']['ts_submit']
    
    # 商机系统商机列表接口
    def get_opp_list(self):
        return self.config['Tiger_Api']['Url']['Opportunity']['opp_list']

    # 商机系统全局检索接口
    def get_opp_global_list(self):
        return self.config['Tiger_Api']['Url']['Opportunity']['opp_global_list']

    # 商机系统商机详情接口
    def get_opp_info(self):
        return self.config['Tiger_Api']['Url']['Opportunity']['opp_info']
    
    # 项目系统项目列表接口
    def get_eng_list(self):
        return self.config['Tiger_Api']['Url']['Engagement']['eng_list']

    # 项目系统全局检索接口
    def get_eng_global_list(self):
        return self.config['Tiger_Api']['Url']['Engagement']['eng_global_list']

    # 资源系统资源列表接口
    def get_res_list(self):
        return self.config['Tiger_Api']['Url']['Resource']['res_list']
    
    # 资源系统mmt计算接口
    def get_mmt_cal(self):
        return self.config['Tiger_Api']['Url']['Resource']['mmt_cal']

    # 资源系统mmt详情接口
    def get_mmt_info(self):
        return self.config['Tiger_Api']['Url']['Resource']['mmt_info']
    
    # 资源系统mmt获取财务rate接口
    def get_mmt_fin_rate(self):
        return self.config['Tiger_Api']['Url']['Resource']['mmt_fin_rate']

    # 资源系统cct计算接口
    def get_cct_cal(self):
        return self.config['Tiger_Api']['Url']['Resource']['cct_cal']

    # 资源系统cct详情接口
    def get_cct_info(self):
        return self.config['Tiger_Api']['Url']['Resource']['cct_info']

    # 资源系统cct获取资源列表接口
    def get_cct_res_list(self):
        return self.config['Tiger_Api']['Url']['Resource']['cct_res_list']
    
    # 客户中心客户查询接口
    def get_cli_list(self):
        return self.config['Tiger_Api']['Url']['Client']['cli_list']


if __name__ == '__main__':
    conf_test = Tiger_ConfigYaml()
    print(get_config_path())
    print(conf_test.get_preuat_url())
    print(conf_test.get_admin_login())
    print(conf_test.get_opp_list())
    print(conf_test.get_opp_global_list())
    print(conf_test.get_opp_info())



