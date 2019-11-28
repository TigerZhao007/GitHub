# -*- coding: utf-8 -*-
"""
时间：2019-10-13
作者: zuoshao（佐少）
代码说明：爬虫_浏览器操作
"""

# 如何配置Headless Chrome~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import requests
import time

# 设置桌面路径~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_desktop():
    import winreg
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    desktop_path = winreg.QueryValueEx(key, "Desktop")[0]
    return desktop_path

# 新加存储路径~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def mkdir(path):

    import os    # 引入模块

    path = path.strip()  # 去除首位空格
    path = path.rstrip("\\")  # 去除尾部 \ 符号
    isExists = os.path.exists(path)  # 判断路径是否存在, 存在-True, 不存在-False

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录, 创建目录操作函数
        os.makedirs(path)

        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False

# 定义要创建的目录
path = get_desktop()
mkpath = path + '\\王者荣耀壁纸'

# 调用函数
mkdir(mkpath)
os.chdir(mkpath)

# ######################################################################################################################
# 网页爬虫，
# ######################################################################################################################
driver = webdriver.PhantomJS(executable_path="phantomjs.exe")
driver.maximize_window()
url = 'http://pvp.qq.com/'
driver.get(url)
moveElement = driver.find_element_by_xpath('//a[@title="游戏资料"]')
ActionChains(driver).move_to_element(moveElement).perform()
driver.find_element_by_xpath('//a[@title="游戏壁纸"]').click()

all_h = driver.window_handles
driver.switch_to.window(all_h[1])

time.sleep(3)

page_num = 0

while page_num < 15:
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    Lists = soup.find_all('div', {'class': 'p_newhero_item'})
    titleLists = []
    hrefLists = []
    for item in Lists:
        subSoup = BeautifulSoup(str(item), 'html.parser')
        titleList = subSoup.find('h4')
        titleLists.append(titleList.text)
        linkList = subSoup.find('li', {'class': 'sProdImgL6'})
        soup = BeautifulSoup(str(linkList), 'html.parser')
        a = soup.find('a')
        hrefLists.append(a['href'])

    for i in range(len(titleLists)):
        url = hrefLists[i]
        r = requests.get(url).content
        path = titleLists[i] + '.jpg'
        try:
            with open(path, 'wb') as f:
                f.write(r)
                print('保存成功 %s.jpg' % titleLists[i])
        except:
            print('保存失败')
    driver.find_element_by_xpath('//a[@class="downpage"]').click()

    time.sleep(3)
    page_num = page_num + 1

driver.close()