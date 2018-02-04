# -*- coding: utf-8 -*-
"""
@Time: 2018/2/4
@Author: songhao
@微信公众号: zeropython
@File: index.py
https://www.168seo.cn/python-2/3385.html
"""
"""
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
# 设置user-agent请求头
dcap["phantomjs.page.settings.loadImages"] = False  # 禁止加载图片
driver = webdriver.PhantomJS(desired_capabilities=dcap)
driver.set_page_load_timeout(40)  # 设置页面最长加载时间为40s
try:
    driver.get("https://www.168seo.cn/")
except:
    pass
driver.get_screenshot_as_file('01.png')  # 保存网页截图
driver.quit()  # 退出浏览器



from selenium import webdriver

options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values': {
        'images': 2
    }
}
options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(chrome_options=options)

# browser = webdriver.Chrome()
url = "https://www.168seo.cn/"
browser.get(url)

browser.quit()
"""
import time
from selenium import webdriver
# 进入浏览器设置
options = webdriver.ChromeOptions()
# 设置中文
options.add_argument('lang=zh_CN.UTF-8')
# 更换头部
options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
browser = webdriver.Chrome(chrome_options=options)
url = "https://httpbin.org/get?show_env=1"
browser.get(url)
time.sleep(10)
browser.quit()