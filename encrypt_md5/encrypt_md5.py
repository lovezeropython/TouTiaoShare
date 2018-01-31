# -*- coding: utf-8 -*-
"""
@Time: 2018/1/31
@Author: songhao
@微信公众号: zeropython
@File: encrypt_md5.py
@ website: https://www.168seo.cn/python/24387.html
"""

import hashlib
"""
Python 内置的 hashlib 模块提供了常见的摘要算法（或称哈希算法，散列算法），如 MD5，SHA1, SHA256 等。
摘要算法的基本原理是：将数据（如一段文字）运算变为另一固定长度值。

MD5 (Message-Digest Algorithm 5, 消息摘要算法），是一种被广泛使用的密码散列函数，可以产生出一个 128 位（16 字节）的散列值（hash value），用于确保信息传输完整一致。
SHA1 (Secure Hash Algorithm, 安全哈希算法) 是 SHA 家族的其中一个算法，它经常被用作数字签名。
"""
# 参数必须是byte类型，否则报Unicode-objects must be encoded before hashing错误

src = 'My test string'.encode('utf-8')
# 生成一个对象
myMd5 = hashlib.md5()

# 传入需要加密的字符串进行MD5加密
myMd5.update(src)

# 就可以获取到经过MD5加密的字符串了
myMd5_Digest = myMd5.hexdigest()

# sha1 加密和 md5加密只是算法不一样

mySha1 = hashlib.sha1()
mySha1.update(src)
mySha1_Digest = mySha1.hexdigest()

print('source string: ', src)

print("www.168seo.cn".center(30,"_"))
print('MD5: ', myMd5_Digest)
print('SHA1: ', mySha1_Digest)

