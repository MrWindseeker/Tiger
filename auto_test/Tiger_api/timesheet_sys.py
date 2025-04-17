import sys, os, json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.LogUtil import LogUtil
from utils.ReqsUtil import ReqsUtil
from config.Tiger_Conf import Tiger_ConfigYaml

preuat_url = Tiger_ConfigYaml().get_preuat_url()
ts_home = Tiger_ConfigYaml().get_ts_home()
ts_list = Tiger_ConfigYaml().get_ts_list()
ts_info = Tiger_ConfigYaml().get_ts_info()
ts_submit = Tiger_ConfigYaml().get_ts_submit()
ts_eng_list = Tiger_ConfigYaml().get_ts_eng_list()
ts_my_eng = Tiger_ConfigYaml().get_ts_my_eng()
ts_add_eng = Tiger_ConfigYaml().get_ts_add_eng()
ts_eng_status = Tiger_ConfigYaml().get_eng_status()

req = ReqsUtil()

class timesheet_sys:
    def __init__(self):
        self.log = LogUtil.sys_log()

    # 首页home/info接口
    def get_ts_home(self, acs_tk, data):
        ts_home_url = preuat_url + ts_home
        headers = {'Authorization':'Bearer {}'.format(acs_tk)}
        res = req.req_get(ts_home_url, headers = headers, data = json.dumps(data))
        return res
    
    # 工时列表接口
    def get_ts_list(self, acs_tk, data):
        ts_list_url = preuat_url + ts_list
        headers = {'Authorization':'Bearer {}'.format(acs_tk)}
        res = req.req_get(ts_list_url, headers = headers, data = json.dumps(data))
        return res

    # 工时详情接口
    def get_ts_info(self, acs_tk, data = None):
        # timesheetId weekEnd 默认时，为查询当前周
        ts_info_url = preuat_url + ts_info
        headers = {'Authorization':'Bearer {}'.format(acs_tk)}
        if not data:
            res = req.req_get(ts_info_url, headers = headers, data = json.dumps(data))
        else:
            res = req.req_get(ts_info_url, headers = headers)
        return res
    
    # 项目查询接口
    def get_eng_list(self, acs_tk, json):
        ts_eng_list_url = preuat_url + ts_eng_list
        headers = {'Authorization':'Bearer {}'.format(acs_tk)}
        res = req.req_post(ts_eng_list_url, headers = headers, json = json)
        return res

    # 我的项目接口
    def get_my_eng(self, acs_tk, data):
        ts_my_eng_url = preuat_url + ts_my_eng
        headers = {'Authorization':'Bearer {}'.format(acs_tk)}
        res = req.req_get(ts_my_eng_url, headers = headers, data = json.dumps(data))
        return res
    
    # 添加项目接口
    def add_eng(self, acs_tk, json):
        ts_add_eng_url = preuat_url + ts_add_eng
        headers = {'Authorization':'Bearer {}'.format(acs_tk)}
        res = req.req_post(ts_add_eng_url, headers = headers, json = json)
        return res

    # 查询项目状态接口
    def get_eng_status(self, acs_tk, data):
        eng_code = data['engCode']
        eng_type = data['engType']
        ts_eng_status_url = preuat_url + ts_eng_status + '?' + 'engCode={}&engType={}'.format(eng_code, eng_type)
        headers = {'Authorization':'Bearer {}'.format(acs_tk)}
        res = req.req_get(ts_eng_status_url, headers = headers, data = json.dumps(data))
        return res
    
    # 工时提交接口
    def ts_submit(self, acs_tk, json):
        ts_submit_url = preuat_url + ts_submit
        headers = {'Authorization':'Bearer {}'.format(acs_tk)}
        res = req.req_post(ts_submit_url, headers = headers, json = json)
        return res