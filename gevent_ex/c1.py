import gevent.monkey
gevent.monkey.patch_socket()

import gevent
import requests
import simplejson as json

def fetch(pid):
    response = requests.get('http://json-time.appspot.com/time.json')
    result = response.text
    json_result = json.loads(result)
    datetime = json_result['datetime']

    print('Process %s: %s' % (pid, datetime))
    return json_result['datetime']

def synchronous():
    for i in range(1,10):
        fetch(i)

def asynchronous():
    threads = []
    for i in range(1,10):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)

print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()

"""
链接: https://pan.baidu.com/s/1dFZv5gH 密码: rcg6
"""