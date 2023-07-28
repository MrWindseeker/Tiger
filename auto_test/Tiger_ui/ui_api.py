import sys, os, json, random
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from Tiger_api.login_api import admin_login
from Tiger_api.admin_sys import admin_sys
from Tiger_api.timesheet_sys import timesheet_sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


test_tim = timesheet_sys()

def add_proj(asc_tk, eng_type):
    json_ts_eng = {'engagementType': '', 'businessUnit': '', 'role': '', 'managerialCntryOrLoc': '', 'engagementCode': None, 'engagementName': None, 'clientCode': None, 'clientName': None, 'employeeName': None, 'employeeGPN': None, 'managementUnit': '', 'subManagementUnit': '', 'pageNo': 1, 'pageSize': 100}
    eng_list = test_tim.get_eng_list(asc_tk, json_ts_eng)['body']['data']['list']
    if eng_list:
        for eng in eng_list:
            print('eng_name:{},eng_code:{},eng_isadd:{},eng_type:{},clientName:{}'.format(eng['engName'], eng['engCode'], eng['isAdd'], eng['engType'], eng['clientName']))
            if not eng['isAdd'] and eng['engType'] == eng_type:
                engCode = eng['engCode']
                data_eng_status = {'engCode': engCode, 'engType': eng['engType']}
                eng_status = test_tim.get_eng_status(asc_tk, data_eng_status)
                if eng['clientName'] != '':
                    engName = str(eng['engCode']) + '-' + str(eng['engName']) + ' - ' + str(eng['clientName'])
                else:
                    engName = str(eng['engCode']) + '-' + str(eng['engName'])
                print('eng_status:{}'.format(eng_status['body']['data']['status']))
                if eng_status['body']['data']['status'] == 'O':
                    json_add_eng = {'clientCode': eng['clientCode'], 'clientId': eng['clientId'], 'clientName': eng['clientName'], 'cntry': eng['cntry'], 'engCode': eng['engCode'], 'engName': eng['engName'], 'engType': eng['engType'], 'description': eng['description'], 'status': eng['status']}
                    test_tim.add_eng(asc_tk, json_add_eng)
                    return engName

def show_wait(driver, by, value, tim, rate):
    '''
    元素显示等待
    :param driver: 驱动
    :param by: 查找元素类型
    :param value: 查找元素属性值
    :param tim: 最长查找时间（秒）
    :param rate: 每隔多长时间查找一次元素（秒）默认0.5秒
    :return: 返回元素    '''
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