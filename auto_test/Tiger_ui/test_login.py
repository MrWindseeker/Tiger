import json, os, sys, time, traceback, pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.common_ui import *
from common import ExcelData, ExcelConf, Base
from Tiger_api.admin_sys import admin_sys

test_admin = admin_sys()

# 初始化ExcelConf
data_key = ExcelConf.ExcelConf()

# 初始化测试用户
init_data = ExcelData.run_data()
user_data = init_data.get_all_data()


def test_typec(get_log, browser):
    user_c = Base.find_dict(user_data, data_key.test_scene, 'C')
    try:
        # 先查询该账号是否有项目
        user = user_c[0][data_key.test_username]
        pwd = user_c[0][data_key.test_password]
        json_login = {'username': user, 'password': pwd, 'captchaVerification': ''}
        login_result = test_admin.login(json_login)
        acs_token = login_result['body']['data']['accessToken']

        project_list = query_project(user, pwd, 'C')
        get_log.info(user+'用户的项目：'+str(project_list['data']))
        # 先判断该用户typec的项目数量
        # 如果没有项目，则通过接口新增一个
        engName = ''
        if len(project_list['data']) <= 0:
            bol = add_porject(user, pwd, 'C')
            if bol == False:
                get_log.error('该用户C类型项目添加失败')
                assert False
            else:
                engName = bol
        else:
            for pl in project_list['data']:
                status = chaxun(pl['engCode'], 'C', acs_token)
                if status == 'O':
                    engName = str(pl['engCode'])+'-'+str(pl['engName'])+' - '+str(pl['clientName'])
                    break
        if engName == '':
            get_log.error('项目名未获取到')
            assert False
        get_log.info('engagement元素选择的项目名为：'+engName)
        browser.get(r"https://bcp-preuat.ey.com.cn/login?redirect=%2Ftim%2F")
        # 用户名输入框
        user_input = show_wait(browser, 'xpath', ui.get('login', 'user_input'), 5, 0.5)
        # 密码输入框
        pwd_input = show_wait(browser, 'xpath', ui.get('login', 'pwd_input'), 5, 0.5)
        user_input.clear()
        user_input.send_keys(user)
        pwd_input.clear()
        pwd_input.send_keys('123456')
        # 登陆按钮
        show_wait(browser, 'xpath', ui.get('login', 'loging_btn'), 5, 0.5).click()
        time.sleep(1)
        # 侧边栏快捷菜单的工时列表按钮
        show_wait(browser, 'xpath', ui.get('home_page', 'Current_Week_Timesheet'), 5, 0.5).click()
        time.sleep(2)
        # 先清空工时表单
        select_all = browser.find_element(By.XPATH, ui.get('timesheet', 'select_all'))
        # 此处的元素无法直接点击，只能使用js的方式模拟点击
        browser.execute_script("arguments[0].click();", select_all)
        show_wait(browser, 'xpath', ui.get('timesheet', 'delete_project'), 5, 0.5).click()
        # 添加项目按钮
        show_wait(browser, 'xpath', ui.get('timesheet', 'add_project'), 5, 0.5).click()
        # # 先判断当前工时是否已填写,如果有工时项目了，则点击新增
        # project_code = show_wait(browser, 'xpath', ui.get('timesheet', 'last_tr_engcode')+'/td[5]', 5, 0.5).text
        # if project_code != '':
        #     # 添加项目按钮
        #     show_wait(browser, 'xpath', ui.get('timesheet', 'add_project'), 5, 0.5).click()
        # 点击最后一行的 look up 按钮
        show_wait(browser, 'xpath',
                  ui.get('timesheet', 'last_tr_engcode')+'/td[2]/div/i',
                  5, 0.5).click()

        # 展开Type选择框
        show_wait(browser, 'xpath', ui.get('Look Up', 'Type_input'), 5, 0.5).click()
        # 选择Type框内的元素
        show_wait(browser, 'xpath', '/html/body/div[3]/div[1]/div[1]/ul/li[1]', 5, 0.5).click()

        # 展开Engagement选择框
        # show_wait(browser, 'xpath',
        #           '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[2]/div/div[2]/form/div[3]/div/div/div/div/input',
        #           5, 0.5).click()
        show_wait(browser, 'xpath', ui.get('Look Up', 'Engagement_input'), 5, 0.5).click()
        # 选择Engagement框内的元素
        # '/html/body/div[4]/div[1]/div[1]/ul/li[1]'
        show_wait(browser, 'xpath', f"//*[text()='{engName}']", 5, 0.5).click()
        time.sleep(1)
        activity = show_wait(browser, 'xpath', '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[2]/div/div[2]/form/div[4]/div/div/div/div/input', 5, 0.5).get_attribute('value')
        if activity is None:
            get_log.error('Activity为空')
            assert False
        get_log.info(f'activity：{activity}')
        # loc1选择框
        # show_wait(browser, 'xpath', '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[2]/div/div[2]/form/div[6]/div/div/div/div/input', 5, 0.5).click()
        show_wait(browser, 'xpath', ui.get('Look Up', 'Loc1_input'), 5, 0.5).click()
        # 选择第一个loc1框内的元素
        show_wait(browser, 'xpath', '/html/body/div[5]/div[1]/div[1]/ul/li[1]', 5, 0.5).click()
        # loc2选择框
        # show_wait(browser, 'xpath', '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[2]/div/div[2]/form/div[7]/div/div/div/div/input', 5, 0.5).click()
        show_wait(browser, 'xpath', ui.get('Look Up', 'Loc2_input'), 5, 0.5).click()
        # 选择第一个loc2框内的元素
        show_wait(browser, 'xpath', '/html/body/div[6]/div[1]/div[1]/ul/li[1]', 5, 0.5).click()
        # 提交
        show_wait(browser, 'xpath',
                  '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[2]/div/div[2]/form/div[8]/button',
                  5, 0.5).click()
        time.sleep(2)
        # 获取第一天工时元素属性是否置灰
        '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[1]/div/div/form/div/div[3]/table/tbody/tr[last()-0]/td[2]/div/i'
        element1 = show_wait(browser, 'xpath',
                            '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[1]/div/div/form/div/div[3]/table/tbody/tr[last()-0]/td[10]',
                            5, 0.5)
        class_name1 = element1.get_attribute('class')
        if str(class_name1).find('weekendClass') == -1:
            show_wait(browser, 'xpath', '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[1]/div/div/form/div/div[3]/table/tbody/tr[last()-0]/td[10]/div/div/div/div/input', 5, 0.5).send_keys(8)
        # 获取第二天工时元素属性是否置灰
        element2 = show_wait(browser, 'xpath',
                            '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[1]/div/div/form/div/div[3]/table/tbody/tr[last()-0]/td[11]',
                            5, 0.5)
        class_name2 = element2.get_attribute('class')
        if str(class_name2).find('weekendClass') == -1:
            show_wait(browser, 'xpath',
                      '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[1]/div/div/form/div/div[3]/table/tbody/tr[last()-0]/td[11]/div/div/div/div/input',
                      5, 0.5).send_keys(8)
        # 获取第三天工时元素属性是否置灰
        element3 = show_wait(browser, 'xpath',
                            '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[1]/div/div/form/div/div[3]/table/tbody/tr[last()-0]/td[12]',
                            5, 0.5)
        class_name3 = element3.get_attribute('class')
        if str(class_name3).find('weekendClass') == -1:
            show_wait(browser, 'xpath',
                      '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[1]/div/div/form/div/div[3]/table/tbody/tr[last()-0]/td[12]/div/div/div/div/input',
                      5, 0.5).send_keys(8)
        # 获取第四天工时元素属性是否置灰
        element4 = show_wait(browser, 'xpath',
                            '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[1]/div/div/form/div/div[3]/table/tbody/tr[last()-0]/td[13]',
                            5, 0.5)
        class_name4 = element4.get_attribute('class')
        if str(class_name4).find('weekendClass') == -1:
            show_wait(browser, 'xpath',
                      '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[1]/div/div/form/div/div[3]/table/tbody/tr[last()-0]/td[13]/div/div/div/div/input',
                      5, 0.5).send_keys(8)
        # 获取第五天工时元素属性是否置灰
        element5 = show_wait(browser, 'xpath',
                            '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[1]/div/div/form/div/div[3]/table/tbody/tr[last()-0]/td[14]',
                            5, 0.5)
        class_name5 = element5.get_attribute('class')
        if str(class_name5).find('weekendClass') == -1:
            show_wait(browser, 'xpath',
                      '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[1]/div/div/form/div/div[3]/table/tbody/tr[last()-0]/td[14]/div/div/div/div/input',
                      5, 0.5).send_keys(8)
        # 获取第六天工时元素属性是否置灰
        element6 = show_wait(browser, 'xpath',
                             '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[1]/div/div/form/div/div[3]/table/tbody/tr[last()-0]/td[15]',
                             5, 0.5)
        class_name6 = element6.get_attribute('class')
        if str(class_name6).find('weekendClass') == -1:
            show_wait(browser, 'xpath',
                      '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[1]/div/div/form/div/div[3]/table/tbody/tr[last()-0]/td[15]/div/div/div/div/input',
                      5, 0.5).send_keys(8)
        # 获取第七天工时元素属性是否置灰
        element7 = show_wait(browser, 'xpath',
                             '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[1]/div/div/form/div/div[3]/table/tbody/tr[last()-0]/td[16]',
                             5, 0.5)
        class_name7 = element7.get_attribute('class')
        if str(class_name7).find('weekendClass') == -1:
            show_wait(browser, 'xpath',
                      '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[1]/div/div/form/div/div[3]/table/tbody/tr[last()-0]/td[16]/div/div/div/div/input',
                      5, 0.5).send_keys(8)
        # 提交工时单
        show_wait(browser, 'xpath', '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[1]/div/span[2]/button[4]', 5, 0.5).click()
        time.sleep(1)
        # 确认提交
        show_wait(browser, 'xpath', '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[6]/div/div[3]/span/button[1]', 5, 0.5).click()
        # 获取提交后的文本信息
        element_tj = show_wait(browser, 'xpath', ui.get('timesheet', 'submit_message'), 5, 0.5).text
        get_log.info('提交后的文本信息：'+element_tj)
        assert str(element_tj) == 'Submit Successfully'
    except Exception as e:
        get_log.error(f'用例执行过程发生异常，异常类型：{e.__class__.__name__}'+traceback.format_exc()+'------------\n')
        assert False

