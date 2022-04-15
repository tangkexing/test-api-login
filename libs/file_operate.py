# @Time    : 2022/1/10 20:12
# @Author  : wanglinxian
# @Email   : wanglinxian@uino.com
# @File    : file_operate.py
# @Software: PyCharm
# @Description: 文件相关操作

import urllib3


class FileOperate:
    '''
    文件下载
    method：  HTTP的方法（GET、POST、PUT、PATCH等）
    url：     文件下载的url
    filepath：文件存放的本地路径
    '''
    def file_download(self, method, url, filepath):
        http = urllib3.PoolManager()
        f = http.request(method, url)
        download_file = open(filepath, 'wb')
        download_file.write(f.data)
        f.release_conn()  # 释放HTTP连接
        download_file.close()

    '''
    删除目录下的所有文件
    filepath：目录
    '''
    def delete_all_files_in_directory(self, filepath):
        file_list = os.listdir(filepath)
        print(file_list)
        for f in file_list:
            s = os.path.join(filepath, f)
            if os.path.isfile(s):
                os.remove(s)
            elif os.path.isdir(s):
                shutil.rmtree(s, True)
