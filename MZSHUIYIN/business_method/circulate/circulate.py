from base.base import BasePage
from business_method.page_ele import commond_ele as com
from business_method.page_ele import circulate_discount as CE


class circulate_ele():
    def __init__(self, driver):
        self.driver = BasePage(driver)

    def case1(self):           # 显示折扣价 只选择一个商品
        self.driver.hover(com.hover_discount, doc='悬浮于活动创建')
        self.driver.click_elements(com.promotion, sort=2 , doc='点击循环打折')
        self.driver.click_element(CE.cycle_tuesday, doc='活动周期选择周二')
        self.driver.click_element(CE.add_activity_period2, doc='增加活动时段2')
        self.driver.click_element(CE.add_activity_period3, doc='增加活动时段3')
        self.driver.click_element(CE.next_produce, doc='下一步，选择活动商品')
        self.driver.click_element(CE.select_product1, doc='选择商品1')
        self.driver.click_element(CE.next_discount, doc='下一步，设置商品折扣')
        self.driver.input_text(CE.one_discount, '9',clear=2, doc='时段1折扣设置打9折')
        self.driver.click_element(CE.next_period, '下一步设置时段2的折扣')
        self.driver.input_text(CE.one_discount, '8.5', clear=2, doc='时段2折扣设置打8.5折')
        self.driver.click_element(CE.next_period, doc='下一步设置时段3的折扣')
        self.driver.input_text(CE.one_reduce, '10', clear=2, doc='设置减价10')
        self.driver.click_element(CE.next_complete, doc='完成并提交')
        self.driver.assert_text(CE.assert_0, '活动创建成功',doc='断言 活动创建成功')
'''
    def case2(self):         # 不显示折扣价 选择两个商品进行批量设置
        self.driver.hover(com.hover_discount, doc='悬浮于活动创建')
        self.driver.click_elements(com.circulate_dis, sort=2 , doc='点击循环打折')
        self.driver.click_element(CE.all_cycle, doc='活动周期全选')
        self.driver.click_element(CE.un_add_activity_period, doc='增加活动时段2')
        self.driver.click_element(CE.un_discounts1, '9', doc='修改活动时段1的折扣为打9折')
        self.driver.click_element(CE.un_reduce_price2, '10', doc='修改活动时段2的减价10')
        self.driver.click_element(CE.next_produce, doc='下一步，选择活动商品')
        self.driver.click_element(com.select_product2, doc='选择商品2')
        self.driver.click_element(com.select_product3, doc='选择商品3')
        self.driver.click_element(CE.next_setting_discount, doc='下一步 设置商品折扣')
        self.driver.assert_text(com.assert_ele1, '活动创建成功',doc='断言 活动创建成功')
'''