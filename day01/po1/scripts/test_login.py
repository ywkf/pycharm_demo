import operator
import unittest
from time import sleep

from parameterized import parameterized

from po1.page.page_login import PageLogin
from po1.tools.get_driver import GetDriver


def get_date():
    list1 = [('19933333333', '', '111111', '请输入密码'),
             ('', '123456', '111111', '请输入手机号'),
             ('1aaaaaaaaaa', '123456', '111111', '要操作的用户不存在'),
             ('1a~!@#$', '123456', '111111', '要操作的用户不存在'),
             ('1a一', '123456', '111111', '要操作的用户不存在'),
             ('a一', '123456', '111111', '要操作的用户不存在'),
             ('1!$@%', '123456', '111111', '要操作的用户不存在'),
             ('a!%$#%@', '123456', '111111', '要操作的用户不存在'),
             ('19933333333', '123123', '111111', '密码错误'),
             ('19933333333', '123456', '11', '请输入谷歌动态口令'),
             ('19933333333', '123456', '111111', '请输入正确的谷歌动态口令')]
    return list1


class TestLogin(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = GetDriver.get_driver()
        cls.login = PageLogin(cls.driver)

    @classmethod
    def tearDownClass(cls):
        sleep(1)
        # cls.driver.refresh()
        cls.driver.quit()

    @parameterized.expand(get_date())
    def test_login(self, username, pwd, vcode, expect):
        if not operator.contains(expect, '谷歌'):
            result = self.login.page_login_ignore_vcode(username, pwd)
        else:
            result = self.login.page_login(username, pwd, vcode)

        # try:
        #     assert result == expect
        # except AssertionError:
        #     self.login.base_screenshot()

        try:
            self.assertIn(expect, result)
        except AssertionError:
            self.login.base_screenshot()