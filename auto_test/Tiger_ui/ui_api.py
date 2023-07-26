import sys, os, json, random
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from Tiger_api.login_api import admin_login
from Tiger_api.admin_sys import admin_sys
from Tiger_api.timesheet_sys import timesheet_sys


test_tim = timesheet_sys()

def add_proj(asc_tk, eng_type):
    json_ts_eng = {'engagementType': '', 'businessUnit': '', 'role': '', 'managerialCntryOrLoc': '', 'engagementCode': None, 'engagementName': None, 'clientCode': None, 'clientName': None, 'employeeName': None, 'employeeGPN': None, 'managementUnit': '', 'subManagementUnit': '', 'pageNo': 1, 'pageSize': 100}
    eng_list = test_tim.get_eng_list(asc_tk, json_ts_eng)['body']['data']['list']
    if eng_list:
        for eng in eng_list:
            # print(eng)
            if not eng['isAdd'] and eng['engType'] == eng_type:
                engCode = eng['engCode']
                data_eng_status = {'engCode': engCode, 'engType': eng['engType']}
                eng_status = test_tim.get_eng_status(asc_tk, data_eng_status)
                eng_name = engCode + '-' + eng['engName'] + ' - ' + eng['clientName']
                if eng_status['body']['data']['status'] == 'O':
                    json_add_eng = {'clientCode': eng['clientCode'], 'clientId': eng['clientId'], 'clientName': eng['clientName'], 'cntry': eng['cntry'], 'engCode': eng['engCode'], 'engName': eng['engName'], 'engType': eng['engType'], 'description': eng['description'], 'status': eng['status']}
                    test_tim.add_eng(asc_tk, json_add_eng)
                    return eng_name