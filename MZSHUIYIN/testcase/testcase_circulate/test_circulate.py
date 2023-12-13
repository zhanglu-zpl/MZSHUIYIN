from business_method.circulate.circulate import circulate_ele as CE
from common.logger import Logger
import pytest,allure

@allure.epic("循环折扣")  # 项目名称
class Test_circulate():
    @pytest.mark.smoke
    # @allure.feature('')  # 一级标签一级标签_测试模块
    @allure.story('循环折扣显示主流程')  # 二级标签 二级标签_测试模块
    @allure.title("验证循环折扣显示主流程无误")  # 三级标签 用例名称@
    @allure.step('循环折扣')
    @allure.severity('blocker')  # 等级 blocker,critical,normal,minor,trivial  阻塞，严重，一般，次要，轻微
    def test_1(self,driver1):
        CE(driver1).case1()

'''
    @pytest.mark.smoke
    # @allure.feature('')  # 一级标签一级标签_测试模块
    @allure.story('循环打折不显示折扣主流程')  # 二级标签 二级标签_测试模块
    @allure.title("验证循环打折不显示折扣主流程")  # 三级标签 用例名称@
    @allure.step('循环打折')
    @allure.severity('blocker')  # 等级 blocker,critical,normal,minor,trivial  阻塞，严重，一般，次要，轻微
    def test_2(self, driver1):
        CE(driver1).case2()
        '''
