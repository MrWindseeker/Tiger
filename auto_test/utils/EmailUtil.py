import smtplib, re, sys, pysnooper
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
from email.utils import parseaddr, formataddr
from email import encoders

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import Base
from utils.LogUtil import LogUtil
from config.Conf import ConfigYaml

# 初始化配置文件
conf_read = ConfigYaml()
# html背景图片定位正则
pattern_img = re.compile("'cid:(.*)'")
# 图片格式
img_type_list = ['.jpg', '.jpeg', '.png', '.bmp']
# 音频视频格式
aud_type_list = ['.mp3', '.mp4']


class EmailUtil:
    """邮件发送工具类"""
    def __init__(self, email_host, sender, auth_code, to_recv, cc_recv, subject, text_cont = None, attach_file = None, html_cont = None, html_img = None):
        self.log = LogUtil.sys_log()

        # 设置邮箱服务器地址
        self.email_host = email_host
        # 设置发件人邮箱地址
        self.sender = sender
        # 设置发件人邮箱授权码或密码
        self.auth_code = auth_code
        # 设置收件人邮箱地址
        self.to_recv = to_recv
        # 设置抄送人邮箱地址
        self.cc_recv = cc_recv
        # 设置邮件主题
        self.subject = subject
        # 设置text正文
        self.text_cont = text_cont
        # 设置html正文
        self.html_cont = html_cont
        # 设置html背景图片
        self.html_img = html_img
        # 设置邮件附件
        self.attach_file = attach_file

    @staticmethod
    def format_addr(s):
        """ 格式化收发件人 """
        email_name, email_addr = parseaddr(s)
        return formataddr((Header(email_name,'utf-8').encode(), email_addr))

    def set_send(self, emails):
        """ 设置发件人 """
        email_name, email_addr = parseaddr(emails)
        return email_addr

    def set_recv(self, emails):
        """ 设置收件人 """
        format_list = []
        for email in emails:
            format_list.append(self.format_addr(email))
        return format_list

    def set_email(self):
        """ 设置邮件基本内容 """
        self.message['Subject'] = Header(self.subject, 'utf-8').encode()
        self.message['From'] = self.format_addr(self.sender)
        self.message['To'] = ";".join(self.set_recv(self.to_recv))
        self.message['Cc'] = ";".join(self.set_recv(self.cc_recv))

    def add_text_cont(self):
        """ 添加text正文 """
        self.message = MIMEMultipart()
        text_cont = MIMEText(self.text_cont, 'plain', 'utf-8')
        self.message.attach(text_cont)

    def add_html_cont(self):
        """ 添加html正文 """
        self.message = MIMEMultipart('related')
        html_cont = MIMEText(self.html_cont, 'html', 'utf-8')
        self.message.attach(html_cont)

        cid_list = pattern_img.findall(self.html_cont)
        if len(cid_list) > 0:
            if len(cid_list) == len(self.html_img):
                # 添加html背景图片
                for cid_img, html_img in zip(cid_list, self.html_img):
                    # 添加图片
                    html_img = open(html_img, 'rb')
                    back_img = MIMEImage(html_img.read())
                    html_img.close()
                    back_img.add_header('Content-ID', '<{}>'.format(cid_img))
                    self.message.attach(back_img)
            elif len(cid_list) != len(self.html_img):
                raise Exception('请检查html图片位置信息及所需图片信息.')

    def add_text_attach(self, text_path):
        """ 添加text附件"""
        text_name = Base.path_to_name(text_path)
        text_file = open(text_path, 'rb')
        text_attach = MIMEText(text_file.read(), 'base64', 'utf-8')
        text_file.close()
        text_attach['Content-Type'] = 'application/octet-stream'
        text_attach['Content-Disposition'] = 'attachment; filename = {}'.format(text_name)
        self.message.attach(text_attach)

    def add_html_attach(self, html_path):
        """ 添加html附件 """
        html_name = Base.path_to_name(html_path)
        html_file = open(html_path, 'rb')
        html_attach = MIMEApplication(html_file.read())
        html_file.close()
        html_attach["Content-Type"] = 'application/octet-stream'
        html_attach.add_header('content-disposition', 'attachment', filename = html_name)
        # html_attach['Content-Disposition'] = 'attachment; filename = {}'.format(html_name)
        self.message.attach(html_attach)

    def add_img_attach(self, img_path):
        """ 添加图片附件 """
        img_name = Base.path_to_name(img_path)
        img_file = open(img_path, 'rb')
        img_attach = MIMEImage(img_file.read())
        img_file.close()
        img_attach["Content-Type"]='application/octet-stream'
        img_attach["Content-Disposition"] = 'attachment; filename = {}'.format(img_name)
        self.message.attach(img_attach)

    def add_aud_attach(self, aud_path):
        """ 添加音频附件 """
        aud_name = Base.path_to_name(aud_path)
        aud_file = open(aud_path, 'rb')
        aud_attach = MIMEAudio(aud_file.read(), 'audio')
        aud_file.close()
        aud_attach["Content-Type"]='application/octet-stream'
        aud_attach["Content-Disposition"] = 'attachment; filename = {}'.format(aud_name)
        self.message.attach(aud_attach)

    def add_zip_attach(self, zip_path):
        """ 添加压缩文件附件 """
        zip_name = Base.path_to_name(zip_path)
        zip_file = open(zip_path, 'rb')
        zip_attach = MIMEText(zip_file.read(), 'base64', 'utf-8')
        zip_file.close()
        zip_attach['Content-Type'] = 'application/octet-stream'
        zip_attach.add_header('content-disposition', 'attachment', filename = zip_name)
        self.message.attach(zip_attach)

    # 增加调试信息
    @pysnooper.snoop()
    def send_email(self):
        """ 发送邮件 """
        try:
            # 连接邮件服务器 SMTP_PORT = 25
            server = smtplib.SMTP(self.email_host, smtplib.SMTP_PORT)
            self.log.info('成功连接到邮件服务器')
            # 用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息 
            # server.set_debuglevel(1) 
            # 登录邮箱服务器
            server.login(self.set_send(self.sender), self.auth_code)
            self.log.info('成功登录邮箱')
            self.log.info('发件人：[{}]'.format(self.sender))

            if not self.cc_recv:
                server.sendmail(self.sender, self.to_recv, self.message.as_string())
                self.log.info('收件人：{}'.format(self.to_recv))
            elif self.cc_recv:
                server.sendmail(self.sender, self.to_recv + self.cc_recv, self.message.as_string())
                self.log.info('收件人：{}；抄送人：{}'.format(self.to_recv, self.cc_recv))
            self.log.info('邮件发送成功')
        except smtplib.SMTPException as e:
            self.log.info('邮件发送异常：')
            self.log.info(e.args)
            self.log.info(str(e))
            self.log.info(repr(e))
        finally:
            server.quit()

