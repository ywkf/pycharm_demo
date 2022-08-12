from time import sleep

from selenium import webdriver

from po1 import page


class GetDriver:

    dirver = None

    @classmethod
    def get_driver(cls):
        if cls.dirver is None:
            cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()
            cls.driver.get(page.url)

        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver:
            sleep(2)
            cls.driver.refresh()
            sleep(2)
            cls.driver.quit()
            cls.driver = None