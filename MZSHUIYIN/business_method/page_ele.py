from selenium.webdriver.common.by import By


class commond_ele():
    hover_discount = (By.XPATH, '/html/body/div[4]/div[1]/header/nav/div/div[2]/ul[1]/li[2]/a')  # 促销悬浮元素
    # 活动创建-折扣/减价[0]、SKU打折[1]、循环打折[2]、满减/满就包邮[3]、第二件促销[4]、全店折扣/减价[5]、全店满减/包邮[6]、淘金币抵扣[7]、折上折元素[8]
    # promotion = (By.CSS_SELECTOR, 'div.amWJu6uN.UC4tVJBm.ybOZHe0x > div.o8VxI75D > a.BV2UTq8x > span.UR73VILe')
    #[0]置顶，[1]置底
    topping = (By.CSS_SELECTOR, 'ul.p7kswUBL > li')

    not_finish=(By.XPATH, '//*[@id="nav-sidebar"]/div/div[2]/div/div/div/div[1]')  # 未结束活动
    first_active=(By.CSS_SELECTOR, 'div.activity-action-main > div > a.mz-btn.btn-bordered.btn-default')[0]#选择第一个活动，结束
    confirm=(By.XPATH, '/html/body/div[14]/div[2]/div/div/div[2]/div/div/div[2]/button[2]')  # 点击确认结束

    price_tag = (By.XPATH, '//*[@id="act-title-form-group"]/div[2]/div[1]/ko-promotion-title/div/div')  # 价格标签
    activity_tag = (By.XPATH, '//*[@id="act-title-form-group"]/div[3]/div[1]/div[1]/ko-dropdown-list/div') #活动标签
    active_range_limit = (By.XPATH, '//*[@id="crm-group-form-group"]/div[2]/label[2]/span')  # 活动范围-限定分组
    active_range_nolimit = (By.XPATH, '//*[@id="crm-group-form-group"]/div[2]/label[1]/span')  # 活动范围 - 不限
    price_tag_tip = (By.XPATH, '//*[@id="act-title-form-group"]/div[2]/div[2]/label[2]/text()')  # 价格标签-限定分组时的断言提示
    un_purchase =(By.XPATH, '//*[@id="zhekou-buy-limit-form-group"]/div[2]/label[1]/span')  # 优惠限购 - 不限购
    first_discount = (By.XPATH, '//*[@id="zhekou-buy-limit-form-group"]/div[2]/label[2]/span')  # 优惠限购 - 首件优惠
    hover_input_discount = (By.XPATH, '//*[@id="act-step-3"]/div[7]/ul/li/div/div[4]/input')  # 设置折扣页 - 鼠标悬浮在打折显示hover
    quota_num = (By.XPATH,'//*[@id="act-custom-buy-limit"]')  # 限购件数 - xxx
    activity_note = (By.XPATH,'//*[@id="act-name"]')  # 设置活动信息 - 活动备注

    regular_version = (By.XPATH, '//*[@id="mj-type"]/div[2]/div[1]')  # 常规版
    exclusive_version = (By.XPATH, '//*[@id="zhekou-buy-limit-form-group"]/div[2]/div[2]')  # 尊享版
    ultimate_version = (By.XPATH, '//*[@id="zhekou-buy-limit-form-group"]/div[2]/div[3]')  # 旗舰版

    start_time = (By.XPATH, '//*[@id="act-start"]')  # 设置活动信息 - 开始时间
    end_time = (By.XPATH, '//*[@id="act-end"]')  # 设置活动信息 - 结束时间
    '//*[@id="zhekouPage"]/div[14]/div[1]/div[2]/div/div[2]/div[1]/ul/li[9]'
    hour_time20 = (By.XPATH, '//*[@id="zhekouPage"]/div[15]/div[1]/div[2]/div/div[2]/div[1]/ul/li[21]')  # 开始时间的小时修改到20点
    time_page1 = (By.XPATH, '//*[@id="zhekouPage"]/div[15]/div[1]/div[1]/div/button[1]/i')  # 设置活动信息 - 时间框往前翻页
    time_page2 = (By.XPATH, '//*[@id="zhekouPage"]/div[15]/div[1]/div[1]/div/button[2]/i')  # 设置活动信息 - 时间框往后翻页

    click_today = (By.XPATH, '//*[@id="zhekouPage"]/div[14]/div[2]/button[1]')  # 点击今天
    click_sure = (By.XPATH, '//*[@id="zhekouPage"]/div[14]/div[2]/button[2]')  # 点击确定
    next_activate = (By.XPATH, '//*[@id="act-step-2"]/div[3]/a[2]') # 下一步 设置活动详情

    input_10 = (By.XPATH, '//*[@id="mz-batch-query-v2-input"]')  # 选择活动页搜索10的商品
    search = (By.XPATH, '//*[@id="mz-batch-query-v2-form"]/div[1]/button')  # 点击搜索
    all_page = (By.XPATH, '/html/body/div[4]/div[2]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[2]/button[1]')  # 全选本页
    select_product1 = (By.XPATH, '//*[@id="act-item-selector"]/ko-item-selector/div/div[6]/div/div[1]/div/div[3]/a')  # 商品1
    select_product2 = (By.XPATH, '//*[@id="act-item-selector"]/ko-item-selector/div/div[6]/div/div[2]/div/div[3]/a')  # 商品2
    select_product3 = (By.XPATH, '//*[@id="act-item-selector"]/ko-item-selector/div/div[6]/div/div[3]/div/div[3]/a')  # 商品3
    select_product4 = (By.XPATH, '//*[@id="act-item-selector"]/ko-item-selector/div/div[6]/div/div[4]/div/div[3]/a')  # 商品4
    select_product5 = (By.XPATH, '//*[@id="act-item-selector"]/ko-item-selector/div/div[6]/div/div[5]/div/div[3]/a')  # 商品5
    select_product6 = (By.XPATH, '//*[@id="act-item-selector"]/ko-item-selector/div/div[6]/div/div[6]/div/div[3]/a')  # 商品6
    choose149 = (By.XPATH, '//*[@id="act-item-selector"]/ko-item-selector/div/div[1]/ul/li[8]/span[1]/span[2]/strong') # 还可以选择149个商品
    choose599 = (By.XPATH, '//*[@id="act-item-selector"]/ko-item-selector/div/div[1]/ul/li[8]/span[1]/span[2]/strong') # 还可以选择599个商品

    product_discount = (By.XPATH, '//*[@id="act-step-3"]/div[7]/ul/li/div/div[4]/input')  # 折扣/减价-设置商品折扣-打折
    product_cut = (By.XPATH, '//*[@id="act-step-3"]/div[7]/ul/li/div/div[5]/input')  # 折扣/减价-设置商品折扣-减价
    product_cut_late = (By.XPATH, '//*[@id="act-step-3"]/div[7]/ul/li/div/div[6]/input')  # 折扣/减价-设置商品折扣-减后
    over_to = (By.XPATH, '//*[@id="act-step-3"]/div[10]/div/a[2]')  # 折扣/减价、sku打折-完成并提交
    pop1 = (By.XPATH, '//*[@id="zhekouPage"]/div[12]/div/div/button')  # 活动创建成功后的评价弹窗关闭键
    #  断言
    assert_ele1 = (By.XPATH, '/html/body/div[4]/div[2]/div[1]/div[2]/div[2]/div/div[2]/div/div[10]/button')  # 断言1，活动创建成功
    assert_ele2 = (By.XPATH, '//*[@id="act-title-form-group"]/div[2]/div[2]/label[2]/a')  # 断言2 定向优惠限定分组【官方公告】
    assert_ele3 = (By.XPATH, '//*[@id="act-end-form-group"]/div[3]/label[2]/span')  # 断言3  活动结束时间不能早于或等于开始时间
    assert_ele4 = (By.XPATH, '//*[@id="act-step-3"]/div[7]/div[1]')  # 断言4  首件优惠活动内只能使用减价模式，已将「打折」模式商品自动换算为减价模式，折后价不变，请确认
    assert_ele5 = (By.XPATH, '//*[@id="zhekou-buy-limit-form-group"]/div[3]/label[3]')  # 断言5  优惠限购件数需要在1-99999之间
    assert_ele6 = (By.XPATH, '//*[@id="act-create-step-1"]/div[7]/div[3]/label[2]')  # 断言6  活动备注限制2-30个字，已输入x个字
    assert_ele7 = (By.XPATH, '//*[@id="act-item-selector"]/ko-item-selector/div/div[1]/ul/li[8]/span[1]/span[2]/strong')  # 还可以选择149个商品
    assert_ele8 = (By.XPATH, '//*[@id="act-item-selector"]/ko-item-selector/div/div[1]/ul/li[8]/span[1]/span[2]/strong')  # 还可以选择599个商品
    assert_ele9 = (By.XPATH, '//*[@id="act-item-selector"]/ko-item-selector/div/div[1]/ul/li[8]/span[1]/span[2]/strong')  # 还可以选择2999个商品
    assert_ele10 = (By.XPATH, '//*[@id="act-step-3"]/ul/li[1]/div/div[5]/input')  # 断言第二件商品为1元
    assert_ele11 = (By.XPATH, '//*[@id="tooltip371040"]/div[2]')  #首件优惠只支持减价模式

