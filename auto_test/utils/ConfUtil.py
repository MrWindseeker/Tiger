import os, configparser

class ConfUtil:
    def __init__(self, conf):
        if os.path.exists(conf):
            self.conf = conf
        else:
            raise FileNotFoundError('文件不存在')

    def read_conf(self):
        conf_data = configparser.ConfigParser()
        conf_data.read(self.conf, encoding='utf8')
        return conf_data
    
    def get_data(self, section, key):
        return self.read_conf()[section][key]
    
if __name__ == '__main__':
    conf_path = 'D:\\Python\\Tiger\\auto_test\\config\\tim_elem.conf'
    test_conf = ConfUtil(conf_path)
    # print(test_conf.read_conf().get('test_case', 'case_id'))
    # test_data = test_conf.read_conf()
    # test_data = test_data['test_case']['case_id']
    test_data = test_conf.get_data('Look_Up', 'Time_Type_input')
    print(test_data)