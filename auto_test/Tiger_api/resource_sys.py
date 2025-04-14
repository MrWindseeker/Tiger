import sys, os, json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.LogUtil import LogUtil
from utils.ReqsUtil import ReqsUtil
from config.Tiger_Conf import Tiger_ConfigYaml

preuat_url = Tiger_ConfigYaml().get_preuat_url()
res_list = Tiger_ConfigYaml().get_res_list()
mmt_cal = Tiger_ConfigYaml().get_mmt_cal()
mmt_info = Tiger_ConfigYaml().get_mmt_info()
mmt_fin_rate = Tiger_ConfigYaml().get_mmt_fin_rate()
cct_cal = Tiger_ConfigYaml().get_cct_cal()
cct_info = Tiger_ConfigYaml().get_cct_info()
cct_res_list = Tiger_ConfigYaml().get_cct_res_list()

req = ReqsUtil()


class resource_sys:
    def __init__(self):
        self.log = LogUtil.sys_log('resource')

    # 获取资源列表接口
    def get_res_list(self, acs_tk, json):
        res_list_url = preuat_url + res_list
        headers = {'Authorization':'Bearer {}'.format(acs_tk)}
        res = req.req_post(res_list_url, json = json, headers=headers)
        return res

    # mmt计算接口
    def get_mmt_cal(self, acs_tk, json):
        mmt_cal_url = preuat_url + mmt_cal
        headers = {'Authorization':'Bearer {}'.format(acs_tk)}
        res = req.req_post(mmt_cal_url, headers=headers, json = json)
        return res

    # mmt详情接口
    def get_mmt_info(self, acs_tk):
        mmt_info_url = preuat_url + mmt_info
        headers = {'Authorization':'Bearer {}'.format(acs_tk)}
        res = req.req_get(mmt_info_url, headers=headers)
        return res

    # mmt获取财务rate接口
    def get_mmt_fin_rate(self, acs_tk, json):
        mmt_fin_rate_url = preuat_url + mmt_fin_rate
        headers = {'Authorization':'Bearer {}'.format(acs_tk)}
        res = req.req_post(mmt_fin_rate_url, headers=headers, json = json)
        return res

    # cct计算接口
    def get_cct_cal(self, acs_tk, json):
        cct_cal_url = preuat_url + cct_cal
        headers = {'Authorization':'Bearer {}'.format(acs_tk)}
        res = req.req_post(cct_cal_url, headers=headers, json = json)
        return res

    # cct详情接口
    def get_cct_info(self, acs_tk, data):
        planId = data['planId']
        version = data['version']
        operator = data['operator']
        cct_info_url = preuat_url + cct_info + '?' + 'planId={}&version={}&operator={}'.format(planId, version, operator)
        headers = {'Authorization':'Bearer {}'.format(acs_tk)}
        res = req.req_get(cct_info_url, headers=headers)
        return res

    # cct获取资源列表接口
    def get_cct_res_list(self, acs_tk, json):
        cct_res_list_url = preuat_url + cct_res_list
        headers = {'Authorization':'Bearer {}'.format(acs_tk)}
        res = req.req_post(cct_res_list_url, headers=headers, json = json)
        return res
