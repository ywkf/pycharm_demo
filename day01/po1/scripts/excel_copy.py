import operator
from time import sleep

from select import select
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from dtd import Dtd
from excel01 import excel_tag

driver = webdriver.Chrome()
driver.maximize_window()
# driver.implicitly_wait(10)


url = 'https://pre-admin.hndt.com/home'
driver.get(url)
driver.find_element(By.CSS_SELECTOR, '#usernameVal').send_keys('19977777777')
driver.find_element(By.CSS_SELECTOR, '#passVal').send_keys('123456')
driver.find_element(By.CSS_SELECTOR, '#submit').click()
code = input('input:')

driver.find_element(By.CSS_SELECTOR, '#codeNum').send_keys(code)
driver.find_element(By.XPATH, '//*[@id="layui-layer1"]/div[3]/a[1]').click()

action = ActionChains(driver)



# 节目制作
WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '//*[text()="节目制作"]'))
driver.find_element(By.XPATH, '//*[text()="节目制作"]').click()

sleep(2)
handles = driver.window_handles
print(handles)
driver.switch_to.window(handles[1])

# list0 = [{'tag': '060201好剧连连看-1致命名单', 'time': '01:00:00', 'copy_name': '000000好剧连连看-1'}, {'tag': '060202好剧连连看-2致命名单', 'time': '00:50:00', 'copy_name': '000000好剧连连看-2'}]

# list0 = [{'tag': '060201好剧连连看-1剿匪英雄', 'time': '01:00:00', 'month': '2 月', 'day': '2', 'date': '2022-06-02'},
#          {'tag': '060202好剧连连看-2剿匪英雄', 'time': '00:50:00', 'month': '2 月', 'day': '2', 'date': '2022-06-02'}]

# list0 = [{'tag': '072302好剧连连看-2致命名单', 'time': '00:50:00', 'copy_name': '000000好剧连连看-2', 'month': '7 月', 'day': '23', 'date': '2022-07-23'}]

list0 = excel_tag()

# tag 列表
list_tag = []
for j in list0:
    list_tag.append(j.get('tag'))
#     tag_name = j.get('tag')[6:]
#     if operator.contains(tag_name, '好剧'):
#         tag_name = tag_name[:7]
#     elif operator.contains(tag_name, '剧场'):
#         tag_name = tag_name[:8]
#     tag_name = '000000' + tag_name
#     list_tag.append(tag_name)
#     print(tag_name)

# 工程文件
driver.find_element(By.XPATH, '//*[text()="工程文件"]').click()
# 编辑
WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div/button[1]/span'))
driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div/button[1]/span').click()
# 返回
sleep(10)
driver.back()


# 搜索
def search_tag(i):

    # 搜索框
    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[1]/form/div[1]/div/div/input'))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[1]/form/div[1]/div/div/input').clear()
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[1]/form/div[1]/div/div/input').send_keys(i.get('copy_name'))
    # 搜索
    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[1]/form/div[3]/div/button[1]'))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[1]/form/div[3]/div/button[1]').click()
    sleep(2)


# 复制工程
def copy_pro(i):

    sleep(1)
    # 复制
    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div/button[2]/span'))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div/button[2]/span').click()
    # 名称
    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[5]/div/div/div[2]/div/form/div/div/div/input'))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[5]/div/div/div[2]/div/form/div/div/div/input').clear()
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[5]/div/div/div[2]/div/form/div/div/div/input').send_keys(i.get('tag'))
    # 确定
    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[5]/div/div/div[3]/div/button[2]'))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[5]/div/div/div[3]/div/button[2]').click()
    print('copy success ', i.get('tag'))
    sleep(2)
    driver.refresh()
    sleep(3)
    # 重置
    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/div[2]/section/div/div/div[3]/div/div[1]/form/div[3]/div/button[2]'))
    driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/div[2]/section/div/div/div[3]/div/div[1]/form/div[3]/div/button[2]').click()
    print('reset')
    # # 重置
    # WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '/html/body/div/section/main/div/div/div/div/div[2]/section/div/div/div[3]/div/div[1]/form/div[3]/div/button[2]/span'))
    # driver.find_element(By.XPATH, '/html/body/div/section/main/div/div/div/div/div[2]/section/div/div/div[3]/div/div[1]/form/div[3]/div/button[2]/span').click()

# # 创建工程
# def create_test(i):
#     # 新建
#     WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/button'))
#     driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/button').click()
#     # 节目名
#     driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[4]/div/div/div[2]/div/form/div[1]/div/div[1]/input').send_keys(i.get('tag'))
#     # 通道
#     driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[4]/div/div/div[2]/div/form/div[3]/div/div/label[3]/span[2]').click()
#     # 确定创建
#     driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[4]/div/div/div[3]/div/button[2]/span').click()


