from selenium.webdriver.common.by import By

"""项目配置地址"""

url = 'https://pre-admin.hndt.com/home'

# 节目制作账号
pmake_username = '19977777777'
# 节目制作secret
pmake_secret = 'NE4WEQJZ7UTZGKRYUR5PTGOGU5OJ2ZIG'

# 节目审核技审账号
check_username = '19966666666'
# 节目制作secret
check_secret = 'RCB6OQKKHOFDLJ5OMPRI3HDEJFKT2YRO'

# 节目终审账号
check_fin_username = '19955555555'
# 节目制作secret
check_fin_secret = 'N4REOGIS6CXODN34HRYO7F7L3VVFDB4O'

# 测试密码
test_pwd = '123456'


"""以下为登录页面元素配置信息"""

# 用户名
login_username = By.ID, "usernameVal"
# 密码
login_pwd = By.ID, "passVal"
# 登录按钮
login_btn = By.CSS_SELECTOR, "#submit"
# 登录提示信息
login_message = By.XPATH, "//div[@class='layui-layer-content']"
# 验证码
login_verify_code = By.ID, "codeNum"
# 验证码确定按钮
login_code_btn = By.XPATH, "//a[@class='layui-layer-btn0']"
# 验证码取消按钮
login_code_cancel_btn = By.XPATH, "//a[@class='layui-layer-btn1']"


""" Home 页面 """

# 节目制作菜单按钮
home_pmake_btn = By.XPATH, '//*[text()="节目制作"]'


"""节目制作-工程文件"""

# 工程文件菜单按钮
pmake_project_btn = By.XPATH, '//*[text()="工程文件"]'

# 最新工程编辑按钮
pmake_project1_edit_btn = By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div/button[1]/span'

# 搜索框
pmake_project_search = By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[1]/form/div[1]/div/div/input'

# 搜索按钮
pmake_project_search_btn = By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[1]/form/div[3]/div/button[1]'

# 工程文件复制按钮
pmake_project1_copy_btn = By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div/button[2]/span'

# 工程文件复制文件名称输入框
pmake_project1_copy_name = By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[5]/div/div/div[2]/div/form/div/div/div/input'

# 工程文件复制文件确定按钮
pmake_project1_copy_name_btn = By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[5]/div/div/div[3]/div/button[2]'

# 重置按钮
pmake_project_reset = By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/div[2]/section/div/div/div[3]/div/div[1]/form/div[3]/div/button[2]'

# 最新节目工程名称
pmake_project1_name = By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div'

# 次新节目工程名称
pmake_project2_name = By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[2]/div'

# # 最新节目按钮
# pmake_project1_check_btn = By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div/button[1]'

# 列表节目工程名称
pmake_project_name_list = [By.XPATH, '//tr[{}]//td[2]//div[1]']



"""云剪辑"""

# 时间线字幕片段
mskj_timeline_subtitles = By.XPATH, "//div[@class='clip-item_text']"
    # By.XPATH, '/html/body/div/div[7]/div[2]/div[1]/div[2]/div/div[5]/div[1]/div/div/div[3]/span[1]'

# 时间线字幕片段鼠标双击文本元素
mskj_timeline_subtitles_mouse = By.XPATH, '//*[@id="0,0,clip"]/div[3]/span[1]'

# 字幕文本输入框
mskj_subtitles_text = By.XPATH, '//*[@id="panel"]/div[12]/div[1]/div/div/div[2]/div[1]/div[1]/textarea'

# 字幕向下居中按钮
mskj_subtitles_centerdown = By.XPATH, '//*[@id="panel"]/div[12]/div[1]/div/div/div[2]/div[1]/div[8]/div[2]/table/tr[3]/td[2]'

# 工程保存菜单
mskj_pro_save_menu = By.CSS_SELECTOR, '#title-bar > div.general-dropdown.el-dropdown'

# 保存菜单保存按钮
mskj_pro_save_menu_save_btn = By.XPATH, '/html/body/ul/li[1]/span'

# 导出视频按钮
mskj_pro_export_btn = By.XPATH, '/html/body/div/div[3]/div/button[2]'

# 导出视频名称输入框
mskj_pro_export_name = By.XPATH, '/html/body/div/section/main/div/div[2]/div[1]/div[1]/div[2]/input'

# 电视播出选项
mskj_pro_export_tv = By.XPATH, '/html/body/div/section/main/div/div[2]/div[1]/div[3]/div[2]/label[2]/span[2]'

# 获取封面按钮
mskj_pro_export_get_cover_btn = By.XPATH, '/html/body/div/section/main/div/div[2]/div[1]/div[5]/div[3]/button[1]'

# 提交审核按钮
mskj_pro_export_check_btn = By.XPATH, "/html/body/div[1]/section/footer/button[1]/span"

# 日期选择框
mskj_binding_date = By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div[1]/form/div[3]/div/div/input'

# 日期选择框月份按钮
mskj_binding_date_month_btn = By.XPATH, '/html/body/div[4]/div[1]/div/div[1]/span[2]'

# 选择对应月份
mskj_binding_date_select_month = [By.LINK_TEXT, '{}']

# 选择对应日期
mskj_binding_date_select_day = [By.XPATH, '//td[@class="available"]//div//span[contains(text(),{})]']

# 绑定节目列表首条节目日期
mskj_binding_pro1_date = By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[4]/div'

# 绑定节目列表首条节目名称
mskj_binding_pro1_name = By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[1]/div'

# 绑定节目列表次条节目日期
mskj_binding_pro2_name = By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div[2]/div[3]/table/tbody/tr[2]/td[1]/div'

# 绑定按钮1
mskj_binding1_btn = By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[5]/div/button/span'

# 绑定按钮2
mskj_binding2_btn = By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div[2]/div[3]/table/tbody/tr[2]/td[5]/div/button/span'

# 节目绑定提交按钮
mskj_binding_submit_btn = By.XPATH, '/html/body/div[4]/div/div[3]/div/button[2]/span'

# 节目绑定完成提示
mskj_binding_complete_message = By.XPATH, '/html/body/div[6]'

# 审核通过按钮
mskj_pro_check_pass_btn = By.XPATH, '/html/body/div/div[5]/div[1]/div[2]/div[3]/button[1]'

# 操作完成提示信息
mskj_result_message = By.XPATH, '/html/body/div[6]'


"""节目制作-待审节目"""

# 待审节目菜单按钮
pmake_prog2check_btn = By.XPATH, '//*[text()="待审节目"]'

# 节目列表首条节目审核状态
pmake_prog2check_pro1_state = By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[9]/div/span[5]'

# 节目列表首条节目名称
pmake_prog2check_pro1_name = By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div'

# 节目列表首条节目日期
pmake_prog2check_pro1_date = By.XPATH ,'/html/body/div[1]/section/main/div/div/div/div/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div'

# 审核按钮
pmake_prog2check_check_btn = By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/div[2]/section/div/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[10]/div/button'

# 技审确认按钮
pmake_prog2check_confirm_btn = By.XPATH, "//div[@class='el-dialog']//span//span"

# 技审确认/终审 通过按钮
pmake_prog2check_check_pass_btn = By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/div[2]/section/div/div[2]/button[1]'





# # 获取异常文本信息
# login_err_info = By.CSS_SELECTOR, ".layui-layer-content"
# # 点击异常提示框 按钮
# login_err_btn_ok = By.CSS_SELECTOR, ".layui-layer-btn0"
# # 安全退出
# login_logout = By.PARTIAL_LINK_TEXT, "安全退出"
