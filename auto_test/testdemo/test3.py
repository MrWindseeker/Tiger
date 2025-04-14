import logging, datetime, os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Conf
from config.Conf import ConfigYaml


# 创建类
class LogUtil:
    """日志工具类，用于创建和配置日志记录器"""
    # 日志名称默认包含当前文件名
    _File_Name = os.path.basename(__file__).split(".")[0]

    # 日志格式默认
    # _Default_Format = '%(asctime)s [%(levelname)s] %(message)s'

    _Default_Format = '%(asctime)s [%(levelname)s] %(name)s:%(lineno)d - %(message)s'

    # 定义日志级别的映射
    _Log_Level_Map = {
        'info': logging.INFO,
        'debug': logging.DEBUG,
        'warn': logging.WARNING,
        'error': logging.ERROR,
    }

    def __init__(self, logger):
        """最小化初始化，仅存储logger实例"""
        self.logger = logger

    def _create_handler(handler_class, level, formatter, **kwargs):
        """创建处理器"""
        handler = handler_class(**kwargs)
        handler.setLevel(level)
        handler.setFormatter(formatter)

        return handler
    
    def _log_path(log_name = _File_Name):
        """生成日志文件路径"""
        config = ConfigYaml()
        logs_dir = Conf.get_log_path()
        cur_date = datetime.datetime.now().strftime('%Y-%m-%d')
        log_extension = config.get_conf_log_extension()
        log_file = os.path.join(logs_dir, log_name)

        if not os.path.exists(log_file):
            os.makedirs(log_file)
        log_path = os.path.join(log_file, log_name + '-' + cur_date + log_extension)
        
        return log_path

    @classmethod
    def _create_logger(cls, log_name, log_level):
        """核心方法：创建并配置logger实例"""
        # 获取logger实例
        logger = logging.getLogger(log_name)
        logger.setLevel(cls._Log_Level_Map[log_level])

        # 避免重复添加处理器
        if not logger.handlers:
            # 定义日志格式
            formatter = logging.Formatter(cls._Default_Format)

            # 创建处理器
            console_handler = cls._create_handler(
                logging.StreamHandler,
                cls._Log_Level_Map[log_level],
                formatter
            )
            file_handler = cls._create_handler(
                logging.FileHandler,
                cls._Log_Level_Map[log_level],
                formatter,
                filename = cls._log_path(log_name)
            )

            # 添加处理器
            logger.addHandler(console_handler)
            logger.addHandler(file_handler)

        return logger
    
    @classmethod
    def sys_log(cls, log_name = _File_Name):
        """主入口：获取日志工具实例"""

        # 获取配置
        config = ConfigYaml()
        log_level = config.get_conf_log_level()

        # 创建logger实例
        logger = cls._create_logger(log_name, log_level)
        
        return cls(logger)
    
    def __getattr__(self, name):
        """委托logger的方法调用"""
        return getattr(self.logger, name)

    
if __name__ == '__main__':
    # 使用示例
    log_util = LogUtil.sys_log()
    log_util.info('优化后的日志信息')
    log_util.debug('调试信息')