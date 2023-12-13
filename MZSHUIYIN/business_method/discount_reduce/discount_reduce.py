from business_method.page_ele import commond_ele as cele
from business_method.page_ele import discount_reduce as re
from base.base import BasePage
from business_method.page_ele import commond_ele as com

class  DiscountReduce():

    def __init__(self, driver):
        self.driver = BasePage(driver)

    # 折扣状态活动主流程
    def case1(self):
        self.driver.hover(cele.hover_discount, doc='悬浮于活动创建')
        self.driver.click_elements(com.promotion, sort=0, doc='点击进入折扣减价')
        self.driver.click_element(re.next_produce, doc='下一步，选择活动商品')
        self.driver.click_element(re.select_product3, doc='选择商品3')
        self.driver.click_element(re.next_discount, doc='下一步，设置商品折扣')
        self.driver.click_element(re.product_cut, doc='点击减价')
        self.driver.input_text(re.product_cut, "1", doc='输入减价1')
        self.driver.click_element(re.next_complete, doc='完成并提交')
        self.driver.click_element(cele.pop1, doc='关闭评价弹窗')
        self.driver.assert_text(re.assert_0, "活动创建成功", doc='断言活动创建成功')

    # 定向标签限定分组
    def case2(self):
        self.driver.hover(cele.hover_discount, doc='悬浮于活动创建')
        self.driver.click_elements(com.promotion, sort=0, doc='点击进入折扣减价')
        self.driver.click_element(cele.active_range_limit, doc='选择限定分组')
        self.driver.assert_text(cele.assert_ele2, '官方公告', doc='断言限定分组需要定向优惠类标签')

    # 活动结束时间不能早于等于开始时间
    def case3(self):
        self.driver.hover(cele.hover_discount, doc='悬浮于活动创建')
        self.driver.click_elements(com.promotion, sort=0, doc='点击进入折扣减价')
        self.driver.click_element(cele.start_time, doc='点击开始时间')
        self.driver.click_element(cele.click_today, doc='点击今天')
        self.driver.click_element(cele.end_time, doc='点击结束时间')
        self.driver.click_element(cele.click_today, doc='点击今天')
        self.driver.assert_text(cele.assert_ele3, '活动结束时间必须晚于当前系统时间',
                                doc='断言活动结束时间必须晚于当前系统时间')

    # 首件优惠活动模式下只能使用减价
    def case4(self):
        self.driver.hover(cele.hover_discount, doc='悬浮于活动创建')
        self.driver.click_elements(com.promotion, sort=0, doc='点击进入折扣减价')
        self.driver.click_element(cele.first_discount, doc='点击首件优惠')
        self.driver.click_element(re.next_produce, doc='下一步选择活动商品')
        self.driver.click_element(re.select_product3, doc='选择商品3')
        self.driver.click_element(re.next_discount, doc='下一步，设置商品折扣')
        self.driver.hover(re.discount0,doc='悬浮与打折框')
        self.driver.assert_text(cele.assert_ele4,
                                '首件优惠活动内只能使用减价模式，已将「打折」模式商品自动换算为减价模式，折后价不变，请确认',
                                doc='断言首件优惠只能使用减价模式')

    # 验证限购数量小于最小值断言
    def case5(self):
        self.driver.hover(cele.hover_discount, doc='悬浮于活动创建')
        self.driver.click_elements(com.promotion, sort=0, doc='点击进入折扣减价')
        self.driver.click_element(cele.quota_num, doc='点击限购件数框')
        self.driver.input_text(cele.quota_num, '0', doc='限购输入0件')
        self.driver.assert_text(cele.assert_ele5, '1 到 99999，当前输入 0，低于最小允许值',
                                doc='断言限购数量低于最小允许值')

    # 验证限购数量为500时创建打折活动成功
    def case6(self):
        self.driver.hover(cele.hover_discount, doc='悬浮于活动创建')
        self.driver.click_elements(com.promotion, sort=0, doc='点击进入折扣减价')
        self.driver.click_element(cele.quota_num, doc='点击限购件数框')
        self.driver.input_text(cele.quota_num, '500', doc='限购输入500件')
        self.driver.click_element(re.next_produce, doc='下一步选择活动商品')
        self.driver.click_element(re.select_product3, doc='选择商品3')
        self.driver.click_element(re.next_discount, doc='下一步，设置商品折扣')
        self.driver.click_element(re.discount0, doc='点击打折框')
        self.driver.input_text(re.discount0, '8.5', clear=2, doc='输入框打8.5折')
        self.driver.click_element(re.next_complete, doc='完成并提交')
        self.driver.click_element(cele.pop1, doc='关闭评价弹窗')
        self.driver.assert_text(re.assert_0, "活动创建成功", doc='断言活动创建成功')

    # 验证活动备注字数限制
    def case7(self):
        self.driver.hover(cele.hover_discount, doc='悬浮于活动创建')
        self.driver.click_elements(com.promotion, sort=0, doc='点击进入折扣减价')
        self.driver.input_text(cele.activity_note, "测", clear=2, doc='活动备注输入一个字折')
        self.driver.assert_text(cele.assert_ele6, '2 到 30 个字，已输入 1 个字', doc='断言备注为一个字时报错')

    # 验证常规版选择商品时，提示还可选择剩余商品数量
    def case8(self):
        self.driver.hover(cele.hover_discount, doc='悬浮于活动创建')
        self.driver.click_elements(com.promotion, sort=0, doc='点击进入折扣减价')
        self.driver.click_element(re.next_produce, doc='下一步，选择活动商品')
        self.driver.click_element(re.select_product3, doc='选择商品3')
        self.driver.assert_text(cele.assert_ele7, '149', doc='断言常规版还可以选择149个商品')

    # 验证尊享版选择商品时，提示还可选择剩余商品数量
    def case9(self):
        self.driver.hover(cele.hover_discount, doc='悬浮于活动创建')
        self.driver.click_elements(com.promotion, sort=0, doc='点击进入折扣减价')
        self.driver.click_element(cele.exclusive_version, doc='选择尊享版')
        self.driver.click_element(re.next_produce, doc='下一步，选择活动商品')
        self.driver.click_element(re.select_product3, doc='选择商品3')
        self.driver.assert_text(cele.assert_ele8, '599', doc='断言尊享版还可以选择599个商品')

    # 验证旗舰版选择商品时，提示还可以选择剩余商品数量
    def case10(self):
        self.driver.hover(cele.hover_discount, doc='悬浮于活动创建')
        self.driver.click_elements(com.promotion, sort=0, doc='点击进入折扣减价')
        self.driver.click_element(cele.ultimate_version, doc='选择旗舰版')
        self.driver.click_element(re.next_produce, doc='下一步，选择活动商品')
        self.driver.click_element(re.select_product3, doc='选择商品3')
        self.driver.assert_text(cele.assert_ele9, '2999', doc='断言旗舰版还可以选择2999个商品')