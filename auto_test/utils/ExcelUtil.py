import os, xlrd2, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Conf

class ExcelUtil:
    """Excel工具类：读取指定 Excel 表格并解析为字典列表"""
    
    def __init__(self, excel_name, sheet_by):
        self.excel_file = os.path.join(Conf.get_data_path(), excel_name)
        if not os.path.exists(self.excel_file):
            raise FileNotFoundError(f"文件不存在: {self.excel_file}")
        if not isinstance(sheet_by, (str, int)):
            raise TypeError("sheet_by 参数必须为 str 或 int 类型")
        self.sheet_by = sheet_by
        self._data_list = None

    def data_list(self):
        """读取 Excel 数据并返回为字典列表"""
        if self._data_list is not None:
            return self._data_list

        workbook = xlrd2.open_workbook(self.excel_file)
        sheet = (
            workbook.sheet_by_index(self.sheet_by)
            if isinstance(self.sheet_by, int)
            else workbook.sheet_by_name(self.sheet_by)
        )

        headers = sheet.row_values(0)
        self._data_list = [
            dict(zip(headers, sheet.row_values(row_idx)))
            for row_idx in range(1, sheet.nrows)
        ]
        return self._data_list

if __name__ == '__main__':
    # excel_file = Conf.get_data_path() + os.sep + 'test_data.xlsx'
    # print(excel_file)
    data_excel = ExcelUtil('test_data.xlsx', '测试用户_1')
    data_list = data_excel.data_list()
    # print(data_list)

    all_data = []
    for data in data_list:
        all_data.append(data)
    
    print(data_list)
