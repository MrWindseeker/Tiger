# 封装Log工具类
import logging
import datetime
import os
import sys
import inspect
from typing import Optional, Dict

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Conf
from config.Conf import ConfigYaml

# 定义日志级别的映射
LOG_LEVEL_MAP: Dict[str, int] = {
    'info': logging.INFO,
    'debug': logging.DEBUG,
    'warn': logging.WARNING,
    'error': logging.ERROR,
}

class LogUtil:
    """日志工具类，用于创建和配置日志记录器"""
    
    def __init__(self, logger: logging.Logger):
        """
        最小化初始化，仅存储logger实例
        :param logger: 配置好的logging.Logger实例
        """
        self.logger = logger

    @classmethod
    def _validate_log_level(cls, level: str) -> str:
        """统一校验日志级别"""
        level = level.lower()
        if level not in LOG_LEVEL_MAP:
            sys.stderr.write(f"Invalid log level '{level}', defaulting to 'info'\n")
            return 'info'
        return level

    @classmethod
    def _create_logger(cls, log_name: str, log_level: str) -> logging.Logger:
        """核心方法：创建并配置logger实例"""
        # 参数校验
        valid_level = cls._validate_log_level(log_level)
        
        # 获取logger实例
        logger = logging.getLogger(log_name)
        logger.setLevel(LOG_LEVEL_MAP[valid_level])

        # 避免重复添加处理器
        if not logger.handlers:
            # 定义日志格式
            formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')

            # 创建处理器
            console_handler = cls._create_handler(
                logging.StreamHandler,
                LOG_LEVEL_MAP[valid_level],
                formatter
            )
            file_handler = cls._create_handler(
                logging.FileHandler,
                LOG_LEVEL_MAP[valid_level],
                formatter,
                filename=cls._generate_log_path(log_name),
                encoding='utf-8'
            )

            # 添加处理器
            logger.addHandler(console_handler)
            logger.addHandler(file_handler)

        return logger

    @staticmethod
    def _create_handler(handler_class: type, level: int, formatter: logging.Formatter, **kwargs) -> logging.Handler:
        """创建处理器"""
        handler = handler_class(**kwargs)
        handler.setLevel(level)
        handler.setFormatter(formatter)
        return handler

    @staticmethod
    def _generate_log_path(log_name: str) -> str:
        """生成日志文件路径"""
        config = ConfigYaml()
        logs_dir = Conf.get_log_path()
        cur_date = datetime.datetime.now().strftime('%Y-%m-%d')
        log_extension = config.get_conf_log_extension()
        
        # 创建模块日志目录
        module_log_dir = os.path.join(logs_dir, log_name)
        os.makedirs(module_log_dir, exist_ok=True)
        
        return os.path.join(
            module_log_dir,
            f"{log_name}-{cur_date}{log_extension}"
        )

    @classmethod
    def get_logger(cls, log_name: Optional[str] = None) -> 'LogUtil':
        """主入口：获取日志工具实例"""
        # 自动获取调用模块名称
        if log_name is None:
            frame = inspect.stack()[1]
            module = inspect.getmodule(frame[0])
            log_name = module.__name__ if module else "default_logger"

        # 获取配置
        config = ConfigYaml()
        log_level = cls._validate_log_level(config.get_conf_log_level())

        # 创建logger实例
        logger = cls._create_logger(log_name, log_level)
        
        return cls(logger)

    def __getattr__(self, name):
        """委托logger的方法调用"""
        return getattr(self.logger, name)

if __name__ == '__main__':
    # 使用示例
    log_util = LogUtil.get_logger()
    log_util.info('优化后的日志信息')
    log_util.debug('调试信息')
    
    # 直接使用logger方法
    logger = log_util.logger
    logger.warning('传统方式记录警告')