import json, os, sys, time, traceback, pytest
from selenium.webdriver import ActionChains
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import ExcelData, ExcelConf, Base, TimElem
from utils.ConfUtil import ConfUtil
from config.Tiger_Conf import *
from Tiger_ui.ui_api import *


conf_path = get_tim_elem_file()
ui = ConfUtil(conf_path)

# 初始化ExcelConf
data_key = ExcelConf.ExcelConf()

# 初始化tim_elem
tim_elem = TimElem.TimElem()

# 初始化测试用户
init_data = ExcelData.run_data()
user_data = init_data.get_all_data()

def test_typec(get_log, browser):
    '''
        项目类型 EngType = C
        Time Type为Regular Time 且 Type为Chargeable
    '''

    try:
        eng_type = 'C'
        user_c = Base.find_dict(user_data, data_key.test_scene, eng_type)
        user = user_c[0][data_key.test_username]
        pwd = str(int(user_c[0][data_key.test_password]))
        engName = seach_engName(user, pwd, eng_type)

        if engName == '':
            get_log.error('项目名未获取到')
            assert False
        get_log.info('engagement元素选择的项目名为：'+engName)
        browser.get(r"https://bcp-preuat.ey.com.cn/login?redirect=%2Ftim%2F")
        # 用户名输入框
        user_input = show_wait(browser, 'xpath', ui.get_data('login', 'user_input'), 5, 0.5)
        # 密码输入框
        pwd_input = show_wait(browser, 'xpath', ui.get_data('login', 'pwd_input'), 5, 0.5)
        user_input.clear()
        user_input.send_keys(user)
        pwd_input.clear()
        pwd_input.send_keys(pwd)
        # 登陆按钮
        show_wait(browser, 'xpath', ui.get_data('login', 'loging_btn'), 5, 0.5).click()
        time.sleep(1)
        # 侧边栏快捷菜单的工时列表按钮
        show_wait(browser, 'xpath', ui.get_data('home_page', 'Current_Week_Timesheet'), 5, 0.5).click()
        time.sleep(2)
        # 先清空工时表单
        select_all = browser.find_element(By.XPATH, ui.get_data('timesheet', 'select_all'))
        # 此处的元素无法直接点击，只能使用js的方式模拟点击
        browser.execute_script("arguments[0].click();", select_all)
        show_wait(browser, 'xpath', ui.get_data('timesheet', 'delete_project'), 5, 0.5).click()
        # 添加工时表单按钮
        show_wait(browser, 'xpath', ui.get_data('timesheet', 'add_project'), 5, 0.5).click()
        # 点击最后一行的 look up 按钮
        icons = browser.find_elements(By.XPATH, ui.get_data('timesheet', 'last_tr_engcode'))
        icons[len(icons)-1].click()
        # 展开Type选择框
        show_wait(browser, 'xpath', ui.get_data('Look Up', 'Type_input'), 5, 0.5).click()
        # 选择Type框内的元素
        show_wait(browser, 'xpath', '/html/body/div[3]/div[1]/div[1]/ul/li[1]', 5, 0.5).click()
        # 展开Engagement选择框
        show_wait(browser, 'xpath', ui.get_data('Look Up', 'Engagement_input'), 5, 0.5).click()
        # 选择Engagement框内的元素
        show_wait(browser, 'xpath', f"//*[text()='{engName}']", 5, 0.5).click()
        time.sleep(1)
        activity = show_wait(browser, 'xpath', ui.get_data('Look Up', 'Activity_input'), 5, 0.5).get_attribute('value')
        if activity is None:
            get_log.error('Activity为空')
            assert False
        get_log.info(f'activity：{activity}')
        # loc1选择框
        show_wait(browser, 'xpath', ui.get_data('Look Up', 'Loc1_input'), 5, 0.5).click()
        # 选择第一个loc1框内的元素
        show_wait(browser, 'xpath', '/html/body/div[5]/div[1]/div[1]/ul/li[1]', 5, 0.5).click()
        # loc2选择框
        show_wait(browser, 'xpath', ui.get_data('Look Up', 'Loc2_input'), 5, 0.5).click()
        # 选择第一个loc2框内的元素
        show_wait(browser, 'xpath', '/html/body/div[6]/div[1]/div[1]/ul/li[1]', 5, 0.5).click()
        # 提交
        show_wait(browser, 'xpath',
                  ui.get_data('Look Up', 'Submit_btn'),
                  5, 0.5).click()
        time.sleep(2)

        # 获取第一天工时元素属性是否置灰
        element1 = icons[len(icons)-1].find_element(By.XPATH, './../../../td[last()-7]')
        class_name1 = element1.get_attribute('class')
        if str(class_name1).find('weekendClass') == -1:
            element1.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 获取第二天工时元素属性是否置灰
        element2 = icons[len(icons)-1].find_element(By.XPATH, './../../../td[last()-6]')
        class_name2 = element2.get_attribute('class')
        if str(class_name2).find('weekendClass') == -1:
            element2.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 获取第三天工时元素属性是否置灰
        element3 = icons[len(icons)-1].find_element(By.XPATH, './../../../td[last()-5]')
        class_name3 = element3.get_attribute('class')
        if str(class_name3).find('weekendClass') == -1:
            element3.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 获取第四天工时元素属性是否置灰
        element4 = icons[len(icons)-1].find_element(By.XPATH, './../../../td[last()-4]')
        class_name4 = element4.get_attribute('class')
        if str(class_name4).find('weekendClass') == -1:
            element4.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 获取第五天工时元素属性是否置灰
        element5 = icons[len(icons)-1].find_element(By.XPATH, './../../../td[last()-3]')
        class_name5 = element5.get_attribute('class')
        if str(class_name5).find('weekendClass') == -1:
            element5.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 获取第六天工时元素属性是否置灰
        element6 = icons[len(icons)-1].find_element(By.XPATH, './../../../td[last()-2]')
        class_name6 = element6.get_attribute('class')
        if str(class_name6).find('weekendClass') == -1:
            element6.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 获取第七天工时元素属性是否置灰
        element7 = icons[len(icons) - 1].find_element(By.XPATH, './../../../td[last()-1]')
        class_name7 = element7.get_attribute('class')
        if str(class_name7).find('weekendClass') == -1:
            element7.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 提交工时单
        show_wait(browser, 'xpath', ui.get_data('timesheet', 'Submit_btn1'), 5, 0.5).click()
        time.sleep(1)
        # 确认提交
        # show_wait(browser, 'xpath', '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[6]/div/div[3]/span/button[1]', 5, 0.5).click()
        show_wait(browser, 'xpath', ui.get_data('timesheet', 'submit_btn2'), 5, 0.5).click()

        # 获取提交后的文本信息
        element_tj = show_wait(browser, 'xpath', ui.get_data('timesheet', 'submit_alert'), 5, 0.5).text
        get_log.info('提交后的文本信息：'+element_tj)
        assert str(element_tj) == 'Submit Successfully'
    except Exception as e:
        get_log.error(f'用例执行过程发生异常，异常类型：{e.__class__.__name__}'+traceback.format_exc()+'------------\n')
        assert False


