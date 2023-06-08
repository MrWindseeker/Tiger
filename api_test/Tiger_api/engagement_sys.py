import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.LogUtil import sys_log
from utils.ReqsUtil import ReqsUtil
from config.Tiger_Conf import Tiger_ConfigYaml

preuat_url = Tiger_ConfigYaml().get_preuat_url()
eng_list = Tiger_ConfigYaml().get_eng_list()
eng_global_list = Tiger_ConfigYaml().get_eng_global_list()

req = ReqsUtil()

class engagement_sys:
    def __init__(self):
        self.log = sys_log('engagement')

    # 项目列表接口
    def get_eng_list(self, acs_tk, json):
        eng_list_url = preuat_url + eng_list
        headers = {'Authorization':'Bearer {}'.format(acs_tk)}
        res = req.req_post(eng_list_url, json = json, headers = headers)
        return res

    # 全局检索接口
    def get_eng_global_list(self, acs_tk, json):
        eng_global_list_url = preuat_url + eng_global_list
        headers = {'Authorization':'Bearer {}'.format(acs_tk)}
        res = req.req_post(eng_global_list_url, json = json, headers = headers)
        return res
