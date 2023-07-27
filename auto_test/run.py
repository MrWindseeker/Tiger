import pytest
from config.Conf import *
import time

case_path = get_case_path()+'/tim_test.py'
report_name = str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))+'.html'
report_path = get_allure_path()+'/'+report_name

if __name__ == '__main__':
	pytest.main([case_path, '--html='+report_path])