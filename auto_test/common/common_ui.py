import os, json, requests, xlrd, time, sys
import configparser
import subprocess
import urllib3
# import win32con, win32gui
# from PIL import Image
# from pyzbar.pyzbar import decode
import random,string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


base_path = os.path.dirname(os.path.dirname(__file__))  #当前项目基本路径
project_path = os.path.join(base_path, 'Tiger_ui')   #项目所在目录路径
print(project_path)
config_path = os.path.join(base_path, 'config')    #配置所在目录路径
# ui_path = os.path.join(base_path, 'ui_element')    #UI元素信息所在目录路径
log_path = os.path.join(base_path, 'logs')    #日志文件所在目录路径
report_path = os.path.join(base_path, 'report')    #报告所在目录路径
drivers_path = os.path.join(base_path, 'drivers')    #驱动所在目录路径
utils_path = os.path.join(base_path, 'util')    #公共模块所在目录路径
image_path = os.path.join(base_path, 'image')   #图片文件所在目录路径

# def read_excel(path):
#     '''
#     获取Excel内容（注：.xls格式）
#     :param path: 指定文件路径
#     :return: Excel内所有的sheet页对象，可通过row/col/cell_values()操作内容
#     '''
#     if os.path.exists(path) and os.path.isfile(path):
#         with xlrd.open_workbook(path) as f:
#             return f.sheets()
#     else:
#         print('路径不存在或不是文件')
#         return False
def read_data(path):
    '''
    读取数据文件内容
    :param path: 指定文件的路径
    :return: ConfigParser对象，通过get('key','key')获取值
    '''
    if os.path.exists(path) and os.path.isfile(path):
        data = configparser.ConfigParser()
        data.read(path,encoding='utf8')
        return data
    else:
        print('路径不存在或不是文件')
        return False


def is_chinese(str):
    '''
    校验字符串是否包含中文字符，找到中文返回True，反之False
    :param str:校验的字符串
    :return: True,False
    '''
    for i in str:
        if u'\u4e00' <= i <= u'\u9fff':
            return True
    return False


# 获取配置信息
conf = read_data(config_path+'/configuration.conf')
ui = read_data(config_path+'/tim_elem.conf')

print(ui.get('Look Up', 'Time_Type_input'))

def get_file(path):
    '''
    获取指定目录路径的文件列表
    :param path: 指定目录路径
    :return: 文件列表
    '''
    if os.path.exists(path) and os.path.isdir(path):
        return os.listdir(path)
    else:
        print('路径不存在或不是目录')
        return False


def select_file(file_path, file_name):
    '''
    查找文件目录下是否有该文件（忽略后缀的形式）
    :param file_path:文件目录
    :param file_name:文件名，不带后缀，只查找是否有该文件名
    :return:True or Fales
    '''
    files = os.listdir(file_path)
    for ff in files:
        portion = ff.split('.')
        if portion[0] == file_name:
            return True
    return False


def login_token(name, pwd):
    '''
    获取登录账户token
    :param name: 登录账号
    :param pwd: 登录密码
    :return: token
    '''
    url = "https://bcp-preuat.ey.com.cn/api/admin-api/system/auth/login"
    headers = {"Content-Type": "application/json;charset=UTF-8"}
    josn = {
              "username": name,
              "password": pwd,
              "captchaVerification": ""
            }
    requests.packages.urllib3.disable_warnings()
    rp = requests.post(url=url, json=josn, headers=headers, verify=False).text
    if json.loads(rp)["code"] == 0:
        return json.loads(rp)["data"]["accessToken"]
    else:
        print('获取toekn失败')
        return False



