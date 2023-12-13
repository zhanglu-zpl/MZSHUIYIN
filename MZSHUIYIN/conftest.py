#!/user/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @File : conftest.py
# @Time : 2022-03-03 15:34
# @Author : mojin
# @Email : 397135766@qq.com
# @Software : PyCharm
#-------------------------------------------------------------------------------

import json

import requests
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
#import time
#from webdriver_manager.chrome import ChromeDriverManager
import pytest

#import allure
#from selenium import webdriver
#from common.logger import Logger
#from common.screen_recordings import RecordScreen
'''
@pytest.fixture(scope="function", autouse=True)
def screencap():
    now = time.strftime("%y%m%d%H%M%S", time.localtime())
    images_path = f'./images/{now}.mp4'
    SR = RecordScreen(images_path=images_path)
    #SR.start()

    yield

    SR.stop()

    allure.attach.file(images_path, name='录屏',attachment_type=allure.attachment_type.MP4)  # 测试步骤中添加一张图片或视频

#session 是多个文件调用一次，可以跨.py文件调用，每个.py文件就是module
#function 每个测试函数运行前后都会创建和销毁的一个夹具。
#class 测试类内部共享夹具实例。
#module 测试模块内共享夹具实例
# 声明使用request测试固件

'''
@pytest.fixture(scope="function")
def driver1():
    ### 下面是chromedriver路径，自己填
    browser = uc.ChromeOptions()
    browser.add_experimental_option("prefs", {"credentials_enable_service": False,
                                              "profile.password_manager_enabled": False})
    driver = uc.Chrome(options=browser)
    ### 打开要自动登录的网站
    driver.get("https://meizhe.meideng.net")
    #with open('../MZSHUIYIN/cookies.txt', 'r', encoding='utf8') as f:
    with open('C:/Users/shyc/.jenkins/workspace/meizhecuxiao/MZSHUIYIN/cookies.txt', 'r', encoding='utf8') as f:
        listCookies = json.loads(f.read())
    for cookie in listCookies:
        cookie_dict = {
            ### 这个domain看cookies第一个字段就知道了，需要找到并填入
            'domain': '.meideng.net',
            "expires": cookie.get('expires'),
            'httpOnly': cookie.get('httpOnly'),
            'name': cookie.get('name'),
            'path': '/',
            'sameSite': cookie.get('sameSite'),
            'value': cookie.get('value'),
            'secure': cookie.get('secure')
        }
        driver.add_cookie(cookie_dict)
        # browser.refresh()  # 刷新网页,cookies才成功
    driver.get("https://meizhe.meideng.net")
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, '/html/body/div[9]/ko-modal-global-adv/div/div/div/div/div/button').click()
    #driver.implicitly_wait(3)
    #driver.find_elements(by=By.CSS_SELECTOR, value='ul.p7kswUBL > li')[0].click()
    yield driver
    '''
    driver.find_element(By.XPATH, '//*[@id="nav-sidebar"]/div/div[2]/div/div/div/div[1]').click()
    driver.implicitly_wait(3)
    d = driver.find_elements(by=By.CSS_SELECTOR, value='div.activity-action-main > div > a.mz-btn.btn-bordered.btn-default')[0]
    d.click()
    driver.implicitly_wait(3)
    driver.find_element(by=By.XPATH, value='/html/body/div[14]/div[2]/div/div/div[2]/div/div/div[2]/button[2]').click()
    driver.implicitly_wait(3)
    '''

    driver.close()


