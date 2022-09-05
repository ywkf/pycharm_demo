from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from time import sleep
import threading

# driver = webdriver.Chrome()

# cap = {
#     "browserName": "chrome",
#     "version": "",
#     "platform": "WINDOWS"
# }

# cap1 = DesiredCapabilities.CHROME.copy()
# cap1['platform'] = "WINDOWS"
#
# driver1 = webdriver.Remote('http://127.0.0.1:4444/wd/hub', cap1)
#
# cap2 = DesiredCapabilities.FIREFOX.copy()
# cap2['platform'] = "WINDOWS"

# driver2 = webdriver.Remote('http://127.0.0.1:4444/wd/hub', cap2)


def get_driver(browser):
    if browser == 'chrome':
        cap = DesiredCapabilities.CHROME.copy()
    elif browser == 'firefox':
        cap = DesiredCapabilities.FIREFOX.copy()
    cap['platform'] = 'WINDOWS'
    return webdriver.Remote('http://127.0.0.1:4444/wd/hub', cap)


def get_baidu(driver):

    driver.get("https://www.baidu.com")
    driver.find_element_by_id('kw').send_keys('Python')
    driver.find_element_by_id('su').click()
    sleep(3)
    driver.quit()


# tr1 = threading.Thread(target=get_baidu, args=(driver1,)).start()
# tr2 = threading.Thread(target=get_baidu, args=(driver2,)).start()

browserName = ['chrome', 'firefox']
for browser in browserName:
    driver = get_driver(browser)
    threading.Thread(target=get_baidu, args=(driver,)).start()