class discount_reduce():
    select_product1 = (By.XPATH, '//*[@id="act-item-selector"]/ko-item-selector/div/div[6]/div/div[1]/div/div[3]/a')  # 商品1
    select_product2 = (By.XPATH, '//*[@id="act-item-selector"]/ko-item-selector/div/div[6]/div/div[2]/div/div[3]/a')  # 商品2
    select_product3 = (By.XPATH, '//*[@id="act-item-selector"]/ko-item-selector/div/div[6]/div/div[3]/div/div[3]/a')  # 商品3
    select_product4 = (By.XPATH, '//*[@id="act-item-selector"]/ko-item-selector/div/div[6]/div/div[4]/div/div[3]/a')  # 商品4
    select_product5 = (By.XPATH, '//*[@id="act-item-selector"]/ko-item-selector/div/div[6]/div/div[5]/div/div[3]/a')  # 商品5
    select_product6 = (By.XPATH, '//*[@id="act-item-selector"]/ko-item-selector/div/div[6]/div/div[6]/div/div[3]/a')  # 商品6

    next_produce = (By.XPATH, '//*[@id="act-step-1"]/div[2]/div/a[2]')  # 下一步 选择活动商品
    next_discount = (By.XPATH, '//*[@id="act-step-2"]/div[3]/div/a[2]')  # 下一步 设置商品折扣
    next_complete = (By.XPATH, '//*[@id="act-step-3"]/div[10]/div/a[2]')  # 完成并提交
    product_cut = (By.XPATH, '//*[@id="act-step-3"]/div[7]/ul/li/div/div[5]/input')  # 折扣/减价-设置商品折扣-减价
    discount1 = (By.XPATH, '//*[@id="act-step-3"]/div[7]/ul/li[1]/div/div[4]/input')   #多件商品时，排第一的商品的打折定位
    discount2 = (By.XPATH, '//*[@id="act-step-3"]/div[7]/ul/li[2]/div/div[4]/input')   #多件商品时，排第二的商品的打折定位
    discount0 = (By.XPATH, '//*[@id="act-step-3"]/div[7]/ul/li/div/div[4]/input')      #单件商品时的打折定位
    assert_0 = (By.XPATH, '//*[@id="act-step-4"]/div/div[1]/div/div[1]/div/span')  # 断言  活动创建成功
    assert_1 = (By.XPATH, '//*[@id="tooltip149608"]/div[2]')   #首件优惠模式下，悬浮与打折框中的文本

