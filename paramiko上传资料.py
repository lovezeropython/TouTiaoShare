# -*- coding: utf-8 -*-
"""
@Time: 2018/1/22
@Author: songhao
@微信公众号: zeropython
@File: paramiko上传资料.py
"""
# 导入用到的模块
import paramiko, os
import datetime

hostname = '123.56.76.1'
username = 'root'
password = 'mima'
port = 22
# 当前电脑主机要上传的文件夹
local_dir = 'C:/Users/admin/Desktop/list/'

# 注意 一定要加 /； 上传的是这个文件下的所有文件
#远程的文件夹
remote_dir = '/tem/p/'
if __name__ == "__main__":
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    # 与服务器进行连接
    files = os.listdir(local_dir)

for f in files:
    print('#########################################')
    print('Beginning to upload file %s ' % datetime.datetime.now())

    print('Uploading file:', os.path.join(local_dir, f))
    # 开始上传
    sftp.put(os.path.join(local_dir, f), os.path.join(remote_dir, f))

    print('Upload file success %s ' % datetime.datetime.now())

    t.close()
    # 关闭连接