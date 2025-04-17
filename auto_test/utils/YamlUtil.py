import os
import yaml

class YamlUtil:
    """ YAML文件工具类 """
    def __init__(self, yaml_path):
        """ 初始化YAML文件工具类 """
        if not os.path.exists(yaml_path):
            raise FileNotFoundError('文件不存在')
        self.yaml_path = yaml_path
        self._data = None
        self._data_all = None

    # 读取单个文档
    def data(self):
        """ 读取单个文档 """
        if not self._data:
            with open(self.yaml_path, 'rb') as f:
                self._data = yaml.safe_load(f)
        return self._data

    # 读取多个文档
    def data_all(self):
        """ 读取多个文档 """
        if not self._data_all:
            with open(self.yaml_path, 'rb') as f:
                self._data_all = list(yaml.safe_load_all(f))
        return self._data_all