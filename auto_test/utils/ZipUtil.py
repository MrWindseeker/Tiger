import os, datetime, shutil
from utils.LogUtil import LogUtil


# 当前时间
cur_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

class ZipUtil:
    def __init__(self):
        self.log = LogUtil.sys_log('ZipUtil')

    def zip_files(self, output_path, output_name, file_path = None, folder_path = None):
        if not file_path and not folder_path:
            raise Exception('至少提供一个文件或文件夹路径！')
            
        # 构建完整的输出路径
        output_path = os.path.join(output_path, output_name + '_' + cur_time)

        # 检查输出文件名是否已存在
        if os.path.exists(output_path + '.zip'):
            # 如果存在，则添加序号
            count = 1
            while os.path.exists(output_path + "_" + str(count)):
                count += 1
            output_path = output_path + "_" + str(count)
        
        # 创建临时文件夹
        temp_folder = output_path + "_temp"
        os.makedirs(temp_folder)    
        try:
            # 复制文件到临时文件夹
            shutil.copy2(file_path, temp_folder)        
            # 复制文件夹到临时文件夹
            shutil.copytree(folder_path, os.path.join(temp_folder, os.path.basename(folder_path)))        
            # 压缩临时文件夹
            shutil.make_archive(output_path, 'zip', temp_folder)
        finally:
            # 删除临时文件夹及其内容
            shutil.rmtree(temp_folder)