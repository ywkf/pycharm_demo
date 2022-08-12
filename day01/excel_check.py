import operator
from time import sleep

from select import select
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from excel01 import excel_tag
from get_google_code import GetGoogleCode

driver = webdriver.Chrome()
driver.maximize_window()
# driver.implicitly_wait(10)

# 启用带插件的浏览器
# option = webdriver.ChromeOptions()
# option.add_argument("--user-data-dir="+r"C:/Users/wyf/AppData/Local/Google/Chrome/User Data/Profile 7/")
# extension_path = r'./身份验证器6.3.3.crx'
# option.add_extension(extension_path)
# driver = webdriver.Chrome(chrome_options=option)   # 打开chrome浏览器

url = 'https://pre-admin.hndt.com/home'
driver.get(url)
driver.find_element(By.CSS_SELECTOR, '#usernameVal').send_keys('19966666666')
driver.find_element(By.CSS_SELECTOR, '#passVal').send_keys('123456')
driver.find_element(By.CSS_SELECTOR, '#submit').click()
# code = input('input:')
sleep(1)
code = GetGoogleCode().calGoogleCode('RCB6OQKKHOFDLJ5OMPRI3HDEJFKT2YRO')
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
# list0 = [{'tag': '070201好剧连连看-1剿匪英雄', 'time': '01:00:00'}, {'tag': '070202好剧连连看-2剿匪英雄', 'time': '00:50:00'}]
list0 = excel_tag()

# tag 列表
list_tag = []
for j in list0:
    list_tag.append(j.get('tag'))


# 待审节目
driver.find_element(By.XPATH, '//*[text()="待审节目"]').click()
WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div'))
tag = driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div').text
print(tag)
date1 = driver.find_element(By.XPATH ,'/html/body/div[1]/section/main/div/div/div/div/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div').text
print(date1)


sleep(1)

date0 = ['2022-08-07']
num = 0
# for i in list_tag:
#     print(i)


def check1():
    num = 0
    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div'))
    tag = driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div').text
    print(tag)
    date1 = driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div').text
    print(date1)

    try:
        # 节目列表 日期
        while operator.contains(date0, date1):

            if operator.contains(list_tag, tag):
                print(111)

                # if not operator.contains(list_tag, tag):
                #     continue

                # 技审确认
                if len(driver.find_elements(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[9]/div/span[5]')) != 0:
                    # 审核
                    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/div[2]/section/div/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[10]/div/button'))
                    driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/div[2]/section/div/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[10]/div/button').click()
                    # 技审确认
                    sleep(2)

                    if len(driver.find_elements(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/div[2]/section/div/div[5]/div/div/div[3]/span/button')) == 0:
                        driver.back()
                        sleep(2)
                        continue
                    WebDriverWait(driver, 20).until(expected_conditions.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/div[2]/section/div/div[5]/div/div/div[3]/span/button')))
                    driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/div[2]/section/div/div[5]/div/div/div[3]/span/button').click()
                    # 通过
                    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/div[2]/section/div/div[2]/button[1]'))
                    driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/div[2]/section/div/div[2]/button[1]').click()
                    sleep(2)

                else:
                    print(222)
                    sleep(2)
                    # 加载
                    driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/div[2]/section/div/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[10]/div/button').click()
                    sleep(10)
                    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '/html/body/div/div[5]/div[1]/div[2]/div[3]/button[1]'))
                    driver.find_element(By.XPATH, '/html/body/div/div[5]/div[1]/div[2]/div[3]/button[1]').click()
                    # driver.back()
                    sleep(1)

                    # 审核
                    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/div[2]/section/div/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[10]/div/button'))
                    driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/div[2]/section/div/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[10]/div/button').click()
                    # 通过
                    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '/html/body/div/div[5]/div[1]/div[2]/div[3]/button[1]'))
                    sleep(3)
                    driver.find_element(By.XPATH, '/html/body/div/div[5]/div[1]/div[2]/div[3]/button[1]').click()

                    sleep(1)
            else:
                print('不在节目列表')
                continue

        sleep(2)
        # 节目
        WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div'))
        tag = driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div').text
        print(tag)
        # 日期
        date1 = driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div').text
        print(date1)

        num += 1

    except:
        check1()
    print(num)


check1()

cookies = driver.get_cookies()
print(cookies)
sleep(2)

cookies1 = driver.get_cookies()
print(cookies1)

# print(num)

sleep(2)
driver.refresh()


sleep(2)

# handles1 = driver.window_handles
# print(handles1)
# driver.switch_to.window(handles[1])

# driver.back()

# driver.quit()