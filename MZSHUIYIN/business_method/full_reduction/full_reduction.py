from business_method.page_ele import commond_ele as cele
from business_method.page_ele import full_reduction as FUP
from base.base import BasePage
from business_method.page_ele import commond_ele as com


class full_reduction_ele():

    def __init__(self, driver):
        self.driver = BasePage(driver)

    # 满减/满包邮-验证活动标签（满就包邮）-满1000元减50元+包邮主流程
    def case1(self):
        self.driver.hover(cele.hover_discount, doc='悬浮于活动创建')
        self.driver.click_elements(com.promotion, sort=3, doc='点击进入满减/满包邮')
        self.driver.click_element(FUP.activity_label, doc='活动标签点击下拉框')
        self.driver.click_element(FUP.full_package_shipping, doc='活动标签选择满就包邮')
        self.driver.click_element(FUP.next_produce, doc='下一步选择活动商品')
        self.driver.click_element(cele.select_product1, doc='选择商品1')
        self.driver.click_element(cele.select_product2, doc='选择商品2')
        self.driver.click_element(FUP.next_activate, doc='下一步设置活动详情')
        self.driver.input_text(FUP.full_yuan, '1000', clear=2, doc='条件1-满元输入框输入满1000元')
        self.driver.input_text(FUP.reduce_price, '50', clear=2, doc='内容1-减价输入框输入减50元')
        self.driver.click_element(FUP.free_shipping, doc='勾选包邮')
        self.driver.click_element(FUP.next_complete, doc='完成并提交')
        self.driver.click_element(FUP.pop1, doc='关闭评价弹窗')
        self.driver.assert_text(FUP.assert_0, "活动创建成功", doc='断言活动创建成功')

    # 满减/满包邮-验证活动标签自定义（满减活动测试）-满2件打9折+送礼物（棒棒糖）
    def case2(self):
        self.driver.hover(cele.hover_discount, doc='悬浮于活动创建')
        self.driver.click_elements(com.promotion, sort=3, doc='点击进入满减/满包邮')
        self.driver.click_element(FUP.click_custom, doc='活动标签点击自定义')
        self.driver.input_text(FUP.custom_input, '满减活动测试', clear=2,doc='自定义活动标签输入满减活动测试')
        self.driver.click_element(FUP.next_produce, doc='下一步选择活动商品')
        self.driver.click_element(cele.select_product1, doc='选择商品1')
        self.driver.click_element(FUP.next_activate, doc='下一步设置活动详情')
        self.driver.input_text(FUP.full_jian, '3', doc='条件1-，满件输入框输入满3件')
        self.driver.input_text(FUP.discount_price, '9', clear=2,doc='内容1-打折输入框输入9折')
        self.driver.click_element(FUP.give_gifts, doc='勾选礼物')
        self.driver.input_text(FUP.gifts_name, '棒棒糖', clear=2,doc='礼物名称输入棒棒糖')
        self.driver.click_element(FUP.next_complete, doc='完成并提交')
        self.driver.click_element(FUP.pop1, doc='关闭评价弹窗')
        self.driver.assert_text(FUP.assert_0, "活动创建成功", doc='断言活动创建成功')

    # 满减/满包邮-验证活动满1000元且满3件-打9折 添加多级优惠-满2件减10元
    def case3(self):
        self.driver.hover(cele.hover_discount, doc='悬浮于活动创建')
        self.driver.click_elements(com.promotion, sort=3, doc='点击进入满减/满包邮')
        self.driver.click_element(FUP.exclusive_version,doc="选择尊享版")
        self.driver.click_element(FUP.next_produce, doc='下一步选择活动商品')
        self.driver.click_element(cele.select_product1, doc='选择商品1')
        self.driver.click_element(FUP.next_activate, doc='下一步设置活动详情')
        self.driver.input_text(FUP.full_yuan_jian1, '1000', clear=2,doc='条件1-满元输入1000元')
        self.driver.input_text(FUP.full_yuan_jian2, '3', clear=2,doc='条件1-满件输入3件')
        self.driver.input_text(FUP.discount_price, '9', clear=2,doc='内容1-打折输入框输入9折')
        self.driver.click_element(FUP.add_many_preferential, doc='添加多级优惠')
        self.driver.input_text(FUP.full_jian, '2', clear=2,doc='条件2-满件输入2件')
        self.driver.input_text(FUP.reduce_price, '10', clear=2,doc='内容2-满减框输入10元')
        self.driver.click_element(FUP.banner_pink, doc='横幅设置浅桃红')
        self.driver.click_element(FUP.next_complete, doc='完成并提交')
        self.driver.click_element(FUP.pop1, doc='关闭评价弹窗')
        self.driver.assert_text(FUP.assert_0, "活动创建成功", doc='断言活动创建成功')