# 编辑工程
def edit_test(i):
    # 编辑
    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div/button[1]/span'))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div/button[1]/span').click()
    # # 字幕
    # WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '/html/body/div/div[5]/div[1]/ul/li[2]/div'))
    # driver.find_element(By.XPATH, '/html/body/div/div[5]/div[1]/ul/li[2]/div').click()
    # # 花字
    # WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '//*[@id="panel"]/div[2]/div[1]/div[8]'))
    # driver.find_element(By.XPATH, '//*[@id="panel"]/div[2]/div[1]/div[8]').click()
    # # 默认文本
    # WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '//*[@id="panel"]/div[2]/div[2]/ul[8]/li[1]/div[1]').is_displayed())
    # action.move_to_element(driver.find_element(By.XPATH, '//*[@id="panel"]/div[2]/div[2]/ul[8]/li[1]/div[1]')).perform()
    # WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '//*[@id="panel"]/div[2]/div[2]/ul[8]/li[1]/div[1]/div[1]').is_displayed())
    # driver.find_element(By.XPATH, '//*[@id="panel"]/div[2]/div[2]/ul[8]/li[1]/div[1]/div[1]').click()
    # 文本设置
    sleep(1)
    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '/html/body/div/div[7]/div[2]/div[1]/div[2]/div/div[5]/div[1]/div/div/div[3]/span[1]'))
    driver.find_element(By.XPATH, '/html/body/div/div[7]/div[2]/div[1]/div[2]/div/div[5]/div[1]/div/div/div[3]/span[1]').click()
    action.double_click(driver.find_element(By.XPATH, '//*[@id="0,0,clip"]/div[3]/span[1]')).perform()
    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '//*[@id="panel"]/div[12]/div[1]/div/div/div[2]/div[1]/div[1]/textarea'))
    driver.find_element(By.XPATH, '//*[@id="panel"]/div[12]/div[1]/div/div/div[2]/div[1]/div[1]/textarea').clear()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="panel"]/div[12]/div[1]/div/div/div[2]/div[1]/div[1]/textarea').send_keys(i.get('tag'))
    driver.find_element(By.XPATH, '//*[@id="panel"]/div[12]/div[1]/div/div/div[2]/div[1]/div[8]/div[2]/table/tr[3]/td[2]').click()
    # 保存
    action.move_to_element(driver.find_element(By.CSS_SELECTOR, '#title-bar > div.general-dropdown.el-dropdown')).perform()
    driver.find_element(By.XPATH, '/html/body/ul/li[1]/span').click()
    sleep(3)
    # # 返回
    # driver.back()
    # sleep(2)


