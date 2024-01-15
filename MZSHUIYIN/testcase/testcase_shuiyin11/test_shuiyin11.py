from MZSHUIYIN.business_method.ztshuiyin.page_ele import Shuiyin11 as SY11
from MZSHUIYIN.common.logger import Logger
import pytest,allure

@allure.epic("主图水印")  # 项目名称
class Test_shuyin11():
    @pytest.mark.smoke
    # @allure.feature('')  # 一级标签一级标签_测试模块
    @allure.story('主图水印创建主流程') # 二级标签 二级标签_测试模块
    @allure.title('验证水印创建流程显示无误') # 三级标签 用例名称@
    @allure.step('1:1主图水印')
    @allure.severity('blocker')  # 等级 blocker,critical,normal,minor,trivial  阻塞，严重，一般，次要，轻微

    def test_1(self,driver1):
        SY11(driver1).case1()