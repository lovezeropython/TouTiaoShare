
导入用到的模块


```python
import os
import shutil
```

获取当前目录


```python
os.getcwd()
```




    '/Users/songhao/py/TouTiaoShare/os_shutil'



返回指定目录下的文件和目录


```python
os.listdir("/Users/songhao/py/TouTiaoShare/")
```




    ['trip模块.py',
     'tqdm_process.py',
     'pre_table.py',
     'Requests session wordpress',
     'Apple_app',
     'crawl_word.py',
     'scrapy_pipelines.py',
     'name_main.py',
     'zeropython',
     'superclass.py',
     'bilibili',
     'mail_python',
     'send_messages.py',
     'get_youdao_world',
     'exe.py',
     'read and wirte csv data',
     'Python_send_message_attach.py',
     '装饰器.py',
     'gevent实例',
     'xunlei.py',
     'README.md',
     'Python_table',
     'asks',
     'read_json',
     'pdfwiter.py',
     'mac_app.py',
     'args_kwargs.py',
     'paramiko上传资料.py',
     'get_baidu_real_url.py',
     'selenium_headless',
     'tuto1.pdf',
     'scrapy login',
     'read_big_file',
     'inspect模块.py',
     '多线程执行函数的两种方式',
     'sysc_wordpress.py',
     '.git',
     'os_shutil',
     '手写一个迭代器.py',
     'jincheng.py',
     'ajax',
     'Requests_Gevent.py',
     '.idea',
     '装饰器']



检验一个文件是否是目录，是否是文件


```python
os.path.isfile('/Users/songhao/py/TouTiaoShare/sysc_wordpress.py')
```




    True




```python
os.path.isfile('/Users/songhao/py/TouTiaoShare')
```




    False




```python
os.path.isdir('/Users/songhao/py/TouTiaoShare')
```




    True



检测路径是否是真的存在


```python
os.path.exists("/Users/songhao/py/TouTiaoShare")
```




    True




```python
os.path.exists("/Users/songhao/py/TouTiaoShar]e")
```




    False



分离一个路径的目录和名称


```python
os.path.split("/Users/songhao/py/TouTiaoShare/sysc_wordpress.py")
```




    ('/Users/songhao/py/TouTiaoShare', 'sysc_wordpress.py')



获取路径名称


```python
os.path.dirname("/Users/songhao/py/TouTiaoShare/sysc_wordpress.py")
```




    '/Users/songhao/py/TouTiaoShare'



获取文件名称


```python
os.path.basename("/Users/songhao/py/TouTiaoShare/sysc_wordpress.py")
```




    'sysc_wordpress.py'



重命名文件名称或者目录


```python
os.rename("/Users/songhao/py/TouTiaoShare/sysc_wordpress1.py",'/Users/songhao/py/TouTiaoShare/sysc_wordpress2.py')
```


```python
ls "/Users/songhao/py/TouTiaoShare/"|grep "sysc_wordpress"
```

    sysc_wordpress2.py


创建多级目录


```python
os.makedirs('/Users/songhao/py/TouTiaoShare/1/2/3')
```


```python
ls "/Users/songhao/py/TouTiaoShare/1/"
```

    [1m[36m2[m[m/


获取文件属性


```python
os.stat("/Users/songhao/py/TouTiaoShare/sysc_wordpress2.py")
```




    os.stat_result(st_mode=33188, st_ino=8603417960, st_dev=16777220, st_nlink=1, st_uid=501, st_gid=20, st_size=394, st_atime=1517298214, st_mtime=1516705471, st_ctime=1517298212)



获取文件的大小


```python
os.path.getsize("/Users/songhao/py/TouTiaoShare/sysc_wordpress2.py")
```




    394



复制文件夹


```python
shutil.copytree("/Users/songhao/py/TouTiaoShare/","/Users/songhao/py/TouTiaoShare1/") # 两个都只能是目录，且生成的目录原来不能存在
```




    '/Users/songhao/py/TouTiaoShare1/'




```python
ls "/Users/songhao/py/"|grep "TouTiaoShar"
```

    TouTiaoShare/
    TouTiaoShare1/


复制文件 要复制的文件必须是文件，新生成的可以是目标目录，也可以是目标文件


```python
shutil.copyfile("/Users/songhao/py/TouTiaoShare/sysc_wordpress2.py","/Users/songhao/py/TouTiaoShare/sysc_wordpress3.py")
```




    '/Users/songhao/py/TouTiaoShare/sysc_wordpress3.py'



移动文件


```python
shutil.move("/Users/songhao/py/TouTiaoShare/sysc_wordpress3.py","/Users/songhao/py/TouTiaoShare/sysc_wordpress4.py")
```




    '/Users/songhao/py/TouTiaoShare/sysc_wordpress4.py'




```python
ls "/Users/songhao/py/TouTiaoShare/"|grep "sysc_wordpress"
```

    sysc_wordpress2.py
    sysc_wordpress4.py


删除目录


```python
os.rmdir("/Users/songhao/py/TouTiaoShare/1/") # 只能删除 空白目录
```


    ---------------------------------------------------------------------------

    OSError                                   Traceback (most recent call last)

    <ipython-input-35-8f41e372260b> in <module>()
    ----> 1 os.rmdir("/Users/songhao/py/TouTiaoShare/1/")
    

    OSError: [Errno 66] Directory not empty: '/Users/songhao/py/TouTiaoShare/1/'


shutil.rmtree这个就很强大了，是不是空目录都是可以删除的


```python
shutil.rmtree("/Users/songhao/py/TouTiaoShare/1/")
```


```python
ls "/Users/songhao/py/TouTiaoShare/1"
```

    ls: /Users/songhao/py/TouTiaoShare/1: No such file or directory



```python

```
