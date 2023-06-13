import re
import sys, json, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.ExcelUtil import ExcelUtil
from common import ExcelConf
from config.Conf import ConfigYaml

# 初始化ExcelConf
data_key = ExcelConf.ExcelConf()
# 初始化配置文件
conf_read = ConfigYaml()

class run_data:
    # def __init__(self, excel_name, sheet_by):
    def __init__(self):
        excel_name = conf_read.get_excel_file()
        excel_sheet = conf_read.get_excel_sheet()
        # 使用excel工具类，获取数据list
        self._data_excel = ExcelUtil(excel_name, excel_sheet)
        self._data_list = self._data_excel.data_list()

    # 获取所有测试用例
    def get_all_data(self):       
        return self._data_list

    # 获取需要执行的测试用例
    def get_run_data(self):
        # 列：是否运行，Y
        test_data = []
        for data in self._data_list:
            # str.upper()：把所有字符中的小写字母转换成大写字母
            # str.lower()：把所有字符中的大写字母转换成小写字母
            if str(data[data_key.case_is_run]).lower() == 'y':
                # print(data)
                # 保存要执行的数据，放到新的列表
                test_data.append(data)
        return test_data

    # 获取前置测试用例
    def get_pre_data(self, pre, case_id):
        all_data = self.get_all_data()
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
    testdata = run_data().get_run_data()
    # print(testdata[0]['status_code'])
    # print(type(testdata[0]['status_code']))
    # print(testdata[0]['请求参数'])
    # print(type(testdata[0]['请求参数']))
    # print(json.loads(testdata[0]['请求参数']))
    # print(testdata[0]['headers'])
    # print(testdata[0]['cookies'])
    # print(testdata[1][data_key.case_db_verify])
    # print(type(testdata[2][data_key.case_db_verify]))
    alldata = run_data().get_all_data()
    print(testdata[0]['前置条件'].split(','))
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