def check(i):
    sleep(1)
    # 导出视频
    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '/html/body/div/div[3]/div/button[2]'))
    driver.find_element(By.XPATH, '/html/body/div/div[3]/div/button[2]').click()
    # 名称
    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '/html/body/div/section/main/div/div[2]/div[1]/div[1]/div[2]/input'))
    driver.find_element(By.XPATH, '/html/body/div/section/main/div/div[2]/div[1]/div[1]/div[2]/input').clear()
    driver.find_element(By.XPATH, '/html/body/div/section/main/div/div[2]/div[1]/div[1]/div[2]/input').send_keys(i.get('tag'))
    # 电视播出
    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '/html/body/div/section/main/div/div[2]/div[1]/div[3]/div[2]/label[2]/span[2]'))
    driver.find_element(By.XPATH, '/html/body/div/section/main/div/div[2]/div[1]/div[3]/div[2]/label[2]/span[2]').click()
    # 获取封面
    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '/html/body/div/section/main/div/div[2]/div[1]/div[5]/div[3]/button[1]'))
    driver.find_element(By.XPATH, '/html/body/div/section/main/div/div[2]/div[1]/div[5]/div[3]/button[1]').click()
    sleep(1)
    # 提交审核
    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '/html/body/div/section/footer/button[1]'))
    driver.find_element(By.XPATH, '/html/body/div/section/footer/button[1]').click()
    sleep(1)
    # 日期
    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div[1]/form/div[3]/div/div/input'))
    driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div[1]/form/div[3]/div/div/input').click()

    # 月份
    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/div[1]/span[2]'))
    month0 = driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/div[1]/span[2]').text.strip()
    # 月份格式转换
    month1 = Dtd().date_c_to_date_n(i.get('month')).strip()
    # 判断月份
    if month0 != month1:
        driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/div[1]/span[2]').click()
        sleep(1)
        WebDriverWait(driver, 20).until(lambda x: x.find_element(By.LINK_TEXT, '{}'.format(i.get('month'))))
        month = driver.find_element(By.LINK_TEXT, '{}'.format(i.get('month'))).text
        print('month: ', month)
        driver.find_element(By.LINK_TEXT, '{}'.format(i.get('month'))).click()
        sleep(1)

    # 选择日期
    sleep(1)
    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '//td[@class="available"]//div//span[contains(text(),{})]'.format(i.get('day'))))
    day = driver.find_element(By.XPATH, '//td[@class="available"]//div//span[contains(text(),{})]'.format(i.get('day'))).text
    if day.strip() == i.get('day'):
        driver.find_element(By.XPATH, '//td[@class="available"]//div//span[contains(text(),{})]'.format(i.get('day'))).click()
    sleep(2)

    # 判断日期和名称
    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[4]/div'))
    date1 = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[4]/div').text
    name1 = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[1]/div').text.replace(' ', '')
    name2 = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div[2]/div[3]/table/tbody/tr[2]/td[1]/div').text.replace(' ', '')
    if name1 == '法治测试卡*':
        name1 = '法治测试卡 *'
        print('name111:', name1)
    if date1.strip() == '2029-06-10':
        sleep(3)
    print('date1: ', date1)
    print('name1: ', name1)
    print('name2: ', name2)
    print('i.getdate: ', i.get('date'))
    print('i.gettag', i.get('tag')[6:])
    # 判断绑定列表中第一条节目日期和名称
    if date1 == i.get('date') and name1 == i.get('tag')[6:]:
        print(111111)
        # 绑定
        WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[5]/div/button/span'))
        driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[5]/div/button/span').click()
        # # 提交
        # WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '/html/body/div[4]/div/div[3]/div/button[2]/span'))
        # print('绑定')
        # # driver.find_element(By.XPATH, '/html/body/div[4]/div/div[3]/div/button[2]/span').click()
        # sleep(3)
    # 判断绑定列表中第二条节目日期和名称
    elif date1 == i.get('date') and name2 == i.get('tag')[6:]:
        print(222222)
        # 绑定
        WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div[2]/div[3]/table/tbody/tr[2]/td[5]/div/button/span'))
        driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div[2]/div[3]/table/tbody/tr[2]/td[5]/div/button/span').click()
    # 判断绑定列表是否存在该节目
    elif date1 != i.get('date') or (name1 != i.get('tag')[6:] and name2 != i.get('tag')[6:]):
        driver.back()
        sleep(2)
        return 'NotInList'

    # 提交
    sleep(1)
    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '/html/body/div[4]/div/div[3]/div/button[2]/span'))
    print('绑定 ', i.get('tag'))
    driver.find_element(By.XPATH, '/html/body/div[4]/div/div[3]/div/button[2]/span').click()
    # 完成提示
    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '/html/body/div[6]'))
    text = driver.find_element(By.XPATH, '/html/body/div[6]').text
    print(text)
    if text == '操作成功':
        sleep(2)
        driver.back()
        driver.back()
    elif len(driver.find_elements(By.XPATH, '/html/body/div[6]')) == 0:
        sleep(4)
        WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '/html/body/div[6]'))
        text = driver.find_element(By.XPATH, '/html/body/div[6]').text
        print(text)
        if text == '操作成功':
            sleep(2)
            driver.back()
            driver.back()


def test1():

    try:
        for i in list0:
            print('本条节目：', i)
            i1 = list0[list0.index(i) - 1]
            print('上条节目：', i1)
            # 去重
            WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div'))
            tag1 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div').text
            print('最新节目工程：', tag1)
            # 判断页面第一条节目是否在节目单
            if not operator.contains(list_tag, tag1):
                print('new create')
                search_tag(i)
                copy_pro(i)
                edit_test(i)
                c = check(i)
                if c == 'NotInList':
                    continue
            # 页面第一条非节目单中上条节目跳过
            elif tag1 != i1.get('tag') and tag1 != list_tag[-1]:
                print('pass')
                continue
            # 页面第一条为节目单中上条节目
            elif tag1 == i1.get('tag'):
                print('now')
                sleep(2)
                # 判断上条节目是否提审
                WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div/button[2]'))
                check_btn = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div/button[2]').is_enabled()
                # 若上条节目未提审，进行编辑提审
                if check_btn:
                    edit_test(i1)
                    c2 = check(i1)
                    if c2 == 'NotInList':
                        continue
                # 上条节目已提审，按流程进行本条节目
                search_tag(i)
                copy_pro(i)
                edit_test(i)
                c = check(i)
                if c == 'NotInList':
                    continue
            sleep(1)
    except:
        test1()


test1()

WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div'))
tag11 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div').text
WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[2]/div'))
tag22 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[2]/div').text
print('最新节目工程：', tag11)
print('次新节目工程：', tag22)
if tag11 != list_tag[-1]:
    test1()
else:
    sleep(2)
    driver.refresh()
    sleep(2)

sleep(2)
driver.refresh()
sleep(2)

