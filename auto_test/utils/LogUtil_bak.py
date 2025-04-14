# 封装Log工具类
import logging
import datetime, os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Conf
from config.Conf import ConfigYaml

# 定义日志级别的映射
log_l = {
    'info': logging.INFO,
    'debug': logging.DEBUG,
    'warn': logging.WARNING,
    'error': logging.ERROR,
}

# 创建类
class LogUtil:
# 定义参数
    # 输出文件名称，Loggername，日志级别
    def __init__(self, log_file, log_name, log_level):
        self.log_file = log_file
        self.log_name = log_name
        self.log_level = log_level

# 输出控制台或文件
        # 设置logger名称
        self.logger = logging.getLogger(self.log_name)

        # 设置log级别
        self.logger.setLevel(log_l[self.log_level])

        # 判断handler是否存在
        if not self.logger.handlers:
            # 定义日志格式
            formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')

            # 日志打印
            fh_stream = logging.StreamHandler()
            fh_stream.setLevel(log_l[self.log_level])
            fh_stream.setFormatter(formatter)

            # 写入文件
            fh_file = logging.FileHandler(self.log_file)
            fh_file.setLevel(log_l[self.log_level])
            fh_file.setFormatter(formatter)

            # 添加handler
            self.logger.addHandler(fh_stream)
            self.logger.addHandler(fh_file)


# 1、初始化参数数据
# 日志文件名称、日志文件级别
# 日志文件名称 = logs目录 + 当前时间 + 扩展名
# logs目录
logs_path = Conf.get_log_path()
# 当前时间
cur_time = datetime.datetime.now().strftime('%Y-%m-%d')
# 扩展名
log_extension = ConfigYaml().get_conf_log_extension()
# logfile = os.path.join(logs_path, cur_time + log_extension)
# print(logfile)
# 日志名称默认包含当前文件名
file_name=os.path.basename(__file__).split(".")[0]
# print(name)
# 日志文件级别
loglevel = ConfigYaml().get_conf_log_level()
# print(loglevel)

def sys_log(log_name = file_name):
    logspath = os.path.join(logs_path, log_name)
    # logspath_daily = os.path.join(logspath, log_name + '-' + cur_time)
    if not os.path.exists(logspath):
        os.makedirs(logspath)
    logfile = os.path.join(logspath, log_name + '-' + cur_time + log_extension)
    return LogUtil(log_file = logfile, log_name = log_name, log_level = loglevel).logger


if __name__ == '__main__':
    # sys_log().debug('this is a debug')
    log = sys_log()
    log.info('this is a info')
    log.debug('this is a debug')
    log.warning('this is a warning')
    log.error('this is a error')