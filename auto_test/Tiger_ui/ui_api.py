import sys, os, math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Tiger_api.admin_sys import admin_sys
from Tiger_api.timesheet_sys import timesheet_sys
from utils.LogUtil import sys_log


test_tim = timesheet_sys()
test_admin = admin_sys()
log = sys_log('ui_api_log')

def add_check_eng(asc_tk, eng_type):
    json_ts_eng = {'engagementType': '{}'.format(eng_type), 'businessUnit': '', 'role': '', 'managerialCntryOrLoc': '', 'engagementCode': None, 'engagementName': None, 'clientCode': None, 'clientName': None, 'employeeName': None, 'employeeGPN': None, 'managementUnit': '', 'subManagementUnit': '', 'pageNo': 1, 'pageSize': 10}
    # 项目总数
    eng_num = test_tim.get_eng_list(asc_tk, json_ts_eng)['body']['data']['total']
    # 每次查询100条，最大循环次数
    count = min(3, math.ceil(eng_num / 100))
    for i in range(1, count + 1):
        json_ts_eng = {'engagementType': '{}'.format(eng_type), 'businessUnit': '', 'role': '', 'managerialCntryOrLoc': '', 'engagementCode': None, 'engagementName': None, 'clientCode': None, 'clientName': None, 'employeeName': None, 'employeeGPN': None, 'managementUnit': '', 'subManagementUnit': '', 'pageNo': i, 'pageSize': 100}
        eng_list = test_tim.get_eng_list(asc_tk, json_ts_eng)['body']['data']['list']
        if eng_list:
            for eng in eng_list:
                if not eng['isAdd'] and eng['engType'] == eng_type:
                    engCode = eng['engCode']
                    data_eng_status = {'engCode': engCode, 'engType': eng['engType']}
                    eng_status = test_tim.get_eng_status(asc_tk, data_eng_status)
                    if eng['clientName'] != '':
                        engName = str(eng['engCode']) + '-' + str(eng['engName']) + ' - ' + str(eng['clientName'])
                    else:
                        engName = str(eng['engCode']) + '-' + str(eng['engName'])
                    if eng_status['body']['data']['status'] == 'O' and eng_status['body']['data']['engActivities']:
                        json_add_eng = {'clientCode': eng['clientCode'], 'clientId': eng['clientId'], 'clientName': eng['clientName'], 'cntry': eng['cntry'], 'engCode': eng['engCode'], 'engName': eng['engName'], 'engType': eng['engType'], 'description': eng['description'], 'status': eng['status']}
                        test_tim.add_eng(asc_tk, json_add_eng)
                        return engName

def seach_engName(user, pwd, eng_type):
    json_login = {'username': user, 'password': pwd, 'captchaVerification': ''}
    login_result = test_admin.login(json_login)
    # 获取登录token
    acs_token = login_result['body']['data']['accessToken']
    # 查询用户已添加Type为Chargeable的项目
    data_eng_type = {"engType": eng_type}
    eng_list_result = test_tim.get_my_eng(acs_token, data_eng_type)
    eng_list = eng_list_result['body']['data']
    # 如果没有项目，则通过接口新增一个
    # engName 项目名，方便egagement选项的内容选择
    engName = ''
    if len(eng_list) <= 0:
        eng_name = add_check_eng(acs_token, eng_type)
        if not eng_name:
            log.error('该用户{}类型项目添加失败'.format(eng_type))
            assert False
        else:
            engName = eng_name
    elif len(eng_list) > 0:
        for eng in eng_list:
            data_eng_status = {'engCode': eng['engCode'], 'engType': eng_type}
            eng_status = test_tim.get_eng_status(acs_token, data_eng_status)
            if eng_status['body']['data']['status'] == 'O' and eng_status['body']['data']['engActivities']:
                if eng['clientName'] != '':
                    engName = str(eng['engCode']) + '-' + str(eng['engName']) + ' - ' + str(eng['clientName'])
                    break
                else:
                    engName = str(eng['engCode']) + '-' + str(eng['engName'])
                    break
        if not engName:
            eng_name = add_check_eng(acs_token, eng_type)
            if not eng_name:
                log.error('该用户{}类型项目添加失败'.format(eng_type))
                assert False
            else:
                engName = eng_name
    return engName

def show_wait(driver, by, value, tim, rate):
    '''
    元素显示等待
    :param driver: 驱动
    :param by: 查找元素类型
    :param value: 查找元素属性值
    :param tim: 最长查找时间（秒）
    :param rate: 每隔多长时间查找一次元素（秒）默认0.5秒
    :return: 返回元素
    '''
    wait = WebDriverWait(driver, tim, rate)
    if by == 'xpath':
        return wait.until(EC.visibility_of_element_located((By.XPATH, value)))
    if by == 'id':
        return wait.until(EC.visibility_of_element_located((By.ID, value)))
    if by == 'name':
        return wait.until(EC.visibility_of_element_located((By.NAME, value)))
    if by == 'class':
        return wait.until(EC.visibility_of_element_located((By.CLASS_NAME, value)))
    if by == 'css':
        return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, value)))
    if by == 'link':
        return wait.until(EC.visibility_of_element_located((By.LINK_TEXT, value)))
    if by == 'tag':
        return wait.until(EC.visibility_of_element_located((By.TAG_NAME, value)))
    if by == 'part_link':
        return wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, value)))