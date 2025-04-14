import sys, os, json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.LogUtil import LogUtil
from utils.ReqsUtil import ReqsUtil
from config.Tiger_Conf import Tiger_ConfigYaml

preuat_url = Tiger_ConfigYaml().get_preuat_url()
cli_list = Tiger_ConfigYaml().get_cli_list()

req = ReqsUtil()


class client_sys:
    def __init__(self):
        self.log = LogUtil.sys_log('client')

    # 客户列表查询接口
    def get_cli_list(self, acs_tk, json):
        cli_list_url = preuat_url + cli_list
        headers = {'Authorization':'Bearer {}'.format(acs_tk)}
        res = req.req_post(cli_list_url, json = json, headers=headers)
        return res