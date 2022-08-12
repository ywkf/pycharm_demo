from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from excel01 import excel_tag

driver = webdriver.Chrome()
# driver.maximize_window()
driver.implicitly_wait(10)

# url = 'https://pre-admin.hndt.com/cprogramme/programAudit/programPlan'

url = 'https://pre-admin.hndt.com/home'
driver.get(url)
# driver.add_cookie({'name': 'SESSION', 'value': 'NDEwMDk2NTQtYjVkMi00YzRkLWExZWMtOWUyNjUwOTkzNzVk'})
# a = input('input:')

# excel_tag()
cookies = driver.get_cookies()
print(cookies)
sleep(5)

cookies1 = driver.get_cookies()
print(cookies1)
# driver.add_cookie({'name': 'SESSION', 'value': 'NDEwMDk2NTQtYjVkMi00YzRkLWExZWMtOWUyNjUwOTkzNzVk'})
sleep(3)
driver.refresh()
# driver.get('https://www.baidu.com')

# driver.find_element(By.ID, "kw").send_keys("baidu")
# driver.find_element(By.ID, "su").click()
# driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys('baidu')
# driver.find_element(By.XPATH, '//*[@id="su"]').click()
# driver.maximize_window()
# driver.find_element(By.CSS_SELECTOR, '#kw').send_keys('baidu')
# driver.find_element(By.CSS_SELECTOR, '#su').click()

sleep(3)

# driver.back()

# driver.quit()