from utils.LogUtil import sys_log
from utils.ReqsUtil import ReqsUtil
from config.Tiger_Conf import Tiger_ConfigYaml

preuat_url = Tiger_ConfigYaml().get_preuat_url()
oppor_list = Tiger_ConfigYaml().get_oppor_list()
oppor_global_list = Tiger_ConfigYaml().get_oppor_global_list()
oppor_info = Tiger_ConfigYaml().get_oppor_info()

req = ReqsUtil()

class opportunity_sys:
    def __init__(self):
        self.log = sys_log('opportunity')

    # 商机列表接口
    def get_oppor_list(self, acs_tk, json):
        oppor_list_url = preuat_url + oppor_list
        headers = {'Authorization':'Bearer {}'.format(acs_tk)}
        res = req.req_post(oppor_list_url, json = json, headers = headers)
        return res

    # 全局检索接口
    def get_oppor_global_list(self, acs_tk, json):
        oppor_global_list_url = preuat_url + oppor_global_list
        headers = {'Authorization':'Bearer {}'.format(acs_tk)}
        res = req.req_post(oppor_global_list_url, json = json, headers = headers)
        return res

    # 商机详情接口
    def get_oppor_info(self, acs_tk, oppor_id):
        oppor_info_url = preuat_url + oppor_info + '?' + 'id={}'.format(oppor_id)
        headers = {'Authorization':'Bearer {}'.format(acs_tk)}
        res = req.req_get(oppor_info_url, headers = headers)
        return res

