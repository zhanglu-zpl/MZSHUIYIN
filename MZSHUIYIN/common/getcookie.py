import os
from selenium.webdriver.common.by import By
import json
import undetected_chromedriver as uc

class getcookie():
    ### 下面是chromedriver路径，自己填
    browser = uc.ChromeOptions()
    browser.add_experimental_option("prefs", {"credentials_enable_service": False,"profile.password_manager_enabled": False})
    driver = uc.Chrome(options=browser)
    ### 打开要自动登录的网站，比如说csdn
    driver.get("https://meizhe.meideng.net")
    ###登录操作
    driver.find_element(By.XPATH, '//*[@id="loginPage"]/div/div[2]/div/div/div/div/div[4]/a').click()
    frame = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/iframe')
    driver.switch_to.frame(frame)
    driver.find_element(By.XPATH, '//*[@id="fm-login-id"]').send_keys('寒茜璐')
    driver.find_element(By.XPATH, '//*[@id="fm-login-password"]').send_keys('23127zhanglu222')
    driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/div[4]/button').click()
    driver.implicitly_wait(20)
    driver.find_element(By.XPATH, '//*[@id="component_navbar"]/nav/div/div[2]/ul[1]/li[2]/a/span')
    dictCookies = driver.get_cookies()
    jsonCookies = json.dumps(dictCookies)
    with open('C:/Users/shyc/.jenkins/workspace/meizhecuxiao/MZSHUIYIN/cookies.txt', 'w') as f:
    #with open('../MZSHUIYIN/cookies.txt', 'w') as f:
        f.write(jsonCookies)
        f.flush()
    print('cookies保存成功！')
    driver.quit()