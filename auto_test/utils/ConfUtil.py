import os
import configparser


class ConfUtil:
    """ 配置文件工具类，支持读取配置并获取特定值 """
    def __init__(self, conf_path: str):
        if not os.path.isfile(conf_path):
            raise FileNotFoundError('配置文件不存在: {}'.format(conf_path))
        self.conf_path = conf_path
        self._config = None

    def _load_config(self):
        if self._config is None:
            self._config = configparser.ConfigParser()
            self._config.read(self.conf_path, encoding='utf-8')

    def get_data(self, section: str, key: str) -> str:
        self._load_config()
        try:
            return self._config.get(section, key)
        except (configparser.NoSectionError, configparser.NoOptionError) as e:
            raise KeyError('读取配置出错: {}'.format(e))

    def get_section(self, section: str) -> dict:
        self._load_config()
        if section not in self._config:
            raise KeyError('配置中不存在 section: {}'.format(section))
        return dict(self._config[section])


if __name__ == '__main__':
    import sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    from config import Tiger_Conf

    conf_path = Tiger_Conf.get_tim_elem_file()
    test_conf = ConfUtil(conf_path)
    try:
        test_data = test_conf.get_data('Look_Up', 'Time_Type_input')
        print(f"Time_Type_input: {test_data}")
    except KeyError as e:
        print(e)