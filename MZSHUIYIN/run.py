import pytest
import os
import shutil
from common.getcookie import getcookie
from common.logincookie import clear_directory as cle
from common.logger import Logger

if __name__ == '__main__':
    #print("开始删除allure-results")
    # filepath = (os.path.abspath(os.path.dirname(__file__)) + "/allure-results/")
    # if os.path.exists(filepath):
    #     shutil.rmtree("{}".format(filepath))
    #     os.makedirs("{}".format(filepath))
    # else:
    #     os.makedirs("{}".format(filepath))
    # path_report = (os.path.abspath(os.path.dirname(__file__)) + "/allure-report")
    # if os.path.exists(path_report):
    #     shutil.rmtree("{}".format(path_report))

    getcookie()
    a_clear = '/MZSHUIYIN/png'
    b_clear = '/MZSHUIYIN/images'

    try:
        cle(a_clear)
        cle(b_clear)
        shutil.rmtree("./target")  # 删除报告目录，删除后只能看到当前执行后的报告结果，不删除能看到执行的历史执行结果
    except:
        pass


    # pytest.main(['-m','smoke'])
    pytest.main(['-vs','--alluredir', './target/allure-results'])  #test_func  test_risk  #'./test_func',

    #pytest.main(['./test_case','-vs','--alluredir', './target/allure-results'])#,'-n 3'

    allure_html = 'allure generate ./target/allure-results -o ./target/allure-report --clean'  # 生成allure的html报告
    os.system(allure_html)

    #os.system('allure open allure-report')  # 打开报告

#失败重试
# • 测试失败后要重新运行n次，要在重新运行之间添加延迟时 间，间隔n秒再运行。
# • 执行:
# • 安装:pip install pytest-rerunfailures
# • pytest -v - -reruns 5 --reruns-delay 1 —每次等1秒 重试5次

#并发运行
# 前提:用例之间都是独立的，没有先后顺序，随机都能执行，可重复运行不 影响其他用例。
# 安装:Pip3 install pytest-xdist
# • 多个CPU并行执行用例，直接加-n 3是并行数量:pytest -n 3 • 在多个终端下一起执行

    # os.system('--alluredir=allure-results  --clean-alluredir')#清理之前的
    # os.system('allure generate allure-results -o allure-report -c ')#allure generate命令的时候会从这些测试结果集中去生成HTML报告

    # pytest.main(["-sq",
    #              "--alluredir", "./allure-results"])
    # os.system(r"allure generate --clean allure-results -o allure-report")



