import operator
import unittest
from time import sleep

from parameterized import parameterized

from po1 import page
from po1.page.page_check import PageCheck
from po1.page.page_check_fin import PageCheckFin
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


class TestCheckFin(unittest.TestCase):

    driver = None
    pmake = None
    mskj = None

    @classmethod
    def setUpClass(cls):
        cls.driver = GetDriver.get_driver()
        PageLogin(cls.driver).page_login(page.check_fin_username, page.test_pwd, page.check_fin_secret)
        PageHome(cls.driver).page_home_click_pmake()
        sleep(2)
        handles = cls.driver.window_handles
        cls.driver.switch_to.window(handles[1])
        PageCheckFin(cls.driver).page_click_prog2check_btn()
        cls.check_fin = PageCheckFin(cls.driver)
        cls.mskj = PageMskj(cls.driver)

    @classmethod
    def tearDownClass(cls):
        sleep(2)
        cls.driver.refresh()

    @parameterized.expand(get_data())
    def test_copy_to_check(self, tag, time, copy_name, month, day, date):

        try:
            # 获取审核列表节目1拟播日期
            date1 = self.check_fin.page_check_get_prog1_date()
            # 获取审核列表节目1名称
            tag1 = self.check_fin.page_check_get_prog1_name()
            # 获取节目tag列表
            list_tag = get_list_tag()

            # 判断当前审核节目拟播日期是否对应，且包含在节目列表中
            if date1 == date and operator.contains(list_tag, tag1):

                # 终审
                self.check_fin.pac_page_check_prog_check_fin_pass()

            else:
                print('不在节目列表')
        except:
            self.check_fin.base_screenshot()
