import json
import undetected_chromedriver as uc
import os

def clear_directory(directory_path):
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                clear_directory(file_path)
                os.rmdir(file_path)
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")


def login_cookies():
    ### 下面是chromedriver路径，自己填
    browser = uc.ChromeOptions()
    browser.add_experimental_option("prefs", {"credentials_enable_service": False,"profile.password_manager_enabled": False})
    driver = uc.Chrome(options=browser)
    ### 打开要自动登录的网站
    driver.get("https://meizhe.meideng.net")
    with open('/MZSHUIYIN/cookies.txt', 'r', encoding='utf8') as f:
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
    return driver

#pytest终端执行时../MEIZHE/testcase1/cookies.txt
#单个用例执行，可以../testcase1/cookies.txt


