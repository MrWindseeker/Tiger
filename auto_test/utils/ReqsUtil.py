# 公共方法封装
import requests, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.LogUtil import LogUtil


class ReqsUtil:
    """ 封装requests请求工具类 """
    def __init__(self):
        """ 初始化requests请求工具类 """
        self.log = LogUtil.sys_log('ReqsUtil')

    # 1、定义公共方法
    def req_api(self, url, method = 'get', data = None, json = None, headers = None, cookies = None, img = None):
        """ 发送请求"""
    # 2、根据参数method判断get/post请求
        if method == 'get':
            # 发送get请求
            self.log.info('发送get请求，url：{}'.format(url))
            r = requests.get(url, data = data, json = json, headers = headers, cookies = cookies)
        elif method == 'post':
            # 发送post请求
            self.log.info('发送post请求，url：{}'.format(url))
            r = requests.post(url, data = data, json = json, headers = headers, cookies = cookies)
    # 3、获取结果内容
        code = r.status_code
        content = r.content
        try:
            body = r.json()
        except Exception as e:
            body = r.text
    # 4、内容存到字典
        res = dict()
        res['code'] = code
        if not img:
            res['body'] = body
        elif img == 'y':
            res['content'] = content
    # 5、字典返回
        return res

    # 1、重构get方法
    def req_get(self, url, img = None, **kwargs):
        """ 发送get请求 """
    # 2、定义参数
    # url, json, headers, cookies, method等，可以使用**kwargs
    # 3、调用公共方法
        return self.req_api(url, method='get', img = img, **kwargs)

    # 1、重构post方法
    def req_post(self, url, img = None, **kwargs):
        """ 发送post请求 """
    # 2、定义参数
    # url, json, headers, cookies, method等，可以使用**kwargs
    # 3、调用公共方法
        return self.req_api(url, method='post', img = img, **kwargs)