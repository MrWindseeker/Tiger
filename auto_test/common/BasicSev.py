import sys, os, json, re, subprocess, shutil, datetime
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Conf
from common import Base
from utils.LogUtil import LogUtil
from utils.MysqlUtil import MysqlUtil
from utils.AssertUtil import AssertUtil
from utils.EmailUtil import EmailUtil
from utils.ZipUtil import ZipUtil

# 初始化配置文件
conf_read = Conf.ConfigYaml()
# 初始化断言
assert_util = AssertUtil()
# 初始化压缩
compress_util = ZipUtil()
# 图片格式
img_type_list = ['.jpg', '.jpeg', '.png', '.bmp']
# 音频视频格式
aud_type_list = ['.mp3', '.mp4']
# 压缩文件格式
zip_type_list = ['.zip', '.rar']
# allure报告相关信息
allure_path = Conf.get_allure_path()
allure_open = Conf.get_allure_open()
allure_output = Conf.get_output_path()


# 当前时间
cur_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

def init_mysql(msdb_env):
    """ 初始化mysql对象 """
    # 读取配置,初始化数据库信息
    msdb_info = conf_read.get_db_conf_info(msdb_env)
    # host, user, passwd, database, port = 3306, charset = 'utf8'
    host = msdb_info['db_host']
    user = msdb_info['db_user']
    passwd = msdb_info['db_passwd']
    database = msdb_info['db_database']
    port = msdb_info['db_port']
    charset = msdb_info['db_charset']

    # 初始化mysql对象
    mysql = MysqlUtil(host, user, passwd, database, port, charset)
    # print(mysql)
    return mysql

def assert_db(db_name, result, db_verify):
    """ 数据库验证 """
    # 数据库验证
    mysql = init_mysql(db_name)
    res_sql = mysql.query_one(db_verify)
    db_verify_list = list(res_sql.keys())
    for line in db_verify_list:
        test_res_line = result[line]
        res_sql_line = res_sql[line]
        assert_util.assert_body(test_res_line, res_sql_line)

def allure_report(report_path, report_html_path):
    """ 生产allure报告 """
    # 生产allure报告
    allure_cmd = "allure generate {} -o {} --clean".format(report_path, report_html_path)
    try:
        subprocess.run(allure_cmd, shell=True)
    except:
        raise Exception('执行用例失败，请核查！')

def open_report(report_html_path):
    """ 打开allure报告 """
    open_cmd = "allure open {}".format(report_html_path)
    try:
        subprocess.run(open_cmd, shell=True)
    except:
        raise Exception('打开测试报告失败，请核查！')
    
def compress_files(output_path = allure_output, output_name = '接口测试报告', file_path = allure_open, folder_path = allure_path):
    """ 压缩文件或文件夹 """
    compress_util.zip_files(output_path, output_name, file_path = file_path, folder_path =folder_path)

def send_email(subject, text_cont = None, attach_file = None, html_cont = None, html_img = None):
    """ 发送邮件 """
    email_info = conf_read.get_email_info()
    email_host = email_info['email_host']
    sender = email_info['sender']
    auth_code = email_info['auth_code']
    to_recv = email_info['to_recv']
    cc_recv = email_info['cc_recv']
    subject = subject

    email = EmailUtil(email_host, sender, auth_code, to_recv, cc_recv, subject, text_cont = text_cont, attach_file = attach_file, html_cont = html_cont, html_img = html_img)

    # 添加text或html正文
    if html_cont:
        email.add_html_cont()
    elif text_cont:
        email.add_text_cont()

    # 添加附件
    if attach_file:
        for file_path in attach_file:
            if Base.path_to_filetype(file_path) == '.txt':
                email.add_text_attach(file_path)
            elif Base.path_to_filetype(file_path) == '.html':
                email.add_html_attach(file_path)
            elif Base.path_to_filetype(file_path) in zip_type_list:
                email.add_zip_attach(file_path)
            elif Base.path_to_filetype(file_path) in img_type_list:
                email.add_img_attach(file_path)
            elif Base.path_to_filetype(file_path) in aud_type_list:
                email.add_aud_attach(file_path)
            else:
                raise Exception('未找到附件信息，请检查.')

    # 设置邮件信息
    email.set_email()
    email.send_email()


if __name__ == '__main__':
    subject = 'email_test'
    text_cont = 'hello everyone'
    html_cont = '''
    <p>大连森林动物园官网地址：</p>
    <p><a href = 'https://www.dlzoo.com/'>点击进入</a></p>
    <p>Jinhu's Photo</p>
    <p>------------------------------------------------</p>
    <p><img src = 'cid:image_0'></p>
    <p>------------------------------------------------</p>
    <p><img src = 'cid:image_1'></p>
    '''
    html_img = ['/Users/windseeker/Desktop/文件/JH.jpg', '/Users/windseeker/Desktop/文件/SH.png']
    # attach_files = ['D:/Windseeker/Desktop/test/dolanaar.txt','D:/Windseeker/Desktop/test/test.html','D:/Windseeker/Desktop/test/niefeng.png','D:/Windseeker/Desktop/test/WeChat_20230212194705.mp4',Base.find_latest_file(allure_output)]
    attach_files = ['/Users/windseeker/Desktop/文件/Windseeker.txt','/Users/windseeker/Desktop/文件/test.html','/Users/windseeker/Desktop/文件/niefeng.png','/Users/windseeker/Desktop/文件/WeChat_20230212194705.mp4']

    send_email(subject, html_cont = html_cont, html_img = html_img, attach_file = attach_files)
    # send_email(subject, html_cont = html_cont, html_img = html_img)