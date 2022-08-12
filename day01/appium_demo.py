import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.2'
# 设备的名字，Android随意，非空；iOS有要求
desired_caps['deviceName'] = 'Nox'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)

action = TouchAction(driver)

# WebDriverWait(driver, 20).until(lambda x: x.find_element(By.XPATH, '//*[@text="WLAN"]'))
time.sleep(2)
e1 = driver.find_element(By.XPATH, '//*[@text="声音"]')
e2 = driver.find_element(By.XPATH, '//*[@text="建议"]')
time.sleep(2)
driver.drag_and_drop(e1, e2)
time.sleep(2)
driver.swipe(100, 100, 100, 1000)
time.sleep(2)

driver.find_element(By.XPATH, '//*[@text="WLAN"]').click()
driver.find_element(By.ID, 'com.android.settings:id/switch_widget').click()
time.sleep(1)
driver.find_element(By.ID, 'com.android.settings:id/switch_widget').click()
time.sleep(3)
# driver.find_element(By.XPATH, '//*[@text="WiredSSID"]').click()
action.long_press(driver.find_element(By.XPATH, '//*[@text="WiredSSID"]'), duration=1000).perform()


print('window_size: ', driver.get_window_size())
# driver.save_screenshot('./image.png')


time.sleep(2)

print(111)
driver.quit()