import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class Base:

    # 获取 driver
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)

    # 查找元素（显式等待）
    def base_find_element(self, loc, timeout=20, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击元素
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 输入元素
    def base_input(self, loc, value):
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(value)

    # 获取输入文本
    def base_input_get_value(self, loc):
        return self.base_find_element(loc).get_attribute('value')

    # 获取文本
    def base_get_text(self, loc):
        return self.base_find_element(loc).text.strip()

    # 判断元素是否存在
    def base_ele_is_exist(self, loc):
        try:
            self.base_find_element(loc)
            return True
        except:
            return False

    # 判断按钮元素是否可用
    def base_ele_is_enable(self, loc):
        return self.base_find_element(loc).is_enabled()

    # 鼠标移动
    def base_mouse_move_to(self, loc):
        el = self.base_find_element(loc)
        self.action.move_to_element(el).perform()

    # 鼠标双击
    def base_mouse_double_click(self, loc):
        el = self.base_find_element(loc)
        self.action.double_click(el).perform()

    # 截图
    def base_screenshot(self):
        self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y_%m_%d_%H_%M_%S")))
        # self.driver.get_screenshot_as_file("../image/%s.png" %(time.strftime("%Y_%m_%d_%H_%M_%S")))
