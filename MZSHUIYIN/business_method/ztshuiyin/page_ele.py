from selenium.webdriver.common.by import By

class Shuiyin11():
    hover_sucai = (By.XPATH,'//*[@id="component_navbar"]/nav/div/div[2]/ul[1]/li[4]/a') #首页导航栏素材悬浮元素
    watermark = (
    By.CSS_SELECTOR, 'div.amWJu6uN.UC4tVJBm.ybOZHe0x.B9h15aOr > div.o8VxI75D > a:nth-child(2) > span.UR73VILe')
    # [0]置顶，[1]置底    主图水印元素位置
    setup_shuiyin = ()


