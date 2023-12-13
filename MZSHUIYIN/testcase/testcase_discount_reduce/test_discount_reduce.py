from business_method.discount_reduce.discount_reduce import DiscountReduce as DRE
from common.logger import Logger
import pytest,allure

@allure.epic("折扣减价")  # 项目名称
class Test_discount_reduce():
    @pytest.mark.smoke
    # @allure.feature('')  # 一级标签一级标签_测试模块
    @allure.story('折扣减价主流程')  # 二级标签 二级标签_测试模块
    @allure.title("验证折扣减价主流程无误")  # 三级标签 用例名称@
    @allure.step('折扣减价')
    @allure.severity('blocker')  # 等级 blocker,critical,normal,minor,trivial  阻塞，严重，一般，次要，轻微
    def test_1(self,driver1):
        DRE(driver1).case1()

    @pytest.mark.smoke
    # @allure.feature('')  # 一级标签一级标签_测试模块
    @allure.story('折扣减价断言限定分组-定向标签')  # 二级标签 二级标签_测试模块
    @allure.title("验证限定分组提示需要定向标签无误")  # 三级标签 用例名称@
    @allure.step('定向分组选择定向标签')
    @allure.severity('blocker')  # 等级 blocker,critical,normal,minor,trivial  阻塞，严重，一般，次要，轻微
    def test_2(self, driver1):
        DRE(driver1).case2()

    @pytest.mark.smoke
    # @allure.feature('')  # 一级标签一级标签_测试模块
    @allure.story('折扣减价断言开始/结束时间')  # 二级标签 二级标签_测试模块
    @allure.title("验证活动结束时间不能早于或等于开始时间无误")  # 三级标签 用例名称@
    @allure.step('开始时间>=结束时间')
    @allure.severity('blocker')  # 等级 blocker,critical,normal,minor,trivial  阻塞，严重，一般，次要，轻微
    def test_3(self, driver1):
        DRE(driver1).case3()

    @pytest.mark.smoke
    # @allure.feature('')  # 一级标签一级标签_测试模块
    @allure.story('折扣减价断言首件优惠模式下只能使用减价')  # 二级标签 二级标签_测试模块
    @allure.title("验证首件优惠模式下不能使用折扣无误")  # 三级标签 用例名称@
    @allure.step('首件优惠只能减价')
    @allure.severity('blocker')  # 等级 blocker,critical,normal,minor,trivial  阻塞，严重，一般，次要，轻微
    def test_4(self, driver1):
        DRE(driver1).case4()

    @pytest.mark.smoke
    # @allure.feature('')  # 一级标签一级标签_测试模块
    @allure.story('折扣减价断言限购数量输入小于最小值')  # 二级标签 二级标签_测试模块
    @allure.title("验证断言提示限购数量小于最小值无误")  # 三级标签 用例名称@
    @allure.step('限购数量1-99999')
    @allure.severity('blocker')  # 等级 blocker,critical,normal,minor,trivial  阻塞，严重，一般，次要，轻微
    def test_5(self, driver1):
        DRE(driver1).case5()

    @pytest.mark.smoke
    # @allure.feature('')  # 一级标签一级标签_测试模块
    @allure.story('折扣减价限购数量为500创建活动成功')  # 二级标签 二级标签_测试模块
    @allure.title("验证断言提示限购数量小于最小值无误")  # 三级标签 用例名称@
    @allure.step('限购数量1-99999')
    @allure.severity('blocker')  # 等级 blocker,critical,normal,minor,trivial  阻塞，严重，一般，次要，轻微
    def test_6(self, driver1):
        DRE(driver1).case6()

    @pytest.mark.smoke
    # @allure.feature('')  # 一级标签一级标签_测试模块
    @allure.story('折扣减价活动备注字数限制')  # 二级标签 二级标签_测试模块
    @allure.title("验证断言活动备注字数字数不够报错提示无误")  # 三级标签 用例名称@
    @allure.step('活动备注字数限制2-30')
    @allure.severity('blocker')  # 等级 blocker,critical,normal,minor,trivial  阻塞，严重，一般，次要，轻微
    def test_7(self, driver1):
        DRE(driver1).case7()

    @pytest.mark.smoke
    # @allure.feature('')  # 一级标签一级标签_测试模块
    @allure.story('折扣减价常规版提示剩余商品数量')  # 二级标签 二级标签_测试模块
    @allure.title("验证断言常规版提示剩余商品数无误")  # 三级标签 用例名称@
    @allure.step('常规版选择商品后提示剩余商品数量')
    @allure.severity('blocker')  # 等级 blocker,critical,normal,minor,trivial  阻塞，严重，一般，次要，轻微
    def test_8(self, driver1):
        DRE(driver1).case8()

    @pytest.mark.smoke
    # @allure.feature('')  # 一级标签一级标签_测试模块
    @allure.story('折扣减价尊享版提示剩余商品数量')  # 二级标签 二级标签_测试模块
    @allure.title("验证断言尊享版提示剩余商品数无误")  # 三级标签 用例名称@
    @allure.step('尊享版选择商品后提示剩余商品数量')
    @allure.severity('blocker')  # 等级 blocker,critical,normal,minor,trivial  阻塞，严重，一般，次要，轻微
    def test_9(self, driver1):
        DRE(driver1).case9()

    @pytest.mark.smoke
    # @allure.feature('')  # 一级标签一级标签_测试模块
    @allure.story('折扣减价旗舰版提示剩余商品数量')  # 二级标签 二级标签_测试模块
    @allure.title("验证断言旗舰版提示剩余商品数无误")  # 三级标签 用例名称@
    @allure.step('旗舰版选择商品后提示剩余商品数量')
    @allure.severity('blocker')  # 等级 blocker,critical,normal,minor,trivial  阻塞，严重，一般，次要，轻微
    def test_10(self, driver1):
        DRE(driver1).case10()