def test_typep(get_log, browser):
    try:
        # 先查询该账号是否有项目
        user = conf.get('user', 'tim_user')
        pwd = conf.get('user', 'tim_pwd')
        token = login_token(user, pwd)
        project_list = query_project(user, pwd, 'P')
        get_log.info(user + '用户的项目：' + str(project_list['data']))
        # 先判断该用户typec的项目数量
        # 如果没有项目，则通过接口新增一个
        engName = ''
        if len(project_list['data']) <= 0:
            bol = add_porject(user, pwd, 'P')
            if bol == False:
                get_log.error('该用户P类型项目添加失败')
                assert False
            else:
                engName = bol
        else:
            for pl in project_list['data']:
                status = chaxun(pl['engCode'], 'P', token)
                if status == 'O':
                    engName = str(pl['engCode']) + '-' + str(pl['engName']) + ' - ' + str(pl['clientName'])
                    break
        if engName == '':
            get_log.error('项目名未获取到')
            assert False
        get_log.info('engagement元素选择的项目名为：' + engName)
        browser.get(r"https://bcp-preuat.ey.com.cn/login?redirect=%2Ftim%2F")
        user_input = show_wait(browser, 'xpath',
                         '/html/body/div/div/div[1]/div[2]/div/div[2]/form/div[2]/div[1]/div/div/input', 5, 0.5)
        pwd_input = show_wait(browser, 'xpath',
                        '/html/body/div/div/div[1]/div[2]/div/div[2]/form/div[2]/div[2]/div/div/input', 5, 0.5)
        user_input.clear()
        user_input.send_keys(user)
        pwd_input.clear()
        pwd_input.send_keys('123456')
        # 登陆按钮
        show_wait(browser, 'xpath', '/html/body/div/div/div[1]/div[2]/div/div[2]/form/div[3]/div/button', 5,
                  0.5).click()
        # 侧边栏快捷菜单的工时列表按钮
        show_wait(browser, 'xpath',
                  '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div[2]/div[2]/i', 5,
                  0.5).click()
        time.sleep(2)
        # 先判断当前工时是否已填写,如果有工时项目了，则点击新增
        project_code = show_wait(browser, 'xpath',
                                 '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[1]/div/div/form/div/div[3]/table/tbody/tr[last()-0]/td[5]',
                                 5, 0.5).text
        if project_code != '':
            show_wait(browser, 'xpath',
                      '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[1]/div/div/div/div[2]/span[1]',
                      5, 0.5).click()
        # 点击最后一行的 look up 按钮
        show_wait(browser, 'xpath',
                  '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[1]/div/div/form/div/div[3]/table/tbody/tr[last()-0]/td[2]/div/i',
                  5, 0.5).click()

        # 展开Type选择框
        show_wait(browser, 'xpath',
                  '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[2]/div/div[2]/form/div[2]/div/div/div/div/input',
                  5, 0.5).click()
        # 选择Type框内的元素
        show_wait(browser, 'xpath', '/html/body/div[3]/div[1]/div[1]/ul/li[2]', 5, 0.5).click()

        # 展开Engagement选择框
        show_wait(browser, 'xpath',
                  '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[2]/div/div[2]/form/div[3]/div/div/div/div/input',
                  5, 0.5).click()
        # 选择Engagement框内的元素
        show_wait(browser, 'xpath', f"//*[text()='{engName}']", 5, 0.5).click()
        # show_wait(browser, 'xpath', '/html/body/div[4]/div[1]/div[1]/ul/li[1]', 5, 0.5).click()
        time.sleep(1)
        activity = show_wait(browser, 'xpath', '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[2]/div/div[2]/form/div[4]/div/div/div/div/input', 5, 0.5).get_attribute('value')
        if activity is None:
            get_log.error('Activity为空')
            assert False
        get_log.info(f'activity：{activity}')
        # loc1选择框
        show_wait(browser, 'xpath',
                  '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[2]/div/div[2]/form/div[6]/div/div/div/div/input',
                  5, 0.5).click()
        # 选择第一个loc1框内的元素
        show_wait(browser, 'xpath', '/html/body/div[5]/div[1]/div[1]/ul/li[1]', 5, 0.5).click()
        # loc2选择框
        show_wait(browser, 'xpath',
                  '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[2]/div/div[2]/form/div[7]/div/div/div/div/input',
                  5, 0.5).click()
        time.sleep(10)
        # 选择第一个loc2框内的元素
        show_wait(browser, 'xpath', '/html/body/div[6]/div[1]/div[1]/ul/li[1]', 5, 0.5).click()
        # 提交
        show_wait(browser, 'xpath',
                  '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[2]/div/div[2]/form/div[8]/button',
                  5, 0.5).click()
        time.sleep(2)
        # 获取第一天工时元素属性是否置灰
        '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[1]/div/div/form/div/div[3]/table/tbody/tr[last()-0]/td[2]/div/i'
        element1 = show_wait(browser, 'xpath',
                             '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[1]/div/div/form/div/div[3]/table/tbody/tr[last()-0]/td[10]',
                             5, 0.5)
        class_name1 = element1.get_attribute('class')
        if str(class_name1).find('weekendClass') == -1:
            show_wait(browser, 'xpath',
                      '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[1]/div/div/form/div/div[3]/table/tbody/tr[last()-0]/td[10]/div/div/div/div/input',
                      5, 0.5).send_keys(8)
        # 获取第二天工时元素属性是否置灰
        element2 = show_wait(browser, 'xpath',
                             '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[1]/div/div/form/div/div[3]/table/tbody/tr[last()-0]/td[11]',
                             5, 0.5)
        class_name2 = element2.get_attribute('class')
        if str(class_name2).find('weekendClass') == -1:
            show_wait(browser, 'xpath',
                      '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[1]/div/div/form/div/div[3]/table/tbody/tr[last()-0]/td[11]/div/div/div/div/input',
                      5, 0.5).send_keys(8)
        # 获取第三天工时元素属性是否置灰
        element3 = show_wait(browser, 'xpath',
                             '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[1]/div/div/form/div/div[3]/table/tbody/tr[last()-0]/td[12]',
                             5, 0.5)
        class_name3 = element3.get_attribute('class')
        if str(class_name3).find('weekendClass') == -1:
            show_wait(browser, 'xpath',
                      '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[1]/div/div/form/div/div[3]/table/tbody/tr[last()-0]/td[12]/div/div/div/div/input',
                      5, 0.5).send_keys(8)
        # 获取第四天工时元素属性是否置灰
        element4 = show_wait(browser, 'xpath',
                             '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[1]/div/div/form/div/div[3]/table/tbody/tr[last()-0]/td[13]',
                             5, 0.5)
        class_name4 = element4.get_attribute('class')
        if str(class_name4).find('weekendClass') == -1:
            show_wait(browser, 'xpath',
                      '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[1]/div/div/form/div/div[3]/table/tbody/tr[last()-0]/td[13]/div/div/div/div/input',
                      5, 0.5).send_keys(8)
        # 获取第五天工时元素属性是否置灰
        element5 = show_wait(browser, 'xpath',
                             '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[1]/div/div/form/div/div[3]/table/tbody/tr[last()-0]/td[14]',
                             5, 0.5)
        class_name5 = element5.get_attribute('class')
        if str(class_name5).find('weekendClass') == -1:
            show_wait(browser, 'xpath',
                      '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[1]/div/div/form/div/div[3]/table/tbody/tr[last()-0]/td[14]/div/div/div/div/input',
                      5, 0.5).send_keys(8)
        # 获取第六天工时元素属性是否置灰
        element6 = show_wait(browser, 'xpath',
                             '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[1]/div/div/form/div/div[3]/table/tbody/tr[last()-0]/td[15]',
                             5, 0.5)
        class_name6 = element6.get_attribute('class')
        if str(class_name6).find('weekendClass') == -1:
            show_wait(browser, 'xpath',
                      '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[1]/div/div/form/div/div[3]/table/tbody/tr[last()-0]/td[15]/div/div/div/div/input',
                      5, 0.5).send_keys(8)
        # 获取第七天工时元素属性是否置灰
        element7 = show_wait(browser, 'xpath',
                             '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[1]/div/div/form/div/div[3]/table/tbody/tr[last()-0]/td[16]',
                             5, 0.5)
        class_name7 = element7.get_attribute('class')
        if str(class_name7).find('weekendClass') == -1:
            show_wait(browser, 'xpath',
                      '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[1]/div/div/form/div/div[3]/table/tbody/tr[last()-0]/td[16]/div/div/div/div/input',
                      5, 0.5).send_keys(8)
        # 提交工时单
        show_wait(browser, 'xpath', '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[1]/div/span[2]/button[4]', 5, 0.5).click()
        # 确认提交
        show_wait(browser, 'xpath', '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[6]/div/div[3]/span/button[1]', 5, 0.5).click()
        time.sleep(2)
        # 获取提交成功的文本信息
        element_tj = show_wait(browser, 'xpath', '/html/body/div[4]/p', 5, 0.5).text
        get_log.info(element_tj)
        assert str(element_tj) == 'Submit Successfully'
    except Exception as e:
        get_log.error(f'用例执行过程发生异常，异常类型：{e.__class__.__name__}'+traceback.format_exc()+'------------\n')
        assert False
