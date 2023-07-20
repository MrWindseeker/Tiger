from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()

ts_url = 'https://bcp-preuat.ey.com.cn/tim'

browser.get(ts_url)

# print(browser.page_source)
# text = soup.get_text()
# with open("D:\\Windseeker\\Desktop\\html.txt", "w", encoding="utf-8") as f:
#     f.write(text)

# 用户名输入
# browser.find_element_by_css_selector("input[type='text']").send_keys('tom.t.xu')
browser.find_element(By.CSS_SELECTOR, "input[placeholder='账号']").clear()
browser.find_element(By.CSS_SELECTOR, "input[placeholder='账号']").send_keys('tom.t.xu')

# 密码输入
browser.find_element(By.CSS_SELECTOR, "input[placeholder='密码']").clear()
browser.find_element(By.CSS_SELECTOR, "input[placeholder='密码']").send_keys('123456')

# 登录
browser.find_element(By.CLASS_NAME, 'el-button--medium').click()

time.sleep(5)

# 点击 'Timesheet'
browser.find_element(By.CSS_SELECTOR, "span[title='Timesheet']").click()

time.sleep(2)

# 点击 'Current Week Timesheet'
browser.find_element(By.XPATH, '/html/body/div[3]/ul/div[1]/div/li/span').click()

time.sleep(10)