if __name__ == '__main__':
    # email_host, sender, auth_code, to_recv, subject, text_cont, file, cc_recv = None
    email_info = conf_read.get_email_info()
    # print(email_info)
    email_host = email_info['email_host']
    sender = email_info['sender']
    auth_code = email_info['auth_code']
    to_recv = email_info['to_recv']
    cc_recv = email_info['cc_recv']
    subject = 'email_test'
    text_cont = 'hello everyone'
    html_cont = '''
    <p>百度官网地址：</p>
    <p><a href = 'https://www.baidu.com/'>点击进入</a></p>
    <p>Jinhu's Photo</p>
    <p>------------------------------------------------</p>
    <p><img src = 'cid:image_0'></p>
    <p>------------------------------------------------</p>
    <p><img src = 'cid:image_1'></p>
    '''
    html_img = []
    attach_files = []
    # email = EmailUtil(email_host, sender, auth_code, to_recv, cc_recv, subject, text_cont = text_cont)
    # email = EmailUtil(email_host, sender, auth_code, to_recv, cc_recv, subject, html_cont = html_cont, html_img = html_img)
    email = EmailUtil(email_host, sender, auth_code, to_recv, cc_recv, subject, html_cont = html_cont, attach_file = attach_files, html_img = html_img)

    email.send_email()