class sku_discount():      # sku打折
    next_produce = (By.XPATH, '//*[@id="act-step-1"]/div[2]/div/a[2]')  # 下一步 选择活动商品
    next_discount = (By.XPATH, '//*[@id="act-step-2"]/div[3]/div/a[2]')  # 下一步 设置商品折扣
    next_complete = (By.XPATH, '//*[@id="act-step-3"]/div[10]/div/a[2]')  # 完成并提交
    select_product1 = (By.XPATH, '//*[@id="act-item-selector"]/ko-item-selector/div/div[6]/div/div[1]/div/div[3]/a')  # 商品1
    select_product2 = (By.XPATH, '//*[@id="act-item-selector"]/ko-item-selector/div/div[6]/div/div[2]/div/div[3]/a')  # 商品2
    select_product3 = (By.XPATH, '//*[@id="act-item-selector"]/ko-item-selector/div/div[6]/div/div[3]/div/div[3]/a')  # 商品3
    select_product4 = (By.XPATH, '//*[@id="act-item-selector"]/ko-item-selector/div/div[6]/div/div[4]/div/div[3]/a')  # 商品4
    select_product5 = (By.XPATH, '//*[@id="act-item-selector"]/ko-item-selector/div/div[6]/div/div[5]/div/div[3]/a')  # 商品5
    select_product6 = (By.XPATH, '//*[@id="act-item-selector"]/ko-item-selector/div/div[6]/div/div[6]/div/div[3]/a')  # 商品6
    hide_unsku = (By.XPATH, '//*[@id="act-item-selector"]/ko-item-selector/div/div[1]/div/div[4]/div/div[1]/div/a[2]')  # 隐藏非sku商品
    assert_0 = (By.XPATH, '//*[@id="act-step-4"]/div/div[1]/div/div[1]/div/span') #活动创建成功断言
    pop1 = (By.XPATH, '//*[@id="skuzhekouPage"]/div[12]/div/div/button') #表扬一下吧弹窗关闭按钮


    sku_hide = (By.XPATH, '//*[@id="act-item-selector"]/ko-item-selector/div/div[1]/div/div[4]/div/div[1]/div/a[2]')  # sku折扣选择活动商品页-隐藏非sku商品
    sku_display = (By.XPATH, '//*[@id="act-item-selector"]/ko-item-selector/div/div[1]/div/div[4]/div/div[1]/div/a[2]')  # sku折扣选择活动商品页-显示非sku商品
    sku_discounts = (By.XPATH, '//*[@id="act-step-3"]/div[6]/ul/li[1]/div/div[5]/button')  # 设置商品折扣页-设置sku折扣
    sku_discounts2 = (By.XPATH, '//*[@id="act-step-3"]/div[6]/ul/li[2]/div/div[5]/button')  # 设置商品折扣页-设置sku折扣2
    sku_discounts3 = (By.XPATH, '//*[@id="act-step-3"]/div[6]/ul/li[3]/div/div[5]/button')  # 设置商品折扣页-设置sku折扣3
    discount_standard1 = (By.XPATH, '/html/body/ko-modal-sku-setting/div/div/div/div[3]/div[4]/ul/li[1]/div/div[3]/input')  # sku折扣-设置sku折扣-打折规格1
    discount_standard2 = (By.XPATH, '/html/body/ko-modal-sku-setting/div/div/div/div[3]/div[4]/ul/li[2]/div/div[3]/input')  # sku折扣-设置sku折扣-打折规格2
    discount_standard3 = (By.XPATH, '/html/body/ko-modal-sku-setting/div/div/div/div[3]/div[4]/ul/li[3]/div/div[3]/input')  # sku折扣-设置sku折扣-打折规格3
    reduce_standard1 = (By.XPATH, '/html/body/ko-modal-sku-setting/div/div/div/div[3]/div[4]/ul/li[1]/div/div[4]/input') # sku折扣-设置sku折扣-减价规格1
    reduce_standard2 = (By.XPATH, '/html/body/ko-modal-sku-setting/div/div/div/div[3]/div[4]/ul/li[2]/div/div[4]/input') # sku折扣-设置sku折扣-减价规格2
    reduce_standard3 = (By.XPATH, '/html/body/ko-modal-sku-setting/div/div/div/div[3]/div[4]/ul/li[3]/div/div[4]/input') # sku折扣-设置sku折扣-减价规格3
    reduced_standard1 = (By.XPATH, '/html/body/ko-modal-sku-setting/div/div/div/div[3]/div[4]/ul/li[1]/div/div[5]/input')  # sku折扣-设置sku折扣-折/减后规格1
    reduced_standard2 = (By.XPATH, '/html/body/ko-modal-sku-setting/div/div/div/div[3]/div[4]/ul/li[2]/div/div[5]/input')  # sku折扣-设置sku折扣-折/减后规格2
    reduced_standard3 = (By.XPATH, '/html/body/ko-modal-sku-setting/div/div/div/div[3]/div[4]/ul/li[3]/div/div[5]/input')  # sku折扣-设置sku折扣-折/减后规格3
    bulk_discount = (By.XPATH, '/html/body/ko-modal-sku-setting/div/div/div/div[3]/div[4]/div[1]/div/form[1]/input')  # sku折扣设置-批量打折
    bulk_reduce_price = (By.XPATH, '/html/body/ko-modal-sku-setting/div/div/div/div[3]/div[4]/div[1]/div/form[2]/input')  # sku折扣设置-批量减价
    bulk_reduced_price = (By.XPATH, '/html/body/ko-modal-sku-setting/div/div/div/div[3]/div[4]/div[1]/div/form[3]/input') # sku折扣设置-批量设置减后价
    discount_certainly = (By.XPATH, '/html/body/ko-modal-sku-setting/div/div/div/div[3]/div[4]/div[1]/div/form[1]/div/button[2]')  # sku折扣设置-批量打折-确定
    reduce_certainly = (By.XPATH, '/html/body/ko-modal-sku-setting/div/div/div/div[3]/div[4]/div[1]/div/form[2]/div/button[2]')  # sku折扣设置-批量减价-确定
    reduced_certainly = (By.XPATH, '/html/body/ko-modal-sku-setting/div/div/div/div[3]/div[4]/div[1]/div/form[3]/div/button[2]')  # sku折扣设置-批量设置减后价-确定
    sku_erasure = (By.XPATH, '//*[@id="sku-settings-container"]/div/div/div[3]/div[4]/div[1]/div/div[3]/button[1]')  # sku折扣设置-抹分
    sku_make_turn = (By.XPATH, '//*[@id="sku-settings-container"]/div/div/div[3]/div[4]/div[1]/div/div[3]/button[2]')  # sku折扣设置-抹角
    sku_allclear = (By.XPATH, '//*[@id="sku-settings-container"]/div/div/div[3]/div[4]/div[1]/div/div[3]/div/button')  # sku折扣设置-清空
    skuone_clear = (By.XPATH, '//*[@id="discount-item-list"]/li[1]/div/button')  # sku折扣设置-单个清空
    sku_clear2 = (By.XPATH, '//*[@id="dialog176019-default-action"]')  # sku折扣设置 - 二次确认清空
    sku_certainly = (By.XPATH, '/html/body/ko-modal-sku-setting/div/div/div/div[5]/button[2]')  # sku折扣设置-整体弹框确定
    sku_cancel = (By.XPATH, '//*[@id="sku-settings-container"]/div/div/div[5]/button[1]') # sku折扣设置-整体弹框取消

    lowest_price = (By.XPATH,'//*[@id="act-step-3"]/div[5]/div[1]/a')  # 设置商品折扣页-显示所有最低价sku
    bulk_discount2 = (By.XPATH, '//*[@id="input_discount_all"]')  # 设置所有商品最低价sku折扣-批量打折
    bulk_reduce_price2 = (By.XPATH, '//*[@id="input_decrease_all"]')  # 设置所有商品最低价sku折扣-批量减价
    bulk_reduced_price2 = (By.XPATH, '//*[@id="input_final_price_all"]')  # 设置所有商品最低价sku折扣 -批量设置减后价
    discount_certainly2 = (By.XPATH,'//*[@id="lowest-sku-settings-container"]/div/div/div[3]/div[4]/div[1]/div/form[1]/div/button[2]')  # 设置所有商品最低价sku折扣-批量打折-确定
    reduce_certainly2 = (By.XPATH, '//*[@id="lowest-sku-settings-container"]/div/div/div[3]/div[4]/div[1]/div/form[2]/div/button[2]')  # 设置所有商品最低价sku折扣-批量减价-确定
    reduced_certainly2 = (By.XPATH, '//*[@id="lowest-sku-settings-container"]/div/div/div[3]/div[4]/div[1]/div/form[3]/div/button[2]')  # 设置所有商品最低价sku折扣-批量设置减后价-确定
    sku_erasure2 = (By.XPATH, '//*[@id="lowest-sku-settings-container"]/div/div/div[3]/div[4]/div[1]/div/div/button[1]')  # sku折扣设置-抹分
    sku_make_turn2 = (By.XPATH, '//*[@id="lowest-sku-settings-container"]/div/div/div[3]/div[4]/div[1]/div/div/button[1]')  # sku折扣设置-抹角
    all_clear = (By.XPATH, '//*[@id="lowest-sku-settings-container"]/div/div/div[3]/div[4]/div[1]/div/div/div/button')  # 设置所有商品的最低价sku折扣-清空/批量清空
    one_clear = (By.XPATH, '//*[@id="discount-item-list"]/li/div/button')  # sku折扣设置-单个清空
    clear_up2 = (By.XPATH, '//*[@id="dialog192610-default-action"]')  # sku折扣设置-二次确认清空
    lowest_certainly = (By.XPATH, '//*[@id="lowest-sku-settings-container"]/div/div/div[5]/button[2]')  # sku折扣设置-显示最低价sku-整体弹框确定
    lowest_cancel = (By.XPATH, '//*[@id="lowest-sku-settings-container"]/div/div/div[5]/button[1]') # sku折扣设置-显示最低价sku-整体弹框取消


