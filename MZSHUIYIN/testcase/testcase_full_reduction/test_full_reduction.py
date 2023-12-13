from business_method.full_reduction.full_reduction import full_reduction_ele as FU
from common.logger import Logger
import pytest, allure

@allure.epic("满减/满包邮")  # 项目名称
class Test_discount_reduce():
    @pytest.mark.smoke
    # @allure.feature('')  # 一级标签一级标签_测试模块
    @allure.story('满1000元减50+包邮主流程')  # 二级标签 二级标签_测试模块
    @allure.title("验证满1000减50+包邮且活动标签为下拉框-满就包邮无误")  # 三级标签 用例名称@
    @allure.step('满减+满包邮')
    @allure.severity('blocker')  # 等级 blocker,critical,normal,minor,trivial  阻塞，严重，一般，次要，轻微
    def test_1(self, driver1):
        FU(driver1).case1()

    @pytest.mark.smoke
    # @allure.feature('')  # 一级标签一级标签_测试模块
    @allure.story('满3件打9折+送礼物主流程')  # 二级标签 二级标签_测试模块
    @allure.title("验证满3件打9折+送礼物且活动标签为自定义-满减活动测试无误")  # 三级标签 用例名称@
    @allure.step('满件+送礼物')
    @allure.severity('blocker')  # 等级 blocker,critical,normal,minor,trivial  阻塞，严重，一般，次要，轻微
    def test_2(self, driver1):
        FU(driver1).case2()

    @pytest.mark.smoke
    # @allure.feature('')  # 一级标签一级标签_测试模块
    @allure.story('满100元且满2件打9折+多级优惠主流程')  # 二级标签 二级标签_测试模块
    @allure.title("验证满100元且满2件打9折+多级优惠无误")  # 三级标签 用例名称@
    @allure.step('满元+满件+多级优惠+横幅')
    @allure.severity('blocker')  # 等级 blocker,critical,normal,minor,trivial  阻塞，严重，一般，次要，轻微
    def test_3(self, driver1):
        FU(driver1).case3()