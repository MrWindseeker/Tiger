import sys, os, json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.LogUtil import sys_log
from utils.ReqsUtil import ReqsUtil
from config.Tiger_Conf import Tiger_ConfigYaml

preuat_url = Tiger_ConfigYaml().get_preuat_url()
opp_list = Tiger_ConfigYaml().get_opp_list()
opp_global_list = Tiger_ConfigYaml().get_opp_global_list()
opp_info = Tiger_ConfigYaml().get_opp_info()

req = ReqsUtil()

class opportunity_sys:
    def __init__(self):
        self.log = sys_log('opportunity')

    # 商机列表接口
    def get_opp_list(self, acs_tk, json):
        opp_list_url = preuat_url + opp_list
        headers = {'Authorization':'Bearer {}'.format(acs_tk)}
        res = req.req_post(opp_list_url, json = json, headers = headers)
        return res

    # 全局检索接口
    def get_opp_global_list(self, acs_tk, json):
        opp_global_list_url = preuat_url + opp_global_list
        headers = {'Authorization':'Bearer {}'.format(acs_tk)}
        res = req.req_post(opp_global_list_url, json = json, headers = headers)
        return res

    # 商机详情接口
    def get_opp_info(self, acs_tk, opp_id):
        opp_info_url = preuat_url + opp_info + '?' + 'id={}'.format(opp_id)
        headers = {'Authorization':'Bearer {}'.format(acs_tk)}
        res = req.req_get(opp_info_url, headers = headers)
        return res

