# -*- coding: utf-8 -*-
"""
@Time: 2018/3/12
@Author: songhao
@微信公众号: zeropython
@File: index.py
"""
import pip
from subprocess import call
# 导入包
for dist in pip.get_installed_distributions():
    call("sudo -H pip3 install --upgrade " + dist.project_name, shell=True)
    #  一定要sudo -H 在Mac Linux 下，不然部分 会没有权限

