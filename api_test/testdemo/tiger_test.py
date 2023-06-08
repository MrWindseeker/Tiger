import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.LogUtil import sys_log
from utils.ReqsUtil import ReqsUtil
from config.Tiger_Conf import Tiger_ConfigYaml

preuat_url = Tiger_ConfigYaml().get_preuat_url()
login = Tiger_ConfigYaml().get_admin_login()
datarole = Tiger_ConfigYaml().get_datarole()

req = ReqsUtil()

class admin_login():
    def __init__(self):
        self.log = sys_log('admin')

    def login(self, username, password):
        login_url = preuat_url + login
        json = {'username': username, 'password': password, 'captchaVerification': ''}
        res = req.req_post(login_url, json = json)
        return res
    
    def datarole(self, acs_tk):
        datarole_url = preuat_url + datarole
        headers = {'Authorization':'Bearer {}'.format(acs_tk)}
        # print(headers)
        json = {'pageNo':1,'pageSize':10}
        res = req.req_post(datarole_url, json = json, headers = headers)
        return res

if __name__ =='__main__':
    test = admin_login()
    username = 'admin'
    password = 'admin123'
    login_test = test.login(username, password)
    access_token =login_test['body']['data']['accessToken']

    # print(access_token)
    datarole_test = test.datarole(access_token)

    print(datarole_test)