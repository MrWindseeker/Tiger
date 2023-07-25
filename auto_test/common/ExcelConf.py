class ExcelConf:
    # 定义属性：用例编号	模块	接口名称	请求url	前置条件	请求类型	请求参数类型	请求参数	预期结果	实际结果	是否运行	headers	cookies	status_code	数据库验证
    case_id = '用例编号'
    case_sys = '系统'
    case_module = '模块'
    case_intf = '接口名称'
    case_url = '请求url'
    case_prec = '前置条件'
    case_method = '请求类型'
    case_params_type = '请求参数类型'
    case_params = '请求参数'
    case_data = '请求data'
    case_expect = '预期结果'
    case_actual = '实际结果'
    case_is_run = '是否运行'
    case_headers = 'headers'
    case_cookies = 'cookies'
    case_code = 'req_code'
    case_db_verify = '数据库验证'

    # 测试用户
    test_sys = '系统'
    test_username = '用户名'
    test_password = '密码'
    test_scene = '场景'

if __name__ == '__main__':
    # print(ExcelConf().case_is_run)
    print(ExcelConf().case_params)