def test_typep(get_log, browser):
    '''
        项目类型 EngType = P
    '''

    try:
        eng_type = 'P'
        user_p = Base.find_dict(user_data, data_key.test_scene, eng_type)
        user = user_p[0][data_key.test_username]
        pwd = str(int(user_p[0][data_key.test_password]))
        engName = seach_engName(user, pwd, eng_type)

        if engName == '':
            get_log.error('项目名未获取到')
            assert False
        get_log.info('engagement元素选择的项目名为：' + engName)
        browser.get(r"https://bcp-preuat.ey.com.cn/login?redirect=%2Ftim%2F")
        # 用户名输入框
        user_input = show_wait(browser, 'xpath', ui.get_data('login', 'user_input'), 5, 0.5)
        # 密码输入框
        pwd_input = show_wait(browser, 'xpath', ui.get_data('login', 'pwd_input'), 5, 0.5)
        user_input.clear()
        user_input.send_keys(user)
        pwd_input.clear()
        pwd_input.send_keys(pwd)
        # 登陆按钮
        show_wait(browser, 'xpath', ui.get_data('login', 'loging_btn'), 5, 0.5).click()
        time.sleep(1)
        # 侧边栏快捷菜单的工时列表按钮
        show_wait(browser, 'xpath', ui.get_data('home_page', 'Current_Week_Timesheet'), 5, 0.5).click()
        time.sleep(2)
        # 先清空工时表单
        select_all = browser.find_element(By.XPATH, ui.get_data('timesheet', 'select_all'))
        # 此处的元素无法直接点击，只能使用js的方式模拟点击
        browser.execute_script("arguments[0].click();", select_all)
        show_wait(browser, 'xpath', ui.get_data('timesheet', 'delete_project'), 5, 0.5).click()
        # 添加工时表单按钮
        show_wait(browser, 'xpath', ui.get_data('timesheet', 'add_project'), 5, 0.5).click()
        # 点击最后一行的 look up 按钮
        icons = browser.find_elements(By.XPATH, ui.get_data('timesheet', 'last_tr_engcode'))
        icons[len(icons) - 1].click()

        # 展开Type选择框
        show_wait(browser, 'xpath', ui.get_data('Look Up', 'Type_input'), 5, 0.5).click()
        # 选择Type框内的元素
        show_wait(browser, 'xpath', '/html/body/div[3]/div[1]/div[1]/ul/li[2]', 5, 0.5).click()
        # 展开Engagement选择框
        show_wait(browser, 'xpath', ui.get_data('Look Up', 'Engagement_input'), 5, 0.5).click()
        # 选择Engagement框内的元素
        show_wait(browser, 'xpath', f"//*[text()='{engName}']", 5, 0.5).click()
        time.sleep(1)
        # activity = show_wait(browser, 'xpath',
        #                      '/html/body/div[1]/div/div/div[2]/div/div/div/div/div[2]/section/div/div[1]/div/div[2]/div[4]/div[2]/div/div[2]/form/div[4]/div/div/div/div/input',
        #                      5, 0.5).get_attribute('value')
        activity = show_wait(browser, 'xpath', ui.get_data('Look Up', 'Activity_input'), 5, 0.5).get_attribute('value')
        if activity is None:
            get_log.error('Activity为空')
            assert False
        get_log.info(f'activity：{activity}')
        # loc1选择框
        show_wait(browser, 'xpath', ui.get_data('Look Up', 'Loc1_input'), 5, 0.5).click()
        # 选择第一个loc1框内的元素
        show_wait(browser, 'xpath', '/html/body/div[5]/div[1]/div[1]/ul/li[1]', 5, 0.5).click()
        # loc2选择框
        show_wait(browser, 'xpath', ui.get_data('Look Up', 'Loc2_input'), 5, 0.5).click()
        # 选择第一个loc2框内的元素
        show_wait(browser, 'xpath', '/html/body/div[6]/div[1]/div[1]/ul/li[1]', 5, 0.5).click()
        # 提交
        show_wait(browser, 'xpath',
                  ui.get_data('Look Up', 'Submit_btn'),
                  5, 0.5).click()
        time.sleep(2)
        # 获取第一天工时元素属性是否置灰
        element1 = icons[len(icons) - 1].find_element(By.XPATH, './../../../td[last()-7]')
        class_name1 = element1.get_attribute('class')
        if str(class_name1).find('weekendClass') == -1:
            element1.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 获取第二天工时元素属性是否置灰
        element2 = icons[len(icons) - 1].find_element(By.XPATH, './../../../td[last()-6]')
        class_name2 = element2.get_attribute('class')
        if str(class_name2).find('weekendClass') == -1:
            element2.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 获取第三天工时元素属性是否置灰
        element3 = icons[len(icons) - 1].find_element(By.XPATH, './../../../td[last()-5]')
        class_name3 = element3.get_attribute('class')
        if str(class_name3).find('weekendClass') == -1:
            element3.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 获取第四天工时元素属性是否置灰
        element4 = icons[len(icons) - 1].find_element(By.XPATH, './../../../td[last()-4]')
        class_name4 = element4.get_attribute('class')
        if str(class_name4).find('weekendClass') == -1:
            element4.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 获取第五天工时元素属性是否置灰
        element5 = icons[len(icons) - 1].find_element(By.XPATH, './../../../td[last()-3]')
        class_name5 = element5.get_attribute('class')
        if str(class_name5).find('weekendClass') == -1:
            element5.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 获取第六天工时元素属性是否置灰
        element6 = icons[len(icons) - 1].find_element(By.XPATH, './../../../td[last()-2]')
        class_name6 = element6.get_attribute('class')
        if str(class_name6).find('weekendClass') == -1:
            element6.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 获取第七天工时元素属性是否置灰
        element7 = icons[len(icons) - 1].find_element(By.XPATH, './../../../td[last()-1]')
        class_name7 = element7.get_attribute('class')
        if str(class_name7).find('weekendClass') == -1:
            element7.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 提交工时单
        show_wait(browser, 'xpath', ui.get_data('timesheet', 'Submit_btn1'), 5, 0.5).click()
        time.sleep(1)
        # 确认提交
        show_wait(browser, 'xpath', ui.get_data('timesheet', 'submit_btn2'), 5, 0.5).click()

        # 获取提交后的文本信息
        element_tj = show_wait(browser, 'xpath', ui.get_data('timesheet', 'submit_alert'), 5, 0.5).text
        get_log.info('提交后的文本信息：' + element_tj)
        assert str(element_tj) == 'Submit Successfully'
    except Exception as e:
        get_log.error(
            f'用例执行过程发生异常，异常类型：{e.__class__.__name__}' + traceback.format_exc() + '------------\n')
        assert False