def login_user(browser, user, pwd):
    '''
    :param browser: 浏览器驱动对象
    :param user: 登录用户名
    :param pwd: 登录密码    '''
    # browser.find_element_by_xpath('//*[@id="app"]/div/form/div[2]/div/div[1]/input').clear()
    # browser.find_element_by_xpath('//*[@id="app"]/div/form/div[2]/div/div[1]/input').send_keys(user)
    # browser.find_element_by_xpath('//*[@id="app"]/div/form/div[3]/div/div/input').clear()
    # browser.find_element_by_xpath('//*[@id="app"]/div/form/div[3]/div/div/input').send_keys(pwd)
    # browser.find_element_by_class_name('el-checkbox__input').click()
    # browser.find_element_by_xpath('//*[@id="app"]/div/form/button/span').click()
    show_wait(browser, *('xpath', '//*[@id="app"]/div/form/div[2]/div/div[1]/input'), 10, 0.5).clear()
    show_wait(browser, *('xpath', '//*[@id="app"]/div/form/div[2]/div/div[1]/input'), 10, 0.5).send_keys(user)
    show_wait(browser, *('xpath', '//*[@id="app"]/div/form/div[3]/div/div/input'), 10, 0.5).clear()
    show_wait(browser, *('xpath', '//*[@id="app"]/div/form/div[3]/div/div/input'), 10, 0.5).send_keys(pwd)
    show_wait(browser,*('xpath','//*[@id="app"]/div/form/button/span'),10,0.5).click()
    time.sleep(2)


def find_element(browser, by, value):
    '''
    #查找元素是否存在，找到True，没找到False
    :param browser: 浏览器驱动对象
    :param by: 定位方式
    :param value: 元素路径
    :return: 元素对象
    '''
    element = None
    try:
        if by == 'id':
            element = browser.find_element_by_id(value)
            return element
        if by == 'xpath':
            element = browser.find_element_by_xpath(value)
            return element
        if by == 'name':
            element = browser.find_element_by_name(value)
            return element
        if by == 'class':
            element = browser.find_element_by_class_name(value)
            return element
    except:
        #未查找到元素
        return element


# def upload_file(filepath, browser_type="chrome"):
#     '''
#     用于非Input标签的文件上传
#     :param filepath: 需上传文件的本地路径
#     :param browser_type: 浏览器类型
#     :return: 无
#     '''
#     if browser_type.lower() == "chrome":
#         title = "打开"
#     elif browser_type.lower() == "firefox":
#         title = "文件上传"
#     elif browser_type.lower() == "ie":
#         title = "选择要加载的文件"
#     elif browser_type.lower() == "edge":
#         title = "打开"
#     # winspy工具定位到文件路径输入框的Class属性路径为：Edit》combox》comboBoxEx32》#32770：
#     # 一级窗口"#32770"
#     dialog = win32gui.FindWindow("#32770", title)
#     ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
#     comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)
#     # 编辑按钮
#     edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)
#     # 打开按钮
#     button = win32gui.FindWindowEx(dialog, 0, 'Button', "打开(&O)")
#     # 输入文件的绝对路径，点击“打开”按钮
#     win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filepath)  # 发送文件路径
#     win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮


# def decode_rqcode(paths):
#     '''
#     解析图片二维码
#     :param paths: 图片路径，需要跟文件名
#     :return: 解析数据    '''
#     if not os.path.exists(paths):
#         raise FileExistsError(paths)
#     mg = Image.open(paths)
#     barcodes = decode(mg)
#     return barcodes


def random_name(num):
    '''
    获取随机字母组成的字符串
    :param num: 字符串长度
    :return:组成的字符串    '''
    username = ''
    for i in range(num):
        username = username+random.choice(string.ascii_lowercase)
    return username


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

# 查询用户已添加的项目数量
def query_project(user, pwd, type):
    token = login_token(user, pwd)
    url1 = 'https://bcp-preuat.ey.com.cn/api/admin-api/timesheet/info/eng/my-eng?engType=P'
    url2 = 'https://bcp-preuat.ey.com.cn/api/admin-api/timesheet/info/eng/my-eng?engType=C'
    header1 = {"authorization": f"Bearer {token}"}
    if type == 'C':
        project_list = json.loads(requests.get(url=url2, headers=header1, verify=False).text)
        return project_list
    if type == 'P':
        project_list = json.loads(requests.get(url=url1, headers=header1, verify=False).text)
        return project_list
    else:
        print('查询条件异常')
        return False



