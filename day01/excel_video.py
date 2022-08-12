import operator
from time import sleep

from select import select
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

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
WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '//*[text()="节目制作"]').is_displayed())
driver.find_element(By.XPATH, '//*[text()="节目制作"]').click()

sleep(2)
handles = driver.window_handles
print(handles)
driver.switch_to.window(handles[1])
list0 = [{'tag': '060201好剧连连看-1剿匪英雄', 'time': '01:00:00', 'month': '2 月', 'day': '2', 'date': '2022-06-02'},
         {'tag': '060202好剧连连看-2剿匪英雄', 'time': '00:50:00', 'month': '2 月', 'day': '2', 'date': '2022-06-02'}]

# list0 = excel_tag()

# tag 列表
list_tag = []
for j in list0:
    list_tag.append(j.get('tag'))


# 工程文件
driver.find_element(By.XPATH, '//*[text()="工程文件"]').click()
# 编辑
WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div/button[2]/span'))
driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div/button[2]/span').click()
# 返回
sleep(10)
driver.back()


# 创建工程
def create_test(i):
    # 新建
    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/button').is_displayed())
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/button').click()
    # 节目名
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[4]/div/div/div[2]/div/form/div[1]/div/div[1]/input').send_keys(i.get('tag'))
    # 通道
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[4]/div/div/div[2]/div/form/div[3]/div/div/label[3]/span[2]').click()
    # 确定创建
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[4]/div/div/div[3]/div/button[2]/span').click()


# 编辑工程
def edit_test(i):
    # 编辑
    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div/button[2]/span'))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div/button[2]/span').click()
    # 字幕
    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '/html/body/div/div[5]/div[1]/ul/li[2]/div').is_displayed())
    driver.find_element(By.XPATH, '/html/body/div/div[5]/div[1]/ul/li[2]/div').click()
    # 花字
    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '//*[@id="panel"]/div[2]/div[1]/div[8]').is_displayed())
    driver.find_element(By.XPATH, '//*[@id="panel"]/div[2]/div[1]/div[8]').click()
    # 默认文本
    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '//*[@id="panel"]/div[2]/div[2]/ul[8]/li[1]/div[1]').is_displayed())
    action.move_to_element(driver.find_element(By.XPATH, '//*[@id="panel"]/div[2]/div[2]/ul[8]/li[1]/div[1]')).perform()
    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '//*[@id="panel"]/div[2]/div[2]/ul[8]/li[1]/div[1]/div[1]').is_displayed())
    driver.find_element(By.XPATH, '//*[@id="panel"]/div[2]/div[2]/ul[8]/li[1]/div[1]/div[1]').click()
    # 文本设置
    action.double_click(driver.find_element(By.XPATH, '//*[@id="0,0,clip"]/div[3]/span[1]')).perform()
    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '//*[@id="panel"]/div[12]/div[1]/div/div/div[2]/div[1]/div[1]/textarea').is_displayed())
    driver.find_element(By.XPATH, '//*[@id="panel"]/div[12]/div[1]/div/div/div[2]/div[1]/div[1]/textarea').clear()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="panel"]/div[12]/div[1]/div/div/div[2]/div[1]/div[1]/textarea').send_keys(i.get('tag'))
    driver.find_element(By.XPATH, '//*[@id="panel"]/div[12]/div[1]/div/div/div[2]/div[1]/div[8]/div[2]/table/tr[3]/td[2]').click()
    # 保存
    action.move_to_element(driver.find_element(By.CSS_SELECTOR, '#title-bar > div.general-dropdown.el-dropdown')).perform()
    driver.find_element(By.XPATH, '/html/body/ul/li[1]/span').click()
    sleep(2)
    # 返回
    driver.back()
    sleep(2)


