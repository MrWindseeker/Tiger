import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.LogUtil import sys_log
import json

# 定义封装类
class AssertUtil:
    # 初始化数据，设置日志名称
    def __init__(self):
        self.log = sys_log('AssertUtil')

    # 验证返回状态码
    def assert_code(self, code, expected_code):
        try:
            assert int(code) == int(expected_code)
            self.log.debug('code检验通过')
            return True
        except:
            self.log.error('code error, code is {}, expected_code is {}'.format(code, expected_code))
            raise

    # 验证返回结果内容
    def assert_body(self, body, expected_body):
        try:
            assert str(body) == str(expected_body)
            self.log.debug('body检验通过')
            return True
        except:
            self.log.error('body error, body is {}, expected_body is {}'.format(body, expected_body))
            raise

    # 验证返回结果是否包含期望的结果
    def assert_in_body(self, body, expected_body):
        # body统一转格式
        try:
            body = json.dumps(body)
            assert expected_body in body
            self.log.debug('body检验通过')
            return True
        except:
            self.log.error('not in or body error, body is {}, expected_body is {}'.format(body, expected_body))
            raise

if __name__ == '__main__':
    assert_util = AssertUtil()
    # assert_util.assert_code('200', '2000')
    # assert_util.assert_in_body('20000', '2000')
    s = ''
    # str = (s.encode('raw_unicode_escape')).decode()
    # print(str)

    # s = '\xe4\xbd\xa0\xe5\xa5\xbd'
    b = s.encode('raw_unicode_escape')
    s = b.decode()
    print(b)  # b'\xe4\xbd\xa0\xe5\xa5\xbd'
    print(s)  # 你好