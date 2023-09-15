# coding:utf-8
import os, sys, pytest, time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from py.xml import html
from selenium import webdriver
from utils.LogUtil import sys_log


# 初始化日志
@pytest.fixture(scope='session', autouse=True)
def get_log():
    global log
    log = sys_log('ui_test')
    return log


# 修改html报告中的Environment部分，需要使用时，解除注释即可
def pytest_configure(config):
    config._metadata = {}
    config._metadata['Test Project Name'] = '工时系统'
    config._metadata['Test address'] = 'https://bcp-preuat.ey.com.cn/tim/'
    config._metadata['Tester'] = 'Virgile'


# 在html报告中的summary添加信息
# @pytest.mark.optionalhook
# def pytest_html_results_summary(prefix):
#     prefix.extend([html.p("所属部门：研发部")])
#     prefix.extend([html.p("测试人员：Virgile")])

def pytest_collection_modifyitems(items):
    '''
    修改用例名称中文乱码
    '''
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode_escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode_escape')


# @pytest.mark.optionalhook
@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Case_name'))
    cells.pop(-1)  # 删除link列


# @pytest.mark.optionalhook
@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.pop(-1)  # 删除link列

driver = None

@pytest.fixture(scope='function', autouse=True)
def browser():
    '''
    根据指定浏览器加载驱动
    :param pytestconfig: 结合钩子函数pytest_addoption使用，用于支持指定浏览器执行程序
    :return: 浏览器驱动对象
    '''
    global driver
    # browser_name = pytestconfig.getoption('browser')
    # if browser_name not in browsers:
    #     raise ValueError(f'{browser_name}浏览器暂无下载驱动')
    # if browser_name == 'chrome':
    #     driver = webdriver.Chrome(tool_path+'/chromedriver.exe')
    # elif browser_name == 'firefox':
    #     driver = webdriver.Firefox(executable_path=tool_path+'/geckodriver.exe')
    driver = webdriver.Chrome()
    driver.maximize_window()
    # 隐式等待10秒
    driver.implicitly_wait(10)
    return driver

def _capture_screenshot():
    """
    截图保存为base64，展示到html中
    :return:
    """
    if driver is not None:
        return driver.get_screenshot_as_base64()
    else:
        print("browser autose设置为false，driver获取异常")

# @pytest.mark.hookwrapper
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    当测试失败的时候，自动截图，展示到html报告中
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    report.description = str(item.function.__doc__)
    if report.description is None:
        report.description = str(item.function.__name__)
    else:
        report.description = str(item.function.__doc__)
    report.nodeid = report.nodeid.encode("unicode_escape").decode("utf-8")  # 设置编码显示中文
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            screen_img = _capture_screenshot()
            if file_name and screen_img is not None:
                # 当失败用例，截图返回的是None时，不会添加到报告中
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


@pytest.hookspec(firstresult=True)
def pytest_runtest_protocol(item, nextitem):
    global Item , Nextitem
    Item = item
    Nextitem = nextitem


@pytest.fixture(autouse=True)
def show(get_log, browser):
    '''
    实现前后置作用
    :param get_log: 日志对象
    :param browser: 浏览器驱动对象
    :return:
    '''
    get_log.info('----------用例%s开始执行----------' % Item)
    yield
    time.sleep(0.8)
    browser.quit()
    get_log.info('----------用例%s执行结束----------' % Item)





# def pytest_addoption(parser):
#     '''
#     钩子函数，用于向 pytestconfig内添加配置
#     '''
#     parser.addoption("--browser", action="store", default="chrome", help="change browser to run")