class circulate_discount():  # 循环打折
    display_price = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div/div[1]/div[1]/div[2]/div/div/label[1]/div/i')  # 循环折扣-搜索页显示折扣价
    hide_price = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div/div[1]/div[1]/div[2]/div/div/label[2]/div/span/span')  # 循环折扣-搜索页不显示折扣价
    cycle_tuesday = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div/div[5]/div[1]/div[2]/div/div/label[2]/div/i') # 循环折扣-活动周期【周二】
    cycle_wednesday = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div/div[5]/div[1]/div[2]/div/div/label[3]/div')  # 循环折扣-活动周期【周三】
    all_cycle = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div/div[5]/div[1]/div[2]/div/div/label[8]/div') # 循环折扣-活动周期全选

    add_activity_period2 = (By.XPATH,'//*[@id="main-content"]/div/div[2]/div/div[6]/div[1]/div[2]/div/div/div/div[2]/a/span')  # 循环折扣-显示下的增加活动时段2
    add_activity_period3 = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div/div[6]/div[1]/div[2]/div/div/div/div[3]/a/span')   #循环折扣-显示下增加活动时段3
    start_time1 = (By.XPATH,'//*[@id="main-content"]/div/div[2]/div/div[6]/div[1]/div[2]/div/div/div/div[1]/div/div[1]/input')  # 循环折扣-活动时段1的开始时间
    end_time1 = (By.XPATH,'//*[@id="main-content"]/div/div[2]/div/div[6]/div[1]/div[2]/div/div/div/div[1]/div/div[2]/input')  # 循环折扣-活动时间1的结束时间
    start_time2 = (By.XPATH,'//*[@id="main-content"]/div/div[2]/div/div[6]/div[1]/div[2]/div/div/div/div[2]/div/div[1]/input')  # 循环折扣-活动时段2的开始时间
    end_time2 = (By.XPATH,'//*[@id="main-content"]/div/div[2]/div/div[6]/div[1]/div[2]/div/div/div/div[2]/div/div[2]/input')  # 循环折扣-活动时段2的结束时间
    start_time3 = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div/div[6]/div[1]/div[2]/div/div/div/div[3]/div/div[1]/input')  # 循环折扣-活动时段3的开始时间
    end_time3 = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div/div[6]/div[1]/div[2]/div/div/div/div[3]/div/div[2]/input')  # 循环折扣-活动时段3的结束时间

    un_add_activity_period = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[2]/div[6]/div[1]/div[2]/div/div/div/div[2]/a/span')   # 循环折扣-不显示下的增加活动时段
    un_start_time1 = (By.XPATH,'//*[@id="main-content"]/div/div[2]/div[2]/div[6]/div[1]/div[2]/div/div/div/div[1]/div/div[1]/input')  # 循环折扣-不显示下活动时段1的开始时间
    un_end_time1 = (By.XPATH,'//*[@id="main-content"]/div/div[2]/div[2]/div[6]/div[1]/div[2]/div/div/div/div[1]/div/div[2]/input')  # 循环折扣-不显示下活动时间1的结束时间
    un_discounts1 = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[2]/div[6]/div[1]/div[2]/div/div/div/div[1]/div/label[1]/div/div/input')  # 循环折扣-不显示时段1下折扣
    un_reduce_price1 = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[2]/div[6]/div[1]/div[2]/div/div/div/div[1]/div/label[2]/div/div/input')  # 循环折扣-不显示时段1下减价
    un_start_time2 = (By.XPATH,'//*[@id="main-content"]/div/div[2]/div[2]/div[6]/div[1]/div[2]/div/div/div/div[2]/div/div[1]/input')  # 循环折扣-不显示下活动时段2的开始时间
    un_end_time2 = (By.XPATH,'//*[@id="main-content"]/div/div[2]/div[2]/div[6]/div[1]/div[2]/div/div/div/div[2]/div/div[2]/input')  # 循环折扣-不显示下活动时段2的结束时间
    un_discounts2 = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[2]/div[6]/div[1]/div[2]/div/div/div/div[2]/div/label[1]/div/div/input')  # 循环折扣-不显示时段2下折扣
    un_reduce_price2 = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[2]/div[6]/div[1]/div[2]/div/div/div/div[2]/div/label[2]/div/div/input')  # 循环折扣-不显示时段2下减价
    un_start_time3 = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[2]/div[6]/div[1]/div[2]/div/div/div/div[3]/div/div[1]/input')  # 循环折扣-不显示下活动时段3的开始时间
    un_end_time3 = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[2]/div[6]/div[1]/div[2]/div/div/div/div[3]/div/div[2]/input')  # 循环折扣-不显示下活动时段3的结束时间
    un_discounts3 = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[2]/div[6]/div[1]/div[2]/div/div/div/div[3]/div/label[1]/div/div/input')  # 循环折扣-不显示时段2下折扣
    un_reduce_price3 = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[2]/div[6]/div[1]/div[2]/div/div/div/div[3]/div/label[2]/div/div/input')  # 循环折扣-不显示时段2下减价
    next_produce = (By.XPATH,'//*[@id="main-content"]/div/div[2]/div/div[10]/button')  # 下一步 选择活动商品
    next_discount = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[3]/button[2]')     # 下一步设置商品折扣
    next_complete = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[4]/button[2]')  # 下一步设置商品折扣

    bulk_discount = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[2]/div[1]/div[2]/input')     # 循环打折-设置商品折扣页-批量设置打折框
    bulk_discount_certain = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[2]/div[1]/div[3]/button[2]')     # 循环打折-设置商品折扣页-批量打折确定框
    bulk_discount_cannel = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[2]/div[1]/div[3]/button[1]')     # 循环打折-设置商品折扣页-批量打折取消框
    bulk_reduce_price = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[2]/div[2]/div[2]/input')     # 循环打折-设置商品折扣页-批量设置减价框
    bulk_reduce_certain = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[2]/div[2]/div[3]/button[2]')     # 循环打折-设置商品折扣页-批量减价确定框
    bulk_reduce_cannel = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[2]/div[2]/div[3]/button[1]')     # 循环打折-设置商品折扣页-批量减价取消框
    after_bulk_reduce = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[2]/div[3]/div[2]/input')     # 循环打折-设置商品折扣页-批量设置减后价
    after_bulk_certain = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[2]/div[3]/div[3]/button[2]')     # 循环打折-设置商品折扣页-批量减后价确定框
    after_bulk_cannel = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[2]/div[3]/div[3]/button[1]')     # 循环打折-设置商品折扣页-批量减后价取消框
    one_discount = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[3]/div[1]/div[4]/div[2]/input')    # 单个商品打折框
    one_reduce = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[3]/div[1]/div[5]/div[2]/input')     # 单个商品减价框
    one_after_reduce = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[3]/div[1]/div[6]/div[2]/input')   # 单个商品减后价框

    next_period = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[4]/button[2]')  # 循环折扣-下一步设置时段2的折扣
    cir_erasure = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[2]/div[4]/button[1]')  # 循环折扣-批量设置商品下的抹分
    cir_make_turn = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[2]/div[4]/button[2]')  # 循环折扣-批量设置商品下的抹角
    cir_erasure2 = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[2]/div[1]/div[3]/button[2]')  #循环折扣- 无sku商品下的抹分
    cir_make_turn2 = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[2]/button[2]')  # 循环折扣-无sku商品下的抹角
    select_product1 = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[2]/div[3]/div[1]/div[1]/div[3]/button')  # 商品1
    select_product2 = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/button')  # 商品2
    select_product3 = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[3]/button')  # 商品3
    select_product4 = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[2]/div[3]/div[2]/div[2]/div[3]/button')  # 商品4
    select_product5 = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[3]/button')  # 商品5
    select_product6 = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[2]/div[3]/div[3]/div[2]/div[3]/button')  # 商品6
    assert_0 = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[1]/div[1]/div[1]/span/span') #活动创建成功断言

