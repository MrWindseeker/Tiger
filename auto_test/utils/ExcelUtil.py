import os, xlrd2, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Conf

class ExcelUtil:
    """ Excel工具类 """
    def __init__(self, excel_name, sheet_by):
        """ 初始化Excel工具类 """
        excel_file = Conf.get_data_path() + os.sep + excel_name
        if os.path.exists(excel_file):
            self.excel_file = excel_file
        else:
            raise FileNotFoundError('文件不存在')
        self.sheet_by = sheet_by
        self._data_list = []


    def data_list(self):
        """ 读取Excel数据 """
        # data数据存在则不读取
        if not self._data_list:
            workbook = xlrd2.open_workbook(self.excel_file)
            if type(self.sheet_by) not in [str, int]:
                raise TypeError('Please input str or int!')
            elif type(self.sheet_by) == int:
                sheet = workbook.sheet_by_index(self.sheet_by)
            elif type(self.sheet_by) == str:
                sheet = workbook.sheet_by_name(self.sheet_by)

        # 读取sheet内容
        # 返回list，元素：字典
        # 格式：[{'a':'a1','b':'b1'},{'a':'a2','b':'b2'}]
        # 获取首行信息
            data_title = sheet.row_values(0)
            # 循环遍历测试行，过滤首行，从1开始
            for ele_r in range(1, sheet.nrows):
                ele_r_val = sheet.row_values(ele_r)
                # 与首行组成dict，放入list
                self._data_list.append(dict(zip(data_title, ele_r_val)))

            return self._data_list

if __name__ == '__main__':
    # excel_file = Conf.get_data_path() + os.sep + 'test_data.xlsx'
    # print(excel_file)
    data_excel = ExcelUtil('test_data.xlsx', '接口测试用例_1')
    data_list = data_excel.data_list()
    # print(data_list)

    all_data = []
    for data in data_list:
        all_data.append(data)
    
    print(data_list)
