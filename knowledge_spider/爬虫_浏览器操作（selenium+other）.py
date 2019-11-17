# -*- coding: utf-8 -*-
"""
时间：2019-10-13
作者: zuoshao（佐少）
代码说明：爬虫_浏览器操作
"""

# ######################################################################################################################
# Headless Chrome
# ######################################################################################################################
# https://blog.csdn.net/u010358168/article/details/79749149

# 如何配置Headless Chrome~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
准备工具：
- python3.6, selenium, PhantomJS 安装selenium：
- pip install selenium
前提条件：
- 本地安装Chrome浏览器
- 本地需要chromedriver驱动器文件，如果不配置环境变量的话，需要手动指定executable_path参数。
https://sites.google.com/a/chromium.org/chromedriver/home
将phantomjs.exe解压到python的script文件夹下。
'''

# 如何使用Headless Chrome~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
br = webdriver.Chrome(chrome_options=chrome_options)
br.get('https://www.baidu.com/')
baidu = br.find_element_by_id('su').get_attribute('value')
print(baidu)


# ######################################################################################################################
# Headless Firefox
# ######################################################################################################################

# 如何配置Headless Firefox~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
准备工具：
- python3.6, selenium, PhantomJS 安装selenium：
- pip install selenium
前提条件：
- 本地安装Firefox浏览器
- 本地需要geckodriver驱动器文件，如果不配置环境变量的话，需要手动指定executable_path参数。
https://github.com/mozilla/geckodriver/releases/
将phantomjs.exe解压到python的script文件夹下。
'''

# 如何使用Headless Firefox~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

def main():
    options = Options()
    options.add_argument('-headless')
    # driver = Firefox(executable_path='./geckodriver', firefox_options=options)
    driver = Firefox(firefox_options=options)
    driver.get("https://www.qiushibaike.com/8hr/page/1/")
    print(driver.page_source)
    driver.close()


if __name__ == '__main__':
    main()