# def test1():
#
#     try:
#         for i in list0:
#             print(i)
#             i1 = list0[list0.index(i) - 1]
#             print(i1)
#             # 去重
#             WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div'))
#             tag1 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div').text
#             # tag2 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[2]/div').text
#             print(tag1)
#             if not operator.contains(list_tag, tag1):
#                 print(111)
#                 create_test(i)
#                 edit_test(i)
#                 video_test(i)
#             elif tag1 != i1.get('tag'):
#                 print(222)
#                 continue
#             elif tag1 == i1.get('tag'):
#                 print(333)
#                 create_test(i)
#                 edit_test(i)
#                 video_test(i)
#             sleep(1)
#     except:
#         test1()
#
#
# test1()

def video_test():

    # driver.find_element(By.XPATH, '//*[@id="0,0,clip"]/div[3]/span[1]').click()
    # action.drag_and_drop(driver.find_element(By.XPATH, '//*[@id="0,0,clip"]/button[2]'),)

    # 编辑
    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div/button[2]/span'))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div/button[2]/span').click()
    # 我的资源
    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '//*[@id="tab-1"]'))
    driver.find_element(By.XPATH, '//*[@id="tab-1"]').click()
    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '//*[@id="panel"]//div[contains(text(),"6月12号节目单24小时素材")]//preceding-sibling::div'))
    driver.find_element(By.XPATH, '//*[@id="panel"]//div[contains(text(),"6月12号节目单24小时素材")]//preceding-sibling::div').click()
    # WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '//*[@id="panel"]/div[1]/div[2]/div[2]/div[2]/div/div[15]/div[1]'))
    # driver.find_element(By.XPATH, '//*[@id="panel"]/div[1]/div[2]/div[2]/div[2]/div/div[15]/div[1]').click()
    # action.drag_and_drop(driver.find_element(By.XPATH, '//*[@id="panel"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[1]'),
    #                      driver.find_element(By.XPATH, '//*[@id="0videoTrack"]/div'))
    # strtime = driver.find_element(By.XPATH, '//*[@id="panel"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[1]/div[6]').text
    # """//*[@id="panel"]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[1]"""
    # ele = driver.find_element(By.XPATH, '//*[@id="panel"]/div[1]/div[2]/div[2]/div[3]/div')
    # eles = ele.find_elements(By.CSS_SELECTOR, '#panel > div.media-resource.panel-list > div.media-body > div:nth-child(2) > div.tab-media-body > div')
    # print(strtime)
    # print(eles)
    # if strtime == i.get('time'):
    #     driver.find_element(By.XPATH, '')
    sleep(2)
    # 节目上轨
    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[1]/div/div[1]/div[2]/div[2]/div[3]/div/div[5]/div[1]'))
    action.move_to_element(driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[1]/div/div[1]/div[2]/div[2]/div[3]/div/div[5]/div[1]')).perform()
    driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[1]/div/div[1]/div[2]/div[2]/div[3]/div/div[5]/div[1]/div[2]').click()

    print(111)
    sleep(2)
    # 全局显示
    # driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", driver.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[1]/svg/use'),
    #                       "border: 2px solid red;")
    # action.move_to_element(driver.find_element(By.XPATH, '//*[name()="svg" and @aria-hidden="true"]//*[name()="use"]')).click().perform()
    # driver.find_element(By.XPATH, '//*[name()="svg" and @aria-hidden="true"]').click()
    # ele = driver.find_element(By.XPATH, '//*[name()="svg" and @aria-hidden="true"]/*[name()="use"]')
    ele = driver.find_element(By.XPATH , '/html/body/div[1]/div[7]/div[1]/div[1]/button[2]')
    ele_x = ele.location.get('x')
    ele_y = ele.location.get('y')
    print(ele.location, ',x = ', ele_x, ' , y = ', ele_y)  # "+": {'x': 1863, 'y': 541}
    action.click(ele).perform()
    sleep(2)
    action.move_by_offset(30, 0).click().perform()
    # js = 'arguments[0].removeAttribute("style");'
    # # js = 'document.getElementByTagName("use").click()'
    # driver.execute_script(js, ele)
    # driver.find_element(By.XPATH, '//*[name()="svg"]//*[name()="use"]').click()
    print(222)

    # 字幕
    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '/html/body/div/div[5]/div[1]/ul/li[2]/div'))
    driver.find_element(By.XPATH, '/html/body/div/div[5]/div[1]/ul/li[2]/div').click()
    # 花字
    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '//*[@id="panel"]/div[2]/div[1]/div[8]'))
    driver.find_element(By.XPATH, '//*[@id="panel"]/div[2]/div[1]/div[8]').click()
    # 默认文本
    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '//*[@id="panel"]/div[2]/div[2]/ul[8]/li[1]/div[1]').is_displayed())
    action.move_to_element(driver.find_element(By.XPATH, '//*[@id="panel"]/div[2]/div[2]/ul[8]/li[1]/div[1]')).perform()
    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '//*[@id="panel"]/div[2]/div[2]/ul[8]/li[1]/div[1]/div[1]').is_displayed())
    driver.find_element(By.XPATH, '//*[@id="panel"]/div[2]/div[2]/ul[8]/li[1]/div[1]/div[1]').click()
    # 文本设置
    action.double_click(driver.find_element(By.XPATH, '//*[@id="0,0,clip"]/div[3]/span[1]')).perform()
    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '//*[@id="panel"]/div[12]/div[1]/div/div/div[2]/div[1]/div[1]/textarea'))
    driver.find_element(By.XPATH, '//*[@id="panel"]/div[12]/div[1]/div/div/div[2]/div[1]/div[1]/textarea').clear()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="panel"]/div[12]/div[1]/div/div/div[2]/div[1]/div[1]/textarea').send_keys('123')
    driver.find_element(By.XPATH, '//*[@id="panel"]/div[12]/div[1]/div/div/div[2]/div[1]/div[8]/div[2]/table/tr[3]/td[2]').click()


    # # 字幕
    # driver.find_element(By.XPATH, '/html/body/div/div[5]/div[1]/ul/li[2]/div').click()
    # # 花字
    # driver.find_element(By.XPATH, '//*[@id="panel"]/div[2]/div[1]/div[8]').click()
    # # 默认文本
    # action.move_to_element(driver.find_element(By.XPATH, '//*[@id="panel"]/div[2]/div[2]/ul[8]/li[1]/div[1]')).perform()
    # driver.find_element(By.XPATH, '//*[@id="panel"]/div[2]/div[2]/ul[8]/li[1]/div[1]/div[1]').click()
    # # 文本设置
    # action.double_click(driver.find_element(By.XPATH, '//*[@id="0,0,clip"]/div[3]/span[1]')).perform()
    # driver.find_element(By.XPATH, '//*[@id="panel"]/div[12]/div[1]/div/div/div[2]/div[1]/div[1]/textarea').clear()
    # sleep(1)
    # driver.find_element(By.XPATH, '//*[@id="panel"]/div[12]/div[1]/div/div/div[2]/div[1]/div[1]/textarea').send_keys('123')
    # driver.find_element(By.XPATH, '//*[@id="panel"]/div[12]/div[1]/div/div/div[2]/div[1]/div[8]/div[2]/table/tr[3]/td[2]').click()
    #
    # driver.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[2]/div[1]/div[2]/div/div[5]/div[2]/div/div/div[3]').click()
    # driver.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[2]/div[1]/div[2]/div/div[5]/div[2]/div/div/div[3]').send_keys(Keys.DOWN)
    #
    # driver.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[2]/div[1]/div[2]/div/div[5]/div[1]/div/div/div[6]').click()
    # action.drag_and_drop(driver.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[2]/div[1]/div[2]/div/div[5]/div[1]/div/div/button[2]'),
    #                      driver.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[2]/div[1]/div[2]/div/div[4]/div[2]')).perform()

try:
    video_test()
except:
    driver.back()
    video_test()


cookies = driver.get_cookies()
print(cookies)
sleep(2)

cookies1 = driver.get_cookies()
print(cookies1)
# driver.add_cookie({'name': 'SESSION', 'value': 'NDEwMDk2NTQtYjVkMi00YzRkLWExZWMtOWUyNjUwOTkzNzVk'})
sleep(2)
driver.refresh()


sleep(2)

# handles1 = driver.window_handles
# print(handles1)
# driver.switch_to.window(handles[1])

# driver.back()

# driver.quit()