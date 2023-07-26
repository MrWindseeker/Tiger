from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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