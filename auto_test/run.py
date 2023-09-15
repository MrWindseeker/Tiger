import pytest, datetime, os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Conf
from common import Base, BasicSev


# cur_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
# case_path = get_case_path() + os.sep + 'tim_test.py'
# report_name = cur_time + '.html'
# report_path = get_pytest_path() + os.sep + report_name


# if __name__ == '__main__':
# 	pytest.main([case_path, '--html='+report_path])


if __name__ == '__main__':
	# allure测试报告路径
	allure_output = Conf.get_output_path()
	report_path = Conf.get_report_path() + os.sep + 'result'
	report_html_path = Conf.get_report_path() + os.sep + 'allure_html'
	# pytest.main(['--capture=tee-sys', os.path.abspath(__file__)])
	# pytest.main([os.path.abspath(__file__)])
	Base.generate_timestamp()
	pytest.main()
	BasicSev.allure_report(report_path, report_html_path)
	# BasicSev.open_report(report_html_path)
	BasicSev.compress_files()
	subject = '接口测试报告'
	text_cont = '接口测试报告_20230914'
	BasicSev.send_email(subject, text_cont = text_cont, attach_file = [Base.find_latest_file(allure_output)])