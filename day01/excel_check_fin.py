import operator
from time import sleep

from select import select
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from excel01 import excel_tag
from get_google_code import GetGoogleCode

driver = webdriver.Chrome()
driver.maximize_window()
# driver.implicitly_wait(10)


url = 'https://pre-admin.hndt.com/home'
driver.get(url)
driver.find_element(By.CSS_SELECTOR, '#usernameVal').send_keys('19955555555')
driver.find_element(By.CSS_SELECTOR, '#passVal').send_keys('123456')
driver.find_element(By.CSS_SELECTOR, '#submit').click()
# code = input('input:')
sleep(1)
code = GetGoogleCode().calGoogleCode('N4REOGIS6CXODN34HRYO7F7L3VVFDB4O')
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


def check_fin1():

    num = 0
    WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div'))
    tag = driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div').text
    print(tag)
    date1 = driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div').text
    print(date1)
    try:
        while operator.contains(date0, date1):

            # 审核
            WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/div[2]/section/div/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[10]/div/button'))
            driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/div[2]/section/div/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[10]/div/button').click()
            try:
                # 通过
                WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/div[2]/section/div/div[2]/button[1]'))
                driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/div[2]/section/div/div[2]/button[1]').click()
                sleep(2)
            except:
                print(111)
                # 通过
                WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/div[2]/section/div/div[2]/button[1]'))
                driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/div[2]/section/div/div[2]/button[1]').click()
                sleep(2)


            # 节目
            WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div'))
            tag = driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div').text
            print(tag)
            # 日期
            WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div'))
            date1 = driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div').text
            print(date1)
            num += 1
            '''
            //*[@id="app"]/div/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[9]/div
            //*[@id="app"]/div/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr[8]/td[9]/div
            //*[@id="app"]/div/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr[8]/td[9]/div/span[5]
            '''
    except:
        check_fin1()
    print(num)

check_fin1()

cookies = driver.get_cookies()
print(cookies)
sleep(5)

cookies1 = driver.get_cookies()
print(cookies1)

print(num)

sleep(3)
driver.refresh()


sleep(3)


# driver.back()

# driver.quit()