class full_reduction():   # 满减满包邮
    select_product1 = (By.XPATH, '//*[@id="act-item-selector"]/ko-item-selector/div/div[6]/div/div[1]/div/div[3]/a')  # 商品1
    select_product2 = (By.XPATH, '//*[@id="act-item-selector"]/ko-item-selector/div/div[6]/div/div[2]/div/div[3]/a')  # 商品2
    select_product3 = (By.XPATH, '//*[@id="act-item-selector"]/ko-item-selector/div/div[6]/div/div[3]/div/div[3]/a')  # 商品3
    select_product4 = (By.XPATH, '//*[@id="act-item-selector"]/ko-item-selector/div/div[6]/div/div[4]/div/div[3]/a')  # 商品4
    select_product5 = (By.XPATH, '//*[@id="act-item-selector"]/ko-item-selector/div/div[6]/div/div[5]/div/div[3]/a')  # 商品5
    select_product6 = (By.XPATH, '//*[@id="act-item-selector"]/ko-item-selector/div/div[6]/div/div[6]/div/div[3]/a')  # 商品6
    exclusive_version = (By.XPATH, '//*[@id="mj-type"]/div[2]/div[2]')  # 尊享版
    activity_label = (By.XPATH, '//*[@id="act-title-form-group"]/div[3]/div[1]/div[1]/ko-dropdown-list')    # 活动标签 - 下拉框选择标签
    discount_promotion = (By.XPATH, '//*[@id="act-title-form-group"]/div[3]/div[1]/div[1]/ko-dropdown-list/div/ul/li[1]/a')   # 活动标签-优惠促销
    full_reduction_promotion = (By.XPATH, '//*[@id="act-title-form-group"]/div[3]/div[1]/div[1]/ko-dropdown-list/div/ul/li[2]/a')   # 活动标签-满减促销
    full_package_shipping = (By.XPATH, '//*[@id="act-title-form-group"]/div[3]/div[1]/div[1]/ko-dropdown-list/div/ul/li[3]/a')   # 活动标签-满就包邮
    full_gifts = (By.XPATH, '//*[@id="dropdown716"]/span')   # 活动标签-满就送礼
    select_custom = (By.XPATH, '//*[@id="act-title-form-group"]/div[3]/div[1]/div[1]/ko-dropdown-list/div/ul/li[5]/a')   # 活动标签-下拉框选择自定义
    click_custom = (By.XPATH, '//*[@id="act-title-form-group"]/div[3]/div[1]/div[2]/a')   # 活动标签-点击自定义
    custom_input = (By.XPATH, '//*[@id="act-custom-title"]')   # 活动标签-自定义输入框
    next_produce = (By.XPATH, '//*[@id="act-step-1"]/div[2]/a[2]')  # 下一步 选择活动商品
    next_activate = (By.XPATH, '//*[@id="act-step-2"]/div[3]/a[2]')  # 下一步 设置活动详情
    next_complete = (By.XPATH, '//*[@id="act-step-3"]/div[5]/a[2]')  # 完成并提交
    add_many_preferential = (By.XPATH, '//*[@id="act-step-3"]/div[1]/ul/li[2]/label/a')   # 设置活动详情-添加多级优惠
    full_yuan = (By.XPATH, '//*[@id="condition-totalPrice"]')   # 条件1置活动详情-满x元
    full_jian = (By.XPATH, '//*[@id="condition-count"]')   # 条件1设置活动详情-满y件
    full_yuan_jian1 = (By.XPATH, '//*[@id="condition-YJPrice"]')   # 条件1设置活动详情-满x元且满y件
    full_yuan_jian2 = (By.XPATH, '//*[@id="condition-YJCount"]')   # 条件1设置活动详情-满x件且满y件
    reduce_price = (By.XPATH, '//*[@id="decreaseMoney"]')   # 内容1置活动详情-减x元
    discount_price = (By.XPATH, '//*[@id="discountRate"]')   # 内容1设置活动详情-打y折
    free_shipping = (By.XPATH, '//*[@id="act-detail-pane"]/div/div[4]/div/div[3]/label[2]')   # 内容1设置活动详情-包邮
    give_gifts = (By.XPATH, '//*[@id="act-detail-pane"]/div/div[4]/div/div[4]/label[2]')   # 内容1设置活动详情-送礼物
    gifts_name = (By.XPATH, '//*[@id="giftName"]')   # 内容1设置活动详情-输入礼物名称
    no_banner = (By.XPATH, '//*[@id="act-detail-pane"]/div/div[4]/div/div[3]/label[2]')   # 设置活动详情-不显示横幅
    banner_orange = (By.XPATH, '//*[@id="act-detail-pane"]/div/div[4]/div/div[4]/label[2]')   # 设置活动详情-活力橙横幅
    banner_red = (By.XPATH, '//*[@id="act-step-3"]/div[3]/div[1]/ul/li[3]/a')  # 设置活动详情-节日红横幅
    banner_simple = (By.XPATH, '//*[@id="act-step-3"]/div[3]/div[1]/ul/li[4]/a')  # 设置活动详情-轻盈简约
    banner_gold = (By.XPATH, '//*[@id="act-step-3"]/div[3]/div[1]/ul/li[5]/a')   # 设置活动详情-淡雅金
    banner_pink = (By.XPATH, '//*[@id="act-step-3"]/div[3]/div[1]/ul/li[6]/a')   # 设置活动详情-浅桃红
    pop1 = (By.XPATH, '//*[@id="mjsPage"]/div[12]/div/div/button')   #商品弹窗关闭键
    assert_0 = (By.XPATH, '//*[@id="act-step-4"]/div/div[1]/div/div[1]/div/span[1]') #活动创建成功文本断言

