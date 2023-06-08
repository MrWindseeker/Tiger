import os
import yaml

class YamlUtil:
    def __init__(self, yaml):
        if os.path.exists(yaml):
            self.yaml = yaml
        else:
            raise FileNotFoundError('文件不存在')
        self._data = None
        self._data_all = None

    # 读取单个文档
    def data(self):
        if not self._data:
            with open(self.yaml, 'rb') as f:
                self._data = yaml.safe_load(f)
        return self._data

    # 读取多个文档
    def data_all(self):
        if not self._data_all:
            with open(self.yaml, 'rb') as f:
                self._data_all = list(yaml.safe_load_all(f))
        return self._data_all