# web自动化测试框架 pytest-allure-selenium-po-demo

#### 介绍
web自动化测试框架 pytest-allure-selenium-po

#### 软件架构
采用PO模型设计思路+pytest测试框架allure展示测试报告

```log
├─base          #base基本操作类，selenium  二次封装
├─business      #促销业务测试
│  ├─ circulate            # 循环打折 
│  ├─ discount_reduce      # 折扣减价
│  ├─ discount_ip          # 折上折
│  ├─ full_reduction       # 满减/满包邮
│  ├─ second_sell          # 第二件促销
│  ├─ sku                  # sku折扣
│  ├─ whole_freeshipping   # 全店满减包邮
│  ├─ whole_store_discount # 全店折扣减价
│  └─ page_ele.py          # 页面元素存储
├─common        #公共方法 
├─images        #录屏文件存放
├─log           #日志
├─png           #截图
├─target        #测试报告
├─testcase      #用例执行测试    
│  ├─ testcase_circulate            # 循环打折 
│  ├─ testcase_discount_reduce      # 折扣减价
│  ├─ testcase_discount_ip          # 折上折
│  ├─ testcase_full_reduction       # 满减/满包邮
│  ├─ testcase_second_sell          # 第二件促销
│  ├─ testcase_sku                  # sku折扣
│  ├─ testcase_whole_freeshipping   # 全店满减包邮
│  └─ testcase_whole_store_discount # 全店折扣减价  
├─conftest.py       #共享配置
├─requirements.txt  #所需要的模块
└─run.py            #执行
  
```


#### 安装教程

1.  安装依赖环境 pip install -r requirements.txt -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
2.  安装allrue报告allure-2.xx.xx.zip
3.  安装java环境，allure需要java环境

#### 使用说明

1.  实现封装了iframe切换，句柄切换，非Input标签上传等等操作
2.  采用PO模型设计思路+pytest测试框架allure展示测试报告
#### 特技

