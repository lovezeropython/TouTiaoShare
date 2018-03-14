
# -*- coding: utf-8 -*-
"""
@Time: 2018/3/13
@Author: songhao
@微信公众号: zeropython
@File: index.py
"""

import pyqrcode

qr = pyqrcode.create("https://www.168seo.cn")
# 创建 qr对象
qr.png("myQrcode.png", scale=6)
# png 方法保存为 png，scale 尺寸


from PIL import Image
import zbarlight
# 导入想对应的包

file_path = './myQrcode.png'
with open(file_path, 'rb') as image_file:
    # 二进制的形式读取图片
    image = Image.open(image_file)
    # Image 打开
    image.load()
    # 加载

codes = zbarlight.scan_codes('qrcode', image)
# scan_codes 读取二维码信息
print('QR codes: %s' % codes)
