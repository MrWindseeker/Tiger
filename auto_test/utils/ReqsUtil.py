# 公共方法封装
import requests, sys, os
from requests.exceptions import RequestException
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.LogUtil import LogUtil


class ReqsUtil:
    """Requests 请求工具类"""

    def __init__(self):
        """ 初始化日志 """
        self.log = LogUtil.sys_log()

    def req_api(self, url, method = 'get', data = None, json = None, headers = None, cookies = None, return_binary = False):
        """
        发送 HTTP 请求
        :param url: 请求地址
        :param method: 请求方法（get/post）
        :param data: 请求体参数（表单）
        :param json: 请求体参数（JSON）
        :param headers: 请求头
        :param cookies: Cookies
        :param return_binary: 是否返回二进制内容
        :return: 包含响应码与响应内容的字典
        """
        try:
            method = method.lower()
            self.log.info('发送{}请求，url：{}'.format(method.upper(), url))

            if method == 'get':
                r = requests.get(url, data = data, json = json, headers = headers, cookies = cookies)
            elif method == 'post':
                r = requests.post(url, data = data, json = json, headers = headers, cookies = cookies)
            else:
                raise ValueError('不支持的请求方法: {}'.format(method.upper()))

            res = {
                'code': r.status_code
            }

            if return_binary:
                res['content'] = r.content
            else:
                try:
                    res['body'] = r.json()
                except ValueError:
                    res['body'] = r.text

            self.log.info('响应状态码：{}'.format(res['code']))
            return res

        except RequestException as e:
            self.log.error('请求异常: {}'.format(e))
            return {'code': 500, 'error': str(e)}

    def req_get(self, url, return_binary = False, **kwargs):
        """
        发送 GET 请求
        :param url: 请求地址
        :param return_binary: 是否返回二进制内容
        :param kwargs: 其他 requests 支持的参数
        :return: 响应结果
        """
        return self.req_api(url, method = 'get', return_binary = return_binary, **kwargs)

    def req_post(self, url, return_binary = False, **kwargs):
        """
        发送 POST 请求
        :param url: 请求地址
        :param return_binary: 是否返回二进制内容
        :param kwargs: 其他 requests 支持的参数
        :return: 响应结果
        """
        return self.req_api(url, method = 'post', return_binary = return_binary, **kwargs)
    

if __name__ == '__main__':
    # 使用示例
    reqs_util = ReqsUtil()
    url = 'https://api.github.com'
    response = reqs_util.req_get(url)
    print('响应内容:', response)