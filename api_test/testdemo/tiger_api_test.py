import sys, os, json, random
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Tiger_api.login_api import admin_login
from Tiger_api.admin_sys import admin_sys
from Tiger_api.timesheet_sys import timesheet_sys
from Tiger_api.opportunity_sys import opportunity_sys
from Tiger_api.engagement_sys import engagement_sys
from Tiger_api.resource_sys import resource_sys
from Tiger_api.client_sys import client_sys


def json_file(file_name):
    path = 'C:/Users/Windseeker/Desktop'
    file_path = os.path.join(path,file_name)
    with open(file_path, 'r', encoding='utf8') as f:
        json_data = json.load(f)
    return json_data

if __name__ == '__main__':
    username = 'Leanne.Du'
    password = '123456'
    json_login = {'username': username, 'password': password, 'captchaVerification': ''}

    test_login = admin_login()
    test_datarole = admin_sys()
    test_timesheet = timesheet_sys()
    test_opportunity = opportunity_sys()
    test_engagement = engagement_sys()
    test_resource = resource_sys()
    test_client = client_sys()

    login_result = test_login.login(json_login)
    acs_tk = login_result['body']['data']['accessToken']

    # json_adm_datarole = {'pageNo':1,'pageSize':10}
    # datarole_result = test_datarole.get_datarole(acs_tk, json_adm_datarole)

    # data_ts_home = {'fiscalYear':'FY23'}
    # ts_home_result = test_timesheet.get_ts_home(acs_tk, data_ts_home)
    # data_ts_list = {'pageNo':99999, 'page':10}
    # ts_list_result = test_timesheet.get_ts_list(acs_tk, data_ts_list)
    data_ts_info = {'timesheetId':2209217882, 'weekEnd':'2023-06-02'}
    ts_info_result = test_timesheet.get_ts_info(acs_tk, data_ts_info)
    # json_ts_submit = {"competency":"","id":"2209217881","itemList":[{"id":6156216,"activity":"0000","activityDescription":"General","engCode":"11288828","engName":"UOTM XWAHHWDM KHFGDKT","friday":"1.0","loc1":"CHN","loc2":"SHANGHAI","monday":"1.0","description":"test110022331","saturday":None,"staffNo":"6715","sunday":None,"thursday":"1.0","timeType":"01","tuesday":"1.0","type":"C","wednesday":"1.0","taskType":None,"engDescription":"UOTM XWAHHWDM KHFGDKT - UOTM XWAHHWDM KHFGDKT","overtimeApproverEm":None,"overtimeApproverEp":None,"clientName":None,"engSubType":"EXT","bdId":None,"remark":None},{"id":6156217,"activity":"0000","activityDescription":"General","engCode":"22759833","engName":"TXW1588-60 YABR Zggxw","friday":"1.0","loc1":"CHN","loc2":"SHANGHAI","monday":"1.0","description":"test110022332","saturday":None,"staffNo":"6715","sunday":None,"thursday":"1.0","timeType":"01","tuesday":"1.0","type":"C","wednesday":"1.0","taskType":None,"engDescription":"TXW1588-60 YABR Zggxw - Uqmldij Bkxhmj Mlsxv Salc Jif.","overtimeApproverEm":None,"overtimeApproverEp":None,"clientName":None,"engSubType":"EXT","bdId":None,"remark":None},{"id":6156218,"activity":"0000","activityDescription":"General","engCode":"22823558","engName":"GWT1587-89 YABR Nwbwl","friday":"1.0","loc1":"CHN","loc2":"SHANGHAI","monday":"1.0","description":"test110022333","saturday":None,"staffNo":"6715","sunday":None,"thursday":"1.0","timeType":"01","tuesday":"1.0","type":"C","wednesday":"1.0","taskType":None,"engDescription":"GWT1587-89 YABR Nwbwl - Uqmldij Bkxhmj Bieyoer Khfgdkt","overtimeApproverEm":None,"overtimeApproverEp":None,"clientName":None,"engSubType":"EXT","bdId":None,"remark":None},{"id":6156219,"activity":"0000","activityDescription":"General","engCode":"22873198","engName":"GWT1587-60 Urhrhsa BULYP ","friday":"1.0","loc1":"CHN","loc2":"SHANGHAI","monday":"1.0","description":"test110022334","saturday":None,"staffNo":"6715","sunday":None,"thursday":"1.0","timeType":"01","tuesday":"1.0","type":"C","wednesday":"1.0","taskType":None,"engDescription":"GWT1587-60 Urhrhsa BULYP  - Dopzrlb Hscdmrn Dstei Kvfak Dnweo Bi., Qdc.","overtimeApproverEm":None,"overtimeApproverEp":None,"clientName":None,"engSubType":"EXT","bdId":None,"remark":None},{"id":6156220,"activity":"0000","activityDescription":"General","engCode":"22874203","engName":"GWT1587-60 Wllimrodb Syaftoeh","friday":"2.0","loc1":"CHN","loc2":"SHANGHAI","monday":"2.0","description":"test110022335","saturday":None,"staffNo":"6715","sunday":None,"thursday":"2.0","timeType":"01","tuesday":"2.0","type":"C","wednesday":"2.0","taskType":None,"engDescription":"GWT1587-60 Wllimrodb Syaftoeh - Hqeanylke Adahu Rc.,Igt.","overtimeApproverEm":None,"overtimeApproverEp":None,"clientName":None,"engSubType":"EXT","bdId":None,"remark":None},{"id":6156221,"activity":"0000","activityDescription":"General","engCode":"22889158","engName":"GWT1587-60 OXQ_XERZI NY","friday":"2.0","loc1":"CHN","loc2":"SHANGHAI","monday":"2.0","description":"test110022336","saturday":None,"staffNo":"6715","sunday":None,"thursday":"2.0","timeType":"01","tuesday":"2.0","type":"C","wednesday":"2.0","taskType":None,"engDescription":"GWT1587-60 OXQ_XERZI NY - Dkgujpkgo (Rojcx) Rc., Igt","overtimeApproverEm":None,"overtimeApproverEp":None,"clientName":None,"engSubType":"EXT","bdId":None,"remark":None}],"region":"","description":"","serviceLine":"","staffType":"","status":"02","subServiceLine":"","weekEnd":"1685030400000","taskType":"","engSubType":"","engDescription":"","overtimeApproverEm":"","overtimeApproverEp":"","bdId":""}
    # ts_submit_result = test_timesheet.ts_submit(acs_tk, json_ts_submit)
    # json_ts_eng = {"engagementType": "", "businessUnit": "", "role": "", "managerialCntryOrLoc": "CN01", "engagementCode": None, "engagementName": None, "clientCode": None, "clientName": None, "employeeName": None, "employeeGPN": None, "managementUnit": "", "subManagementUnit": "", "pageNo": 1, "pageSize": 10}
    # ts_eng_result = test_timesheet.get_eng_list(acs_tk, json_ts_eng)

    # json_opp_list = {"pageSize": 100, "pageNo": 1}
    # opppor_list_result = test_opportunity.get_opp_list(acs_tk, json_opp_list)
    # json_opp_global = {"opprKeyword": None, "fiscalYear": ["FY23"], "pageNo": 1, "pageSize": 10, "sort": "createTime"}
    # opp_global_list_result = test_opportunity.get_opp_global_list(acs_tk, json_opp_global)
    # opp_info_reuslt = test_opportunity.get_opp_info(acs_tk, 2683442)

    # json_eng_list = {"fiscalyears": [], "status": [], "scopes": [], "fuzzysearchkeywords": None, "fuzzysearchtype": None, "availableAmount": None, "createTime": "desc", "sort": "createTime:desc", "pageNo": 1, "pageSize": 20}
    # eng_list_result = test_engagement.get_eng_list(acs_tk, json_eng_list)
    # json_eng_global = {"fuzzysearchkeywords": "", "fuzzysearchtype": "02", "pageNo": 1, "pageSize": 100, "sort": "01", "servicelinecondition": {"servicelinecodes": [], "subservicelinecodes": []}, "ep": [], "em": [], "erp": {}, "eaf": {}, "margin": {}, "createdate": {}, "servicecodecondition": {"globalservicecodes": [], "localservicecodes": []}, "industrycondition": {"industrycodes": [], "subindustrycodes": []}}
    # eng_global_result = test_engagement.get_eng_global_list(acs_tk, json_eng_global)

    # json_res_list = {"pageSize": 10, "pageNo": 1}
    # res_list_result = test_resource.get_res_list(acs_tk, json_res_list)
    # json_mmt_cal = 'json_mmt_cal.json'
    # json_mmt_cal = json_file(json_mmt_cal)
    # mmt_cal_result = test_resource.get_mmt_cal(acs_tk, json_mmt_cal)
    # mmt_info_result = test_resource.get_mmt_info(acs_tk)
    # json_mmt_fin_rate = 'json_mmt_fin_rate.json'
    # json_mmt_fin_rate = json_file(json_mmt_fin_rate)
    # json_mmt_fin_rate['resource_name'] = random.randint(1,99999)
    # mmt_fin_rate_result = test_resource.get_mmt_fin_rate(acs_tk, json_mmt_fin_rate)
    # json_cct_cal = 'json_cct_cal.json'
    # json_cct_cal = json_file(json_cct_cal)
    # cct_cal_result = test_resource.get_cct_cal(acs_tk, json_cct_cal)
    # data_cct_info = {'planId':1661713764907315201, 'version':1, 'operator':'CN011019458'}
    # cct_info_result = test_resource.get_cct_info(acs_tk, data_cct_info)
    # json_cct_res_list = 'json_cct_res_list.json'
    # json_cct_res_list = json_file(json_cct_res_list)
    # cct_res_list_result = test_resource.get_cct_res_list(acs_tk, json_cct_res_list)

    # json_cli_list = {"country": [], "province": [], "city": [], "area": [], "region": [], "marketSegment": [], "office": [], "segment": [], "subStatus": [], "channel": [], "sector": [], "subSector": [], "keyword": "china", "entityType": [], "status": [], "pageNo": 1, "pageSize": 10}
    # cli_list_result = test_client.get_cli_list(acs_tk, json_cli_list)
    
    print(ts_info_result)

    