def test_over_time_EM_EP(get_log, browser):
    '''
        特殊场景，多出两个EM,EP输入框
    '''
    user_c = Base.find_dict(user_data, data_key.test_scene, 'EM_EP')
    try:
        user = user_c[0][data_key.test_username]
        pwd = str(int(user_c[0][data_key.test_password]))
        browser.get(r"https://bcp-preuat.ey.com.cn/login?redirect=%2Ftim%2F")
        # 用户名输入框
        user_input = show_wait(browser, 'xpath', ui.get_data('login', 'user_input'), 5, 0.5)
        # 密码输入框
        pwd_input = show_wait(browser, 'xpath', ui.get_data('login', 'pwd_input'), 5, 0.5)
        user_input.clear()
        user_input.send_keys(user)
        pwd_input.clear()
        pwd_input.send_keys(pwd)
        # 登陆按钮
        show_wait(browser, 'xpath', ui.get_data('login', 'loging_btn'), 5, 0.5).click()
        time.sleep(1)
        # 侧边栏快捷菜单的工时列表按钮
        show_wait(browser, 'xpath', ui.get_data('home_page', 'Current_Week_Timesheet'), 5, 0.5).click()
        time.sleep(2)
        # 先清空工时表单
        select_all = browser.find_element(By.XPATH, ui.get_data('timesheet', 'select_all'))
        # 此处的元素无法直接点击，只能使用js的方式模拟点击
        browser.execute_script("arguments[0].click();", select_all)
        show_wait(browser, 'xpath', ui.get_data('timesheet', 'delete_project'), 5, 0.5).click()

        # 添加第一个项目
        # 添加工时表单按钮
        show_wait(browser, 'xpath', ui.get_data('timesheet', 'add_project'), 5, 0.5).click()
        # 点击最后一行的 look up 按钮
        icons = browser.find_elements(By.XPATH, ui.get_data('timesheet', 'last_tr_engcode'))
        icons[len(icons) - 1].click()
        # 展开Time Type选择框
        show_wait(browser, 'xpath', ui.get_data('Look Up', 'Time_Type_input'), 5, 0.5).click()
        # 选择Time Type框内的元素
        show_wait(browser, 'xpath', '/html/body/div[3]/div[1]/div[1]/ul/li[1]', 5, 0.5).click()
        # 展开Type选择框
        show_wait(browser, 'xpath', ui.get_data('Look Up', 'Type_input'), 5, 0.5).click()
        # 选择Type框内的元素
        show_wait(browser, 'xpath', '/html/body/div[4]/div[1]/div[1]/ul/li[1]', 5, 0.5).click()
        # 展开Engagement选择框
        show_wait(browser, 'xpath', ui.get_data('Look Up', 'Engagement_input'), 5, 0.5).click()
        time.sleep(1)
        # 选择Engagement框内的元素，此元素需要加载一下，使用time.sleep强制等待也可以，以下是通过鼠标悬浮方式
        show_wait(browser, 'xpath',
                            '/html/body/div[5]/div[1]/div[1]/ul/li[1]',
                            5, 0.5).click()
        time.sleep(1)
        activity = show_wait(browser, 'xpath', ui.get_data('Look Up', 'Activity_input'), 5, 0.5).get_attribute('value')
        if activity is None:
            get_log.error('Activity为空')
            assert False
        get_log.info(f'activity：{activity}')
        # loc1选择框
        show_wait(browser, 'xpath', ui.get_data('Look Up', 'Loc1_input'), 5, 0.5).click()
        # 选择第一个loc1框内的元素
        show_wait(browser, 'xpath', '/html/body/div[6]/div[1]/div[1]/ul/li[1]', 5, 0.5).click()
        # loc2选择框
        show_wait(browser, 'xpath', ui.get_data('Look Up', 'Loc2_input'), 5, 0.5).click()
        # 选择第一个loc2框内的元素
        show_wait(browser, 'xpath', '/html/body/div[7]/div[1]/div[1]/ul/li[1]', 5, 0.5).click()
        # 提交
        show_wait(browser, 'xpath',
                  ui.get_data('Look Up', 'Submit_btn'),
                  5, 0.5).click()
        time.sleep(2)
        # 获取第一天工时元素属性是否置灰
        element1 = icons[len(icons) - 1].find_element(By.XPATH, './../../../td[last()-7]')
        class_name1 = element1.get_attribute('class')
        if str(class_name1).find('weekendClass') == -1:
            element1.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 获取第二天工时元素属性是否置灰
        element2 = icons[len(icons) - 1].find_element(By.XPATH, './../../../td[last()-6]')
        class_name2 = element2.get_attribute('class')
        if str(class_name2).find('weekendClass') == -1:
            element2.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 获取第三天工时元素属性是否置灰
        element3 = icons[len(icons) - 1].find_element(By.XPATH, './../../../td[last()-5]')
        class_name3 = element3.get_attribute('class')
        if str(class_name3).find('weekendClass') == -1:
            element3.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 获取第四天工时元素属性是否置灰
        element4 = icons[len(icons) - 1].find_element(By.XPATH, './../../../td[last()-4]')
        class_name4 = element4.get_attribute('class')
        if str(class_name4).find('weekendClass') == -1:
            element4.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 获取第五天工时元素属性是否置灰
        element5 = icons[len(icons) - 1].find_element(By.XPATH, './../../../td[last()-3]')
        class_name5 = element5.get_attribute('class')
        if str(class_name5).find('weekendClass') == -1:
            element5.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 获取第六天工时元素属性是否置灰
        element6 = icons[len(icons) - 1].find_element(By.XPATH, './../../../td[last()-2]')
        class_name6 = element6.get_attribute('class')
        if str(class_name6).find('weekendClass') == -1:
            element6.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 获取第七天工时元素属性是否置灰
        element7 = icons[len(icons) - 1].find_element(By.XPATH, './../../../td[last()-1]')
        class_name7 = element7.get_attribute('class')
        if str(class_name7).find('weekendClass') == -1:
            element7.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)

        # 添加第二个项目
        # 添加工时表单按钮
        show_wait(browser, 'xpath', ui.get_data('timesheet', 'add_project'), 5, 0.5).click()
        # 点击最后一行的 look up 按钮
        icons = browser.find_elements(By.XPATH, ui.get_data('timesheet', 'last_tr_engcode'))
        icons[len(icons) - 1].click()
        # 展开Time Type选择框
        show_wait(browser, 'xpath', ui.get_data('Look Up', 'Time_Type_input'), 5, 0.5).click()
        # 选择Time Type框内的元素
        show_wait(browser, 'xpath', '/html/body/div[7]/div[1]/div[1]/ul/li[2]', 5, 0.5).click()
        # 展开Type选择框
        show_wait(browser, 'xpath', ui.get_data('Look Up', 'Type_input'), 5, 0.5).click()
        # 选择Type框内的元素
        show_wait(browser, 'xpath', '/html/body/div[7]/div[1]/div[1]/ul/li[1]', 5, 0.5).click()
        # 展开Engagement选择框
        show_wait(browser, 'xpath', ui.get_data('Look Up', 'Engagement_input'), 5, 0.5).click()
        time.sleep(1)
        # 选择Engagement框内的元素，此元素需要加载一下，使用time.sleep强制等待也可以，以下是通过鼠标悬浮方式
        engment = show_wait(browser, 'xpath', "//*[text()='23451863-XRVG-GYK IGGJFP XFBFnqkkxdyxvb - FEPLR LLSWYX DONAS EOEDDRFVSG KA., KEX.']/..", 5, 0.5)
        ActionChains(browser).move_to_element(engment).perform()
        engment.click()
        time.sleep(1)
        activity = show_wait(browser, 'xpath', ui.get_data('Look Up', 'Activity_input'), 5, 0.5).get_attribute('value')
        if activity is None:
            get_log.error('Activity为空')
            assert False
        get_log.info(f'activity：{activity}')
        # loc1选择框
        show_wait(browser, 'xpath', ui.get_data('Look Up', 'Loc1_input'), 5, 0.5).click()
        # 选择第一个loc1框内的元素
        show_wait(browser, 'xpath', '/html/body/div[7]/div[1]/div[1]/ul/li[1]', 5, 0.5).click()
        # loc2选择框
        show_wait(browser, 'xpath', ui.get_data('Look Up', 'Loc2_input'), 5, 0.5).click()
        # 选择第一个loc2框内的元素
        show_wait(browser, 'xpath', '/html/body/div[7]/div[1]/div[1]/ul/li[1]', 5, 0.5).click()
        # OT EM框输入信息
        show_wait(browser, 'xpath', ui.get_data('Look Up', 'OT_Approver_EM_input'), 5, 0.5).send_keys('wq')
        time.sleep(1)
        # OT EM框选择信息
        show_wait(browser, 'xpath', '/html/body/div[8]/div[1]/div[1]/ul/li[1]', 5, 0.5).click()
        # OT EP框输入信息
        show_wait(browser, 'xpath', ui.get_data('Look Up', 'OT_Approver_EP_input'), 5, 0.5).send_keys('wa')
        time.sleep(1)
        # OT EP框选择信息
        show_wait(browser, 'xpath', '/html/body/div[9]/div[1]/div[1]/ul/li[1]', 5, 0.5).click()
        # 提交
        show_wait(browser, 'xpath',
                  ui.get_data('Look Up', 'Submit_btn'),
                  5, 0.5).click()
        time.sleep(2)
        # 获取第一天工时元素属性是否置灰
        element1 = icons[len(icons) - 1].find_element(By.XPATH, './../../../td[last()-7]')
        class_name1 = element1.get_attribute('class')
        if str(class_name1).find('weekendClass') == -1:
            element1.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 获取第二天工时元素属性是否置灰
        element2 = icons[len(icons) - 1].find_element(By.XPATH, './../../../td[last()-6]')
        class_name2 = element2.get_attribute('class')
        if str(class_name2).find('weekendClass') == -1:
            element2.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 获取第三天工时元素属性是否置灰
        element3 = icons[len(icons) - 1].find_element(By.XPATH, './../../../td[last()-5]')
        class_name3 = element3.get_attribute('class')
        if str(class_name3).find('weekendClass') == -1:
            element3.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 获取第四天工时元素属性是否置灰
        element4 = icons[len(icons) - 1].find_element(By.XPATH, './../../../td[last()-4]')
        class_name4 = element4.get_attribute('class')
        if str(class_name4).find('weekendClass') == -1:
            element4.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 获取第五天工时元素属性是否置灰
        element5 = icons[len(icons) - 1].find_element(By.XPATH, './../../../td[last()-3]')
        class_name5 = element5.get_attribute('class')
        if str(class_name5).find('weekendClass') == -1:
            element5.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 获取第六天工时元素属性是否置灰
        element6 = icons[len(icons) - 1].find_element(By.XPATH, './../../../td[last()-2]')
        class_name6 = element6.get_attribute('class')
        if str(class_name6).find('weekendClass') == -1:
            element6.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 获取第七天工时元素属性是否置灰
        element7 = icons[len(icons) - 1].find_element(By.XPATH, './../../../td[last()-1]')
        class_name7 = element7.get_attribute('class')
        if str(class_name7).find('weekendClass') == -1:
            element7.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 提交工时单
        show_wait(browser, 'xpath', ui.get_data('timesheet', 'Submit_btn1'), 5, 0.5).click()
        time.sleep(1)
        # 确认提交
        show_wait(browser, 'xpath', ui.get_data('timesheet', 'submit_btn2'), 5, 0.5).click()

        # 获取提交后的文本信息
        element_tj = show_wait(browser, 'xpath', ui.get_data('timesheet', 'submit_alert'), 5, 0.5).text
        get_log.info('提交后的文本信息：' + element_tj)
        assert str(element_tj) == 'Submit Successfully'
    except Exception as e:
        get_log.error(f'用例执行过程发生异常，异常类型：{e.__class__.__name__}'+traceback.format_exc()+'------------\n')
        assert False


