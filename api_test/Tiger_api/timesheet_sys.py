import sys, json

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.LogUtil import sys_log
from utils.ReqsUtil import ReqsUtil
from config.Tiger_Conf import Tiger_ConfigYaml

preuat_url = Tiger_ConfigYaml().get_preuat_url()
ts_home = Tiger_ConfigYaml().get_ts_home()
ts_list = Tiger_ConfigYaml().get_ts_list()
ts_info = Tiger_ConfigYaml().get_ts_info()
ts_submit = Tiger_ConfigYaml().get_ts_submit()
ts_eng_list = Tiger_ConfigYaml().get_ts_eng_list()


req = ReqsUtil()

class timesheet_sys:
    def __init__(self):
        self.log = sys_log('timesheet')

    # 首页home/info接口
    def get_ts_home(self, acs_tk):
        ts_home_url = preuat_url + ts_home
        headers = {'Authorization':'Bearer {}'.format(acs_tk)}
        data = {'fiscalYear':'FY23'}
        res = req.req_get(ts_home_url, headers = headers, data = json.dumps(data))
        return res
    
    # 工时列表接口
    def get_ts_list(self, acs_tk):
        ts_list_url = preuat_url + ts_list
        headers = {'Authorization':'Bearer {}'.format(acs_tk)}
        data = {'pageNo':99999, 'page':10}
        res = req.req_get(ts_list_url, headers = headers, data = json.dumps(data))
        return res

    # 工时详情接口
    def get_ts_info(self, acs_tk, data):
        # timesheetId weekEnd 默认时，为查询当前周
        ts_info_url = preuat_url + ts_info
        headers = {'Authorization':'Bearer {}'.format(acs_tk)}
        res = req.req_get(ts_info_url, headers = headers, data = json.dumps(data))
        return res
    
    # 项目查询接口
    def get_eng_list(self, acs_tk, json):
        ts_eng_list_url = preuat_url + ts_eng_list
        headers = {'Authorization':'Bearer {}'.format(acs_tk)}
        res = req.req_post(ts_eng_list_url, headers = headers, json = json)
        return res

    # 工时提交接口
    def ts_submit(self, acs_tk, json):
        ts_submit_url = preuat_url + ts_submit
        headers = {'Authorization':'Bearer {}'.format(acs_tk)}
        res = req.req_post(ts_submit_url, headers = headers, json = json)
        return res








