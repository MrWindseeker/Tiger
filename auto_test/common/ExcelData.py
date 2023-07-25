import re
import sys, json, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.ExcelUtil import ExcelUtil
from common import ExcelConf, Base
from config.Conf import ConfigYaml

# 初始化ExcelConf
data_key = ExcelConf.ExcelConf()
# 初始化配置文件
conf_read = ConfigYaml()

class run_data:
    # def __init__(self, excel_name, sheet_by):
    def __init__(self):
        # 测试用例
        test_case = conf_read.get_test_case()
        case_sheet = conf_read.get_case_sheet()
        # 测试数据
        test_data = conf_read.get_test_data()
        test_sheet = conf_read.get_data_sheet()
        # 使用excel工具类，获取数据list
        self._case_excel = ExcelUtil(test_case, case_sheet)
        self._case_list = self._case_excel.data_list()
        self._data_excel = ExcelUtil(test_data, test_sheet)
        self._data_list = self._data_excel.data_list()

    # 获取所有测试用例
    def get_all_case(self):       
        return self._case_list

    # 获取所有测试数据
    def get_all_data(self):
        return self._data_list

    # 获取需要执行的测试用例
    def get_run_case(self):
        case_list = Base.find_dict(self._case_list, data_key.case_is_run, 'Y')
        return case_list
    

    # 获取前置测试用例
    def get_pre_case(self, pre, case_id):
        all_data = self.get_all_case()
        for pre_data in all_data:
            # if pre in dict(pre_data).values() and pre_data[data_key.case_id] != case_id:
            if pre == pre_data[data_key.case_id] and pre_data[data_key.case_id] != case_id:
                # print(pre_data[data_key.case_id])
                return pre_data

if __name__ == '__main__':
    # data_excel = ExcelUtil('test_data.xlsx', '接口测试用例_1')
    # testdata = run_data('test_data.xlsx', '接口测试用例_1')
    # conf_read = ConfigYaml()
    # excel_name = conf_read.get_excel_file()
    # excel_sheet = conf_read.get_excel_sheet()
    # testdata = run_data(excel_name, excel_sheet)
    # testdata = run_data().get_run_case()
    # print(testdata[0]['status_code'])
    # print(type(testdata[0]['status_code']))
    # print(testdata[0]['请求参数'])
    # print(type(testdata[0]['请求参数']))
    # print(json.loads(testdata[0]['请求参数']))
    # print(testdata[0]['headers'])
    # print(testdata[0]['cookies'])
    # print(testdata[1][data_key.case_db_verify])
    # print(type(testdata[2][data_key.case_db_verify]))
    # allcase = run_data().get_all_case()
    alldata = run_data().get_all_data()
    runcase = run_data().get_run_case()
    # print(runcase)
    print(alldata)
    # print(testdata[0]['前置条件'].split(','))
    # print(type(alldata[0]))
    # print(dict(alldata[0]).values())
    # print(alldata[0].values())
    # case_data = {'用例编号': 'hp_3', '模块': '首页', '接口名称': '首页', '请求url': 'https://www.taobao.com/', '前置条件': 'hp_2', '请求类型': 'GET', '请求参数类型': 'json', '请求参数': '', '预期结果': '"except_code":201', '实际结果': '', '是否运行': 'Y', 'headers': '', 'cookies': '', 'status_code': 200.0, '数据库验证': ''}
    # case_id = 'hp_5'
    # pre_data = run_data().get_pre_data('hp_6', case_id)
    # print(pre_data)
    # print(type(pre_data))
    # print(pre_data[data_key.case_data])
    # print(type(pre_data[data_key.case_data]))
    # print(pre_data[data_key.case_headers])
    # print(type(pre_data[data_key.case_headers]))