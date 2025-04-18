import os, datetime, shutil
from utils.LogUtil import LogUtil


class ZipUtil:
    """ 封装压缩工具类 """
    def __init__(self):
        """ 初始化ZipUtil类 """
        self.log = LogUtil.sys_log()

    def zip_files(self, output_path, output_name, file_path = None, folder_path = None):
        """ 压缩文件或文件夹 """
        if not file_path and not folder_path:
            raise ValueError('至少提供一个文件或文件夹路径！')

        cur_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        base_output_path = os.path.join(output_path, '{}_{}'.format(output_name, cur_time))
        zip_output_path = self._get_unique_output_path(base_output_path)

        temp_folder = zip_output_path + "_temp"
        os.makedirs(temp_folder)
        try:
            if file_path:
                if not os.path.exists(file_path):
                    raise FileNotFoundError('文件路径不存在：{}'.format(file_path))
                self.log.info('复制文件 {} 到临时目录'.format(file_path))
                shutil.copy2(file_path, temp_folder)

            if folder_path:
                if not os.path.exists(folder_path):
                    raise FileNotFoundError('文件夹路径不存在：{}'.format(folder_path))
                dest_path = os.path.join(temp_folder, os.path.basename(folder_path))
                self.log.info('复制文件夹 {} 到临时目录 {}'.format(folder_path, dest_path))
                shutil.copytree(folder_path, dest_path)

            self.log.info('开始压缩目录 {} 到 {}.zip'.format(temp_folder, zip_output_path))
            shutil.make_archive(zip_output_path, 'zip', temp_folder)
        finally:
            self.log.info('删除临时目录 {}'.format(temp_folder))
            shutil.rmtree(temp_folder)

    def _get_unique_output_path(self, base_path):
        if not os.path.exists(base_path + '.zip'):
            return base_path
        count = 1
        while os.path.exists('{}_{}.zip'.format(base_path, count)):
            count += 1
        return '{}_{}'.format(base_path, count)