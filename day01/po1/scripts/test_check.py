import operator
import unittest
from time import sleep

from parameterized import parameterized

from po1 import page
from po1.page.page_check import PageCheck
from po1.page.page_home import PageHome
from po1.page.page_login import PageLogin
from po1.page.page_mskj import PageMskj
from po1.page.page_prog_make import PageProgMake
from po1.tools.get_prog import excel_tag
from po1.tools.get_driver import GetDriver


def get_data():
    list1 = []
    list2 = [('072501好剧连连看-1神秘人质', '01:00:00', '000000好剧连连看-1', '七月', '25', '2022-07-25'),
             ('072502好剧连连看-2神秘人质', '00:50:00', '000000好剧连连看-2', '七月', '25', '2022-07-25')]
    for i in excel_tag():
        list1.append(i)
    return list1


list2 = [('072501好剧连连看-1神秘人质', '01:00:00', '000000好剧连连看-1', '七月', '25', '2022-07-25'), ('072502好剧连连看-2神秘人质', '00:50:00', '000000好剧连连看-2', '七月', '25', '2022-07-25')]


def get_list_tag():
    list_tag = []
    for i in excel_tag():
        list_tag.append(i[0])
    return list_tag


class TestCheck(unittest.TestCase):

    driver = None
    pmake = None
    mskj = None

    @classmethod
    def setUpClass(cls):
        cls.driver = GetDriver.get_driver()
        PageLogin(cls.driver).page_login(page.check_username, page.test_pwd, page.check_secret)
        PageHome(cls.driver).page_home_click_pmake()
        sleep(2)
        handles = cls.driver.window_handles
        cls.driver.switch_to.window(handles[1])
        PageCheck(cls.driver).page_click_prog2check_btn()
        cls.check = PageCheck(cls.driver)
        cls.mskj = PageMskj(cls.driver)

    @classmethod
    def tearDownClass(cls):
        sleep(2)
        cls.driver.refresh()

    @parameterized.expand(get_data())
    def test_copy_to_check(self, tag, time, copy_name, month, day, date):

        try:
            # 获取审核列表节目1拟播日期
            date1 = self.check.page_check_get_prog1_date()
            # 获取审核列表节目1名称
            tag1 = self.check.page_check_get_prog1_name()
            # 获取节目tag列表
            list_tag = get_list_tag()

            # 判断当前审核节目拟播日期是否对应，且包含在节目列表中
            if date1 == date and operator.contains(list_tag, tag1):

                # 获取审核列表节目1审核状态，是否为待技审确认
                state = self.check.page_check_state_is_check_confirm()
                print('state: ', state)
                # 技审确认
                if state:
                    self.check.pac_page_check_prog_check_pass()

                # 节目审核
                else:
                    self.check.page_check_click_check_btn()
                    sleep(10)
                    self.driver.back()
                    self.check.page_check_click_check_btn()
                    self.mskj.page_mskj_click_check_pass_btn()

            else:
                print('不在节目列表')
        except:
            self.check.base_screenshot()
