from MZSHUIYIN.business_method.ztshuiyin.page_ele import Shuiyin11 as sy11
# from MZSHUIYIN.business_method.ztshuiyin.page_ele import discount_reduce as re
from MZSHUIYIN.base.base import BasePage
# from MZSHUIYIN.business_method.ztshuiyin.page_ele import Shuiyin11 as com

class Shuiyin11() :
    def __init__(self, driver):
        self.driver = BasePage(driver)

    def case1(self):
        self.driver.hover(sy11.hover_sucai, doc='悬浮于素材创建')
        self.driver.click_elements(sy11.watermark, sort=0, doc='点击进入主图水印（新）')
        self.driver.click_element(sy11.next_produce, doc='下一步，选择活动商品')
        # self.driver.click_element(re.select_product3, doc='选择商品3')
        # self.driver.click_element(re.next_discount, doc='下一步，设置商品折扣')
        # self.driver.click_element(re.product_cut, doc='点击减价')
        # self.driver.input_text(re.product_cut, "1", doc='输入减价1')
        # self.driver.click_element(re.next_complete, doc='完成并提交')
        # self.driver.click_element(cele.pop1, doc='关闭评价弹窗')
        # self.driver.assert_text(re.assert_0, "活动创建成功", doc='断言活动创建成功')