class second_sell():   # 第二件促销
    next_produce = (By.XPATH, '//*[@id="act-step-1"]/div[2]/div/a')  # 下一步 选择活动商品
    next_discount = (By.XPATH, '//*[@id="act-step-2"]/div[2]/div/a[2]')  # 下一步 设置商品折扣
    complete = (By.XPATH, '//*[@id="act-step-3"]/div[7]/div/a[2]')  # 完成并提交
    batch_settings_half = (By.XPATH, '//*[@id="act-step-3"]/div[4]/div/div[1]/button[1]')  # 批量设置-第二件半价
    batch_settings_0 = (By.XPATH, '//*[@id="act-step-3"]/div[4]/div/div[1]/button[2]')  # 批量设置-第二件0元
    batch_settings_1 = (By.XPATH, '//*[@id="act-step-3"]/div[4]/div/div[1]/button[3]')  # 批量设置-第二件1元
    batch_two_packs_full = (By.XPATH, '//*[@id="act-step-3"]/div[4]/div/div[2]/label[1]/span')  # 批量设置-满两件包邮
    batch_choose_area = (By.XPATH, '//*[@id="act-step-3"]/div[4]/div/div[2]/label[1]/a')  # 批量设置-设置地区
    select_all = (By.XPATH, '//*[@id="area-selector-container"]/ko-area-selector/div/div[1]/div/a[1]')  # 设置地区-全选
    deselect_all = (By.XPATH, '//*[@id="area-selector-container"]/ko-area-selector/div/div[1]/div/a[2]')  # 设置地区-全不选
    last_used = (By.XPATH, '//*[@id="area-selector-container"]/ko-area-selector/div/div[1]/div/a[6]')  # 设置地区-上次使用的包邮地区
    batch_second_discount = (By.XPATH, '//*[@id="act-step-3"]/div[4]/div/div[2]/label[2]/span[1]')  # 批量设置-第二件优惠上不封顶

    alone_first_price = (By.XPATH, '//*[@id="act-step-3"]/ul/li[1]/div/div[4]/input')  # 单独商品设置-第一件价格框
    alone_settings_half = (By.XPATH, '//*[@id="act-step-3"]/ul/li[1]/div/div[5]/div/button[1]')  # 单独商品1设置-第二件半价
    alone_batch_settings_0 = (By.XPATH, '//*[@id="act-step-3"]/ul/li[1]/div/div[5]/div/button[2]')  # 单独商品1设置-第二件0元
    alone_batch_settings_1 = (By.XPATH, '//*[@id="act-step-3"]/ul/li[1]/div/div[5]/div/button[3]')  # 单独商品1设置-第二件1元
    alone_two_packs_full = (By.XPATH, '//*[@id="act-step-3"]/ul/li[1]/div/div[6]/label[1]/span')  # 单独商品1设置-满两件包邮
    choose_area = (By.XPATH, '//*[@id="act-step-3"]/ul/li[2]/div/div[6]/label[2]/span')  # 单独商品1设置-设置地区

    alone_settings_half2 = (By.XPATH, '//*[@id="act-step-3"]/ul/li[2]/div/div[5]/div/button[1]')  # 单独商品2设置-第二件半价
    alone_batch_settings2_0 = (By.XPATH, '//*[@id="act-step-3"]/ul/li[2]/div/div[5]/div/button[2]')  # 单独商品2设置-第二件0元
    alone_batch_settings2_1 = (By.XPATH, '//*[@id="act-step-3"]/ul/li[2]/div/div[5]/div/button[3]')  # 单独商品2设置-第二件1元
    alone_two_packs_full2 = (By.XPATH, '//*[@id="act-step-3"]/ul/li[2]/div/div[6]/label[1]/span')  # 单独商品2设置-满两件包邮
    choose_area2 = (By.XPATH, '//*[@id="act-step-3"]/ul/li[2]/div/div[6]/label[1]/a')  # 单独商品2设置-设置地区
    alone_second_discount1 = (By.XPATH, '//*[@id="act-step-3"]/ul/li[2]/div/div[6]/label[2]/span')  # 单独商品1设置-第二件优惠上不封顶

    xinjiang = (
    By.XPATH, '//*[@id="area-selector-container"]/ko-area-selector/div/div[2]/div[1]/div/label/span')  # 设置地区-藏疆地区
    north_china = (
    By.XPATH, '//*[@id="area-selector-container"]/ko-area-selector/div/div[3]/div[1]/div/label/span')  # 设置地区-华北地区
    northeast_china = (
    By.XPATH, '//*[@id="area-selector-container"]/ko-area-selector/div/div[4]/div[1]/div/label/span')  # 设置地区-东北地区
    east_china = (
    By.XPATH, '//*[@id="area-selector-container"]/ko-area-selector/div/div[5]/div[1]/div/label/span')  # 设置地区-华东地区
    central_china = (
    By.XPATH, '//*[@id="area-selector-container"]/ko-area-selector/div/div[6]/div[1]/div/label/span')  # 设置地区-华中地区
    south_china = (
    By.XPATH, '//*[@id="area-selector-container"]/ko-area-selector/div/div[7]/div[1]/div/label/span')  # 设置地区-华南地区
    southwest_china = (
    By.XPATH, '//*[@id="area-selector-container"]/ko-area-selector/div/div[6]/div[1]/div/label/span')  # 设置地区-华中地区
    northwest_china = (
    By.XPATH, '//*[@id="area-selector-container"]/ko-area-selector/div/div[7]/div[1]/div/label/span')  # 设置地区-华南地区
    certainly = (By.XPATH, '//*[@id="area-selector-modal"]/div/div/div[3]/a')  # 设置地区-确定框


