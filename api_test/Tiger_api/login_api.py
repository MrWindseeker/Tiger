import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.LogUtil import sys_log
from utils.ReqsUtil import ReqsUtil
from config.Tiger_Conf import Tiger_ConfigYaml

preuat_url = Tiger_ConfigYaml().get_preuat_url()
login = Tiger_ConfigYaml().get_admin_login()

req = ReqsUtil()

class admin_login():
    def __init__(self):
        self.log = sys_log('admin')

    # 登录系统
    def login(self, json):
        login_url = preuat_url + login
        res = req.req_post(login_url, json = json)
        return res
    

if __name__ =='__main__':
    test = admin_login()
    username = 'admin'
    password = 'admin123'
    json_login = {'username': username, 'password': password, 'captchaVerification': ''}
    login_test = test.login(json_login)
    access_token =login_test['body']['data']['accessToken']

    print(access_token)