def test_over_time_TaskType(get_log, browser):
    '''
    特殊场景，多出一个Task Type框
    选择项目code为23470188时，有Task Type选项
    engname 选择 23470188-GWT1589-85 Erh Zrsa - IOP OHLB NKPTJCZD QTBPUPV
    Time Type为Over Time 且 Type为Chargeable
    '''
    user_c = Base.find_dict(user_data, data_key.test_scene, 'Task1')
    try:
        user = user_c[0][data_key.test_username]
        pwd = str(int(user_c[0][data_key.test_password]))
        browser.get(r"https://bcp-preuat.ey.com.cn/login?redirect=%2Ftim%2F")
        # 用户名输入框
        user_input = show_wait(browser, 'xpath', ui.get_data('login', 'user_input'), 5, 0.5)
        # 密码输入框
        pwd_input = show_wait(browser, 'xpath', ui.get_data('login', 'pwd_input'), 5, 0.5)
        user_input.clear()
        user_input.send_keys(user)
        pwd_input.clear()
        pwd_input.send_keys(pwd)
        # 登陆按钮
        show_wait(browser, 'xpath', ui.get_data('login', 'loging_btn'), 5, 0.5).click()
        time.sleep(1)
        # 侧边栏快捷菜单的工时列表按钮
        show_wait(browser, 'xpath', ui.get_data('home_page', 'Current_Week_Timesheet'), 5, 0.5).click()
        time.sleep(2)
        # 先清空工时表单
        select_all = browser.find_element(By.XPATH, ui.get_data('timesheet', 'select_all'))
        # 此处的元素无法直接点击，只能使用js的方式模拟点击
        browser.execute_script("arguments[0].click();", select_all)
        show_wait(browser, 'xpath', ui.get_data('timesheet', 'delete_project'), 5, 0.5).click()

        # 添加第一个项目
        # 添加工时表单按钮
        show_wait(browser, 'xpath', ui.get_data('timesheet', 'add_project'), 5, 0.5).click()
        # 点击最后一行的 look up 按钮
        icons = browser.find_elements(By.XPATH, ui.get_data('timesheet', 'last_tr_engcode'))
        icons[len(icons) - 1].click()
        # 展开Time Type选择框
        show_wait(browser, 'xpath', ui.get_data('Look Up', 'Time_Type_input'), 5, 0.5).click()
        # 选择Time Type框内的元素
        show_wait(browser, 'xpath', '/html/body/div[3]/div[1]/div[1]/ul/li[1]', 5, 0.5).click()
        # 展开Type选择框
        show_wait(browser, 'xpath', ui.get_data('Look Up', 'Type_input'), 5, 0.5).click()
        # 选择Type框内的元素
        show_wait(browser, 'xpath', '/html/body/div[4]/div[1]/div[1]/ul/li[1]', 5, 0.5).click()
        # 展开Engagement选择框
        show_wait(browser, 'xpath', ui.get_data('Look Up', 'Engagement_input'), 5, 0.5).click()
        time.sleep(1)
        # 选择Engagement框内的元素，此元素需要加载一下，使用time.sleep强制等待也可以，以下是通过鼠标悬浮方式
        show_wait(browser, 'xpath',
                            '/html/body/div[5]/div[1]/div[1]/ul/li[1]',
                            5, 0.5).click()
        time.sleep(1)
        activity = show_wait(browser, 'xpath', ui.get_data('Look Up', 'Activity_input'), 5, 0.5).get_attribute('value')
        if activity is None:
            get_log.error('Activity为空')
            assert False
        get_log.info(f'activity：{activity}')
        # loc1选择框
        show_wait(browser, 'xpath', ui.get_data('Look Up', 'Loc1_input'), 5, 0.5).click()
        # 选择第一个loc1框内的元素
        show_wait(browser, 'xpath', '/html/body/div[6]/div[1]/div[1]/ul/li[1]', 5, 0.5).click()
        # loc2选择框
        show_wait(browser, 'xpath', ui.get_data('Look Up', 'Loc2_input'), 5, 0.5).click()
        # 选择第一个loc2框内的元素
        show_wait(browser, 'xpath', '/html/body/div[7]/div[1]/div[1]/ul/li[1]', 5, 0.5).click()
        # 提交
        show_wait(browser, 'xpath',
                  ui.get_data('Look Up', 'Submit_btn'),
                  5, 0.5).click()
        time.sleep(2)
        # 获取第一天工时元素属性是否置灰
        element1 = icons[len(icons) - 1].find_element(By.XPATH, './../../../td[last()-7]')
        class_name1 = element1.get_attribute('class')
        if str(class_name1).find('weekendClass') == -1:
            element1.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 获取第二天工时元素属性是否置灰
        element2 = icons[len(icons) - 1].find_element(By.XPATH, './../../../td[last()-6]')
        class_name2 = element2.get_attribute('class')
        if str(class_name2).find('weekendClass') == -1:
            element2.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 获取第三天工时元素属性是否置灰
        element3 = icons[len(icons) - 1].find_element(By.XPATH, './../../../td[last()-5]')
        class_name3 = element3.get_attribute('class')
        if str(class_name3).find('weekendClass') == -1:
            element3.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 获取第四天工时元素属性是否置灰
        element4 = icons[len(icons) - 1].find_element(By.XPATH, './../../../td[last()-4]')
        class_name4 = element4.get_attribute('class')
        if str(class_name4).find('weekendClass') == -1:
            element4.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 获取第五天工时元素属性是否置灰
        element5 = icons[len(icons) - 1].find_element(By.XPATH, './../../../td[last()-3]')
        class_name5 = element5.get_attribute('class')
        if str(class_name5).find('weekendClass') == -1:
            element5.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 获取第六天工时元素属性是否置灰
        element6 = icons[len(icons) - 1].find_element(By.XPATH, './../../../td[last()-2]')
        class_name6 = element6.get_attribute('class')
        if str(class_name6).find('weekendClass') == -1:
            element6.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 获取第七天工时元素属性是否置灰
        element7 = icons[len(icons) - 1].find_element(By.XPATH, './../../../td[last()-1]')
        class_name7 = element7.get_attribute('class')
        if str(class_name7).find('weekendClass') == -1:
            element7.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)

        # 添加第二个项目
        # 添加工时表单按钮
        show_wait(browser, 'xpath', ui.get_data('timesheet', 'add_project'), 5, 0.5).click()
        # 点击最后一行的 look up 按钮
        icons = browser.find_elements(By.XPATH, ui.get_data('timesheet', 'last_tr_engcode'))
        icons[len(icons) - 1].click()
        # 展开Time Type选择框
        show_wait(browser, 'xpath', ui.get_data('Look Up', 'Time_Type_input'), 5, 0.5).click()
        # 选择Time Type框内的元素
        show_wait(browser, 'xpath', '/html/body/div[7]/div[1]/div[1]/ul/li[2]', 5, 0.5).click()
        # 展开Type选择框
        show_wait(browser, 'xpath', ui.get_data('Look Up', 'Type_input'), 5, 0.5).click()
        # 选择Type框内的元素
        show_wait(browser, 'xpath', '/html/body/div[7]/div[1]/div[1]/ul/li[1]', 5, 0.5).click()
        # 展开Engagement选择框
        show_wait(browser, 'xpath', ui.get_data('Look Up', 'Engagement_input'), 5, 0.5).click()
        time.sleep(1)
        # 选择Engagement框内的元素，此元素需要加载一下，使用time.sleep强制等待也可以，以下是通过鼠标悬浮方式
        engment = show_wait(browser, 'xpath', "//*[text()='23470188-GWT1589-85 Erh Zrsa - IOP OHLB NKPTJCZD QTBPUPV']/..", 5, 0.5)
        ActionChains(browser).move_to_element(engment).perform()
        engment.click()
        time.sleep(1)
        activity = show_wait(browser, 'xpath', ui.get_data('Look Up', 'Activity_input'), 5, 0.5).get_attribute('value')
        if activity is None:
            get_log.error('Activity为空')
            assert False
        get_log.info(f'activity：{activity}')
        # loc1选择框
        show_wait(browser, 'xpath', ui.get_data('Look Up', 'Loc1_input'), 5, 0.5).click()
        time.sleep(1)
        # 选择第一个loc1框内的元素
        show_wait(browser, 'xpath', '/html/body/div[7]/div[1]/div[1]/ul/li[1]', 5, 0.5).click()
        # loc2选择框
        show_wait(browser, 'xpath', ui.get_data('Look Up', 'Loc2_input'), 5, 0.5).click()
        time.sleep(1)
        # 选择第一个loc2框内的元素
        show_wait(browser, 'xpath', '/html/body/div[7]/div[1]/div[1]/ul/li[1]', 5, 0.5).click()
        # Task Type展开
        show_wait(browser, 'xpath', ui.get_data('Look Up', 'Task_Type_input'), 5, 0.5).click()
        time.sleep(1)
        # Task Type框选择信息
        show_wait(browser, 'xpath', '/html/body/div[8]/div[1]/div[1]/ul/li[1]', 5, 0.5).click()
        # 提交
        show_wait(browser, 'xpath',
                  ui.get_data('Look Up', 'Submit_btn'),
                  5, 0.5).click()
        time.sleep(2)
        # 获取第一天工时元素属性是否置灰
        element1 = icons[len(icons) - 1].find_element(By.XPATH, './../../../td[last()-7]')
        class_name1 = element1.get_attribute('class')
        if str(class_name1).find('weekendClass') == -1:
            element1.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 获取第二天工时元素属性是否置灰
        element2 = icons[len(icons) - 1].find_element(By.XPATH, './../../../td[last()-6]')
        class_name2 = element2.get_attribute('class')
        if str(class_name2).find('weekendClass') == -1:
            element2.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 获取第三天工时元素属性是否置灰
        element3 = icons[len(icons) - 1].find_element(By.XPATH, './../../../td[last()-5]')
        class_name3 = element3.get_attribute('class')
        if str(class_name3).find('weekendClass') == -1:
            element3.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 获取第四天工时元素属性是否置灰
        element4 = icons[len(icons) - 1].find_element(By.XPATH, './../../../td[last()-4]')
        class_name4 = element4.get_attribute('class')
        if str(class_name4).find('weekendClass') == -1:
            element4.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 获取第五天工时元素属性是否置灰
        element5 = icons[len(icons) - 1].find_element(By.XPATH, './../../../td[last()-3]')
        class_name5 = element5.get_attribute('class')
        if str(class_name5).find('weekendClass') == -1:
            element5.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 获取第六天工时元素属性是否置灰
        element6 = icons[len(icons) - 1].find_element(By.XPATH, './../../../td[last()-2]')
        class_name6 = element6.get_attribute('class')
        if str(class_name6).find('weekendClass') == -1:
            element6.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 获取第七天工时元素属性是否置灰
        element7 = icons[len(icons) - 1].find_element(By.XPATH, './../../../td[last()-1]')
        class_name7 = element7.get_attribute('class')
        if str(class_name7).find('weekendClass') == -1:
            element7.find_element(By.XPATH, './div/div/div/div/input').send_keys(8)
        # 提交工时单
        show_wait(browser, 'xpath', ui.get_data('timesheet', 'Submit_btn1'), 5, 0.5).click()
        time.sleep(1)
        # 获取提交后的文本信息
        element_tj = show_wait(browser, 'xpath', ui.get_data('timesheet', 'submit_alert'), 5, 0.5).text
        get_log.info('提交后的文本信息：' + element_tj)
        assert str(element_tj) == 'Submit Successfully'
    except Exception as e:
        get_log.error(f'用例执行过程发生异常，异常类型：{e.__class__.__name__}'+traceback.format_exc()+'------------\n')
        assert False