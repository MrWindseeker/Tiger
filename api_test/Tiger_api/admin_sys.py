import sys
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.LogUtil import sys_log
from utils.ReqsUtil import ReqsUtil
from config.Tiger_Conf import Tiger_ConfigYaml

preuat_url = Tiger_ConfigYaml().get_preuat_url()
login = Tiger_ConfigYaml().get_admin_login()
datarole = Tiger_ConfigYaml().get_admin_login()

req = ReqsUtil()

class admin_sys:
    def __init__(self):
        self.log = sys_log('admin')

    # 登录系统
    def login(self, json):
        login_url = preuat_url + login
        res = req.req_post(login_url, json = json)
        return res

    # 数据权限接口
    def get_datarole(self, acs_tk, json):
        datarole_url = preuat_url + datarole
        headers = {'Authorization':'Bearer {}'.format(acs_tk)}
        res = req.req_post(datarole_url, headers = headers, json = json)
        return res