# 查询该用户可添加的项目
def query_project_num(user, pwd):
    token = login_token(user, pwd)
    url1 = 'https://bcp-preuat.ey.com.cn/api/admin-api/timesheet/info/eng/eng-list'
    header1 = {"authorization": f"Bearer {token}", "content-type": "application/json;charset=UTF-8"}
    js = {
          "engagementType": "",
          "role": "",
          "managerialCntryOrLoc": "",
          "engagementCode": None,
          "engagementName": None,
          "clientCode": None,
          "clientName": None,
          "employeeName": None,
          "employeeGPN": None,
          "businessUnit": "",
          "managementUnit": "",
          "subManagementUnit": "",
          "pageNo": 1,
          "pageSize": 100
        }
    rq1 = requests.post(url=url1, headers=header1, json=js, verify=False).text
    # 项目list
    return rq1

# 添加一个项目
def add_porject(user, pwd, cntry):
    '''
    :param user: 用户名
    :param pwd: 密码
    :param cntry: 添加的项目类型，typep-P，typec-C
    :return:
    '''
    token = login_token(user, pwd)
    response = json.loads(query_project_num(user, pwd))
    if len(response["data"]["list"]) != 0:
        for rs in response["data"]["list"]:
            if rs["isAdd"] == False and rs['engType'] == cntry:
                status = chaxun(rs['engCode'], rs['engType'], token)
                engName = str(rs['engCode'])+'-'+str(rs['engName'])+' - '+str(rs['clientName'])
                if status != 'O':
                    continue
                url = "https://bcp-preuat.ey.com.cn/api/admin-api/timesheet/info/eng/create"
                header = {"authorization": f"Bearer {token}", "content-type": "application/json;charset=UTF-8"}
                data = {
                    "clientCode": rs["clientCode"],
                    "clientId": rs["clientId"],
                    "clientName": rs["clientName"],
                    "cntry": rs["cntry"],
                    "engCode": rs["engCode"],
                    "engName": rs["engName"],
                    "engType": rs["engType"],
                    "description": rs["description"],
                    "status": rs["status"]
                }
                rps = requests.post(url=url, json= data, headers=header, verify=False).text
                print(user+'该用户添加了'+str(rs['engCode'])+' - '+str(rs['engName'])+'项目')
                return engName
        return False
    else:
        return False
def allure_report(result_path, report_path):
    allure_cmd = "allure generate {} -o {} --clean".format(result_path, report_path)
    subprocess.run(allure_cmd, shell=True)

def oppen_allure(report_path):
    open_cmd = "allure open {}".format(report_path)
    subprocess.run(open_cmd, shell=True)


# get_log.info(user+'用户的项目：'+str(project_list[0]))
# 先判断该用户typec的项目数量
# 如果没有项目，则通过接口新增一个
# if len(project_list[1]) <= 0:
#     bol = add_porject(user, pwd, 'P')
#     if bol == False:
#         # get_log.error('该用户项目添加失败')
#         print('失败')
#     else:
#         print('添加成功')

# 查询项目状态
def chaxun(engCode, engType, token):
    # engcode = rs['engCode']
    # engType = rs['engType']
    url = f'https://bcp-preuat.ey.com.cn/api/admin-api/timesheet/info/eng/get-code-status?engCode={engCode}&engType={engType}'
    header = {"authorization": f"Bearer {token}"}
    rps = json.loads(requests.get(url=url, headers=header).text)
    status = rps['data']['status']
    return status
#
# user = 'Zhen.Feng.He'
# pwd = '123456'
# print(query_project(user, pwd, 'C'))