class whole_store_discount():   # 全店折扣/减价
    discount_input = (By.XPATH, '//*[@id="fd-value-form-group"]/div[2]/label[1]/input[2]')  # 全店优惠-打折输入框
    reduce_price_input = (By.XPATH, '//*[@id="fd-value-form-group"]/div[2]/label[2]/input[2]')  # 全店优惠-满减输入框
    click_create_activity = (By.XPATH, '//*[@id="act-step-1"]/div[2]/div/a')  # 点击直接创建全店折扣/减价活动
    first_discount = (By.XPATH, '//*[@id="zhekou-buy-limit-form-group"]/div[2]/label[2]')  # 首件优惠
    assert_0 = (By.XPATH, '//*[@id="act-step-4"]/div/div[1]/div/div[1]/div/span')  # 断言活动创建成功
    pop1 = (By.XPATH, '//*[@id="fzhekouPage"]/div[12]/div/div/button')  # 表扬一下弹窗关闭按钮

class whole_store_freeshipping():    # 全店满减/包邮  具体流程用例和满减/包邮相同~不重复写
    activity_label = (By.XPATH, '//*[@id="dropdown246"]')    # 活动标签 - 下拉框选择标签
    discount_promotion = (By.XPATH, '//*[@id="act-title-form-group"]/div[3]/div[1]/div[1]/ko-dropdown-list/div/ul/li[1]/a')   # 活动标签-优惠促销
    full_reduction_promotion = (By.XPATH, '//*[@id="act-title-form-group"]/div[3]/div[1]/div[1]/ko-dropdown-list/div/ul/li[2]/a')   # 活动标签-满减促销
    full_package_shipping = (By.XPATH, '//*[@id="act-title-form-group"]/div[3]/div[1]/div[1]/ko-dropdown-list/div/ul/li[3]/a')   # 活动标签-满就包邮
    full_gifts = (By.XPATH, '//*[@id="act-title-form-group"]/div[3]/div[1]/div[1]/ko-dropdown-list/div/ul/li[4]/a')   # 活动标签-满就送礼
    select_custom = (By.XPATH, '//*[@id="act-title-form-group"]/div[3]/div[1]/div[1]/ko-dropdown-list/div/ul/li[5]/a')   # 活动标签-下拉框选择自定义
    click_custom = (By.XPATH, '//*[@id="act-title-form-group"]/div[3]/div[1]/div[2]/a')   # 活动标签-点击自定义
    custom_input = (By.XPATH, '//*[@id="act-custom-title"]')   # 活动标签-自定义输入框
    next_activate = (By.XPATH, '//*[@id="act-step-1"]/div[2]/a')  # 下一步 设置活动详情
    add_many_preferential = (By.XPATH, '//*[@id="act-step-3"]/div[1]/ul/li[2]/label/a')   # 设置活动详情-添加多级优惠
    full_yuan = (By.XPATH, '//*[@id="condition-totalPrice"]')   # 条件1置活动详情-满x元
    full_jian = (By.XPATH, '//*[@id="condition-count"]')   # 条件1设置活动详情-满y件

    reduce_price = (By.XPATH, '//*[@id="decreaseMoney"]')   # 内容1置活动详情-减x元
    discount_price = (By.XPATH, '//*[@id="discountRate"]')   # 内容1设置活动详情-打y折
    free_shipping = (By.XPATH, '//*[@id="act-detail-pane"]/div/div[4]/div/div[3]/label[1]/span')   # 内容1设置活动详情-包邮
    give_gifts = (By.XPATH, '//*[@id="act-detail-pane"]/div/div[4]/div/div[4]/label[1]/span')   # 内容1设置活动详情-送礼物
    gifts_name = (By.XPATH, '//*[@id="giftName"]')   # 内容1设置活动详情-输入礼物名称
    no_banner = (By.XPATH, '//*[@id="act-step-3"]/div[3]/div[1]/ul/li[1]/a')   # 设置活动详情-不显示横幅
    banner_orange = (By.XPATH, '//*[@id="act-step-3"]/div[3]/div[1]/ul/li[2]/a')   # 设置活动详情-活力橙横幅

    banner_red = (By.XPATH, '//*[@id="act-step-3"]/div[3]/div[1]/ul/li[3]/a')  # 设置活动详情-节日红横幅
    banner_simple = (By.XPATH, '//*[@id="act-step-3"]/div[3]/div[1]/ul/li[4]/a')  # 设置活动详情-轻盈简约
    banner_gold = (By.XPATH, '//*[@id="act-step-3"]/div[3]/div[1]/ul/li[5]/a')   # 设置活动详情-淡雅金
    banner_pink = (By.XPATH, '//*[@id="act-step-3"]/div[3]/div[1]/ul/li[6]/a')   # 设置活动详情-浅桃红
    next_complete = (By.XPATH, '//*[@id="act-step-3"]/div[5]/a[2]')   #完成并提交
    assert_0 = (By.XPATH, '//*[@id="act-step-4"]/div/div[1]/div/div[1]/div/span')   #断言活动创建成功
    pop1 = (By.XPATH, '//*[@id="fmjsPage"]/div[12]/div/div/button') #表扬一下弹窗关闭按钮


class discount_up():     # 定时折上折
    next_produce = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div/button')  # 下一步 选择活动商品
    next_discount = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[2]/button[2]')  # 下一步 设置商品折扣
    complete = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[4]/button[2]')  # 完成并提交
    discount_up_pop = (By.XPATH, '//*[@id="component_navbar"]/div[1]/div/i')  # 弹窗
    select_active = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[1]/div[2]/div[1]/div/div[1]')  # 选择活动
    next1 = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div/button')  # 下一步选择活动商品
    select_doing = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[1]/div[2]/div[1]/div/div[2]/div[2]')  # 选择进行中的活动
    select_shop = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[1]/div[2]/div[4]/div/div/div[3]/button')  # 选择商品，第一个
    next2 = (By.XPATH,'//*[@id="main-content"]/div/div[2]/div[2]/button[2]')  # 下一步
    cut = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[2]/input')  # 折上减几元
    discount = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]/div[1]/div[2]/input')  # 打几折
    ok = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[4]/button[2]')  # 完成并提交
    assert_ele = (By.XPATH, '//*[@id="main-content"]/div/div[2]/div[1]/div[1]/div[1]/span/span')  # 活动创建成功

