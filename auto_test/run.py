import pytest
from config.Conf import *
import datetime

cur_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
case_path = get_case_path() + os.sep + 'tim_test.py'
report_name = cur_time + '.html'
report_path = get_pytest_path() + os.sep + report_name

print(case_path)
print(report_path)

if __name__ == '__main__':
	pytest.main([case_path, '--html='+report_path])