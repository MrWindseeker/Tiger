import sys, os, json, pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import Base, BasicSev, ExcelConf, ExcelData
from config import Conf
from utils.ReqsUtil import ReqsUtil
from utils.AssertUtil import AssertUtil
from utils.LogUtil import sys_log
from config.Tiger_Conf import Tiger_ConfigYaml


# 初始化测试用例
init_data = ExcelData.run_data()
data_list = init_data.get_run_data()
data_key = ExcelConf.ExcelConf()

# 初始化接口请求
req = ReqsUtil()

# 初始化断言
assert_data = AssertUtil()

# 初始化域名orIP
preuat_url = Tiger_ConfigYaml().get_preuat_url()

# 初始化日志
case_log = sys_log('run_case')

class TestCase:
    # case_log.info(type(data_list))
    @pytest.mark.parametrize('test_case', data_list)
    def test_run(self, test_case):
        # 用例编号
        case_id = test_case[data_key.case_id]
        # 系统
        case_sys = test_case[data_key.case_sys]
        # 模块
        case_module = test_case[data_key.case_module]
        # 接口名称
        case_intf = test_case[data_key.case_intf]
        # 请求url
        case_url = test_case[data_key.case_url]
        # 前置条件
        case_prec = test_case[data_key.case_prec]
        # 请求类型
        case_method = test_case[data_key.case_method]
        # 请求参数类型
        case_params_type = test_case[data_key.case_params_type]
        # 请求参数
        case_params = test_case[data_key.case_params]
        # 预期结果
        case_expect = test_case[data_key.case_expect]
        # 实际结果
        case_actual = test_case[data_key.case_actual]
        # 是否运行
        case_is_run = test_case[data_key.case_is_run]
        # headers
        case_headers = test_case[data_key.case_headers]
        # cookies
        case_cookies = test_case[data_key.case_cookies]
        # status_code
        case_code = test_case[data_key.case_code]
        # 数据库验证
        case_db_verify = test_case[data_key.case_db_verify]        

        case_log.info('执行测试用例编号：{}。'.format(case_id))

        # 验证前置条件
        if case_prec:
            pass
        else:
            case_log.info('无前置测试用例。')

        if str(case_method).upper() == 'POST':
            if str(case_params_type).lower() == 'json':
                case_params = Base.json_parse(case_params)
                case_res = req.req_post(preuat_url + case_url, json = case_params, headers = case_headers)
            elif str(case_params_type).lower() == 'data':
                pass
        elif str(case_method).upper() == 'GET':
            case_res = req.req_get(preuat_url + case_url, headers = case_headers)
        
        # return case_res

        # 验证返回码
        assert_data.assert_code(case_res['code'], case_code)

                

if __name__ =='__main__':
    report_path = Conf.get_report_path() + os.sep + 'result'
    report_html_path = Conf.get_report_path() + os.sep + 'html'
    pytest.main(['--capture=tee-sys', 'D:/Python/Tiger/api_test/testdemo/t_case_demo.py'])
    BasicSev.allure_report(report_path, report_html_path)
    BasicSev.open_report(report_html_path)


