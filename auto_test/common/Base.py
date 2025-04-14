import sys, os, json, re, subprocess, datetime
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.LogUtil import LogUtil
from config.Conf import ConfigYaml
from utils.MysqlUtil import MysqlUtil
from utils.AssertUtil import AssertUtil

# 初始化配置文件
conf_read = ConfigYaml()

pat_1 = '\${(.*)}\$'

# 初始化断言
assert_util = AssertUtil()

# 生成时间戳并保存在环境变量中
def generate_timestamp():
    """ 生成时间戳 """
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    os.environ["TIMESTAMP"] = timestamp

def contains_chinese(str):
    """ 判断字符串是否包含中文 """
    # 是否包含中文
    pattern = re.compile(r'[\u4e00-\u9fa5]')
    return bool(pattern.search(str))

def str_to_code(str):
    """ 字符串转unicode形式 """
    # 中文字符串转unicode形式
    return (str.encode('raw_unicode_escape')).decode()

def json_parse(json_data):
    """ 解析json数据 """
    # 转义 json
    return json.loads(json_data) if json_data else None

def res_find(data, pat_data = pat_1):
    """ 正则查询 """
    # 查询，公共方法
    # pattern = re.compile('\${(.*)}\$')
    pattern = re.compile(pat_data)
    re_res = pattern.findall(data)
    return re_res

def res_sub(data, rep_data, pat_data = pat_1):
    """ 正则替换 """
    # 替换，公共方法
    pattern = re.compile(pat_data)
    re_res = res_find(data, pat_data)
    if re_res:
        res_data = pattern.sub(rep_data, data)
        return res_data
    return re_res

def params_find(para):
    """ 参数替换 """
    # 验证是否包含
    if '${' in para:
        para = res_find(para)
    return para

def path_to_name(file_path):
    """ 文件路径截取文件名称 """
    # 文件路径截取文件名称
    if '/' in file_path:
        file_name = file_path.split('/')[-1]
    elif '\\' in file_path:
        file_name = file_path.split('\\')[-1]
    return file_name

def path_to_filetype(file_path):
    """ 文件路径截取文件格式 """
    # 文件路径截取文件格式
    file = os.path.splitext(file_path)
    file_type = file[1]
    return file_type

def find_dict(dict_list, target_key, target_value):
    """ 字典列表查找指定key和value """
    test_dict = []
    # 字典列表找到value对应数据
    for dict_data in dict_list:
        if dict_data[target_key].casefold() == target_value.casefold():
            test_dict.append(dict_data)
    return test_dict

def find_latest_file(dir_path):
    """ 查找目录下最新创建的文件 """
    # 获取目录下所有文件
    files = os.listdir(dir_path)
    # 初始化最新文件和最新创建时间
    latest_file = None
    latest_crt_time = 0
    # 遍历所有文件
    for file in files:
        file_path = os.path.join(dir_path, file)
        # 检查文件是否是文件
        if os.path.isfile(file_path):
            # 获取文件的创建时间
            crt_time = os.path.getctime(file_path)
            # 如果该文件的创建时间比最新创建时间要新，更新最新文件和最新创建时间
            if crt_time > latest_crt_time:
                latest_file = file_path
                latest_crt_time = crt_time
    # 最后latest_file变量将包含目录中创建时间最新的文件的路径
    return latest_file

# def init_mysql(msdb_env):
#     # 读取配置,初始化数据库信息
#     msdb_info = conf_read.get_db_conf_info(msdb_env)
#     # host, user, passwd, database, port = 3306, charset = 'utf8'
#     host = msdb_info['db_host']
#     user = msdb_info['db_user']
#     passwd = msdb_info['db_passwd']
#     database = msdb_info['db_database']
#     port = msdb_info['db_port']
#     charset = msdb_info['db_charset']

#     # 初始化mysql对象
#     mysql = MysqlUtil(host, user, passwd, database, port, charset)
#     # print(mysql)
#     return mysql

# def assert_db(db_name, result, db_verify):
#     # 数据库验证
#     mysql = init_mysql(db_name)
#     res_sql = mysql.fetchone(db_verify)
#     db_verify_list = list(res_sql.keys())
#     for line in db_verify_list:
#         test_res_line = result[line]
#         res_sql_line = res_sql[line]
#         assert_util.assert_body(test_res_line, res_sql_line)
    
# def allure_report(report_path, report_html_path):
#     # 生产allure报告
#     allure_cmd = "allure generate {} -o {} --clean".format(report_path, report_html_path)
#     open_cmd = "allure open {}".format(report_html_path)
#     try:
#         subprocess.run(allure_cmd, shell=True)
#     except:
#         raise Exception('执行用例失败，请核查！')
#     subprocess.run(open_cmd, shell=True)


if __name__ == '__main__':
    # init_db('db1')
    # str1 = '{"Authorization": "JWT ${token}$"}'
    # print(res_find(str1))
    # print(res_sub(str1, '123'))

    # headers = "{'Authorization': 'JWT ${token}$'}"
    # cookies = '{"Authorization": "JWT ${token}$"}'
    # headers = params_find(headers)
    # print(headers)

    file_path = ''
    # print(path_to_name(file_path))
    print(path_to_filetype(file_path))

    # send_email('test_email')