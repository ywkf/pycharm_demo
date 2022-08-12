import logging
import operator
import unittest
from time import sleep

from unittestreport import rerun
from parameterized import parameterized

from po1 import page
from po1.page.page_home import PageHome
from po1.page.page_login import PageLogin
from po1.page.page_mskj import PageMskj
from po1.page.page_prog_make import PageProgMake
from po1.tools.get_log import GetLog
from po1.tools.get_prog import excel_tag
from po1.tools.get_driver import GetDriver


def get_data():
    list1 = []
    list2 = [('072501好剧连连看-1神秘人质', '01:00:00', '000000好剧连连看-1', '七月', '25', '2022-07-25'),
             ('072502好剧连连看-2神秘人质', '00:50:00', '000000好剧连连看-2', '七月', '25', '2022-07-25')]
    # for i in excel_tag():
    #     list1.append(i)
    return list2


list2 = [('072501好剧连连看-1神秘人质', '01:00:00', '000000好剧连连看-1', '七月', '25', '2022-07-25'),
         ('072502好剧连连看-2神秘人质', '00:50:00', '000000好剧连连看-2', '七月', '25', '2022-07-25')]


def get_list_tag():
    list_tag = []
    for i in excel_tag():
        list_tag.append(i[0])
    return list_tag


class TestCopyProgToCheck(unittest.TestCase):

    driver = None
    pmake = None
    mskj = None

    @classmethod
    def setUpClass(cls):
        # 获取浏览器驱动
        cls.driver = GetDriver.get_driver()
        # 登录
        PageLogin(cls.driver).page_login(page.pmake_username, page.test_pwd, page.pmake_secret)
        # 主页
        PageHome(cls.driver).page_home_click_pmake()
        sleep(2)
        # 切换窗口
        handles = cls.driver.window_handles
        cls.driver.switch_to.window(handles[1])
        # 节目制作工程文件
        PageProgMake(cls.driver).page_click_project_btn()
        # 节目制作页面对象
        cls.pmake = PageProgMake(cls.driver)
        # 美摄页面对象
        cls.mskj = PageMskj(cls.driver)

        # 美摄页面加载
        cls.pmake.page_pmake_click_pro1_edit()
        sleep(10)
        cls.driver.back()

    @classmethod
    def tearDownClass(cls):
        sleep(2)
        cls.driver.refresh()

    def get_newest_prog(self):
        sleep(3)
        # pro_new = ''
        list_tag = get_list_tag()
        list0 = self.pmake.page_pmake_get_pro_name_list()
        for i in list0:
            if operator.contains(list_tag, i):
                pro_new = i
                return pro_new

    @rerun(count=4, interval=2)
    @parameterized.expand(get_data())
    def test_copy_to_check(self, tag, time, copy_name, month, day, date):

        try:
            sleep(3)
            # 获取最新节目名称
            tag1 = self.pmake.page_pmake_get_pro1_name()
            # 获取次新节目名称
            tag2 = self.pmake.page_pmake_get_pro2_name()
            # 获取最新节目是否可以复制
            copy1 = self.pmake.page_pmake_copy_is_enable()
            # 获取节目工程名称列表
            list0 = self.pmake.page_pmake_get_pro_name_list()
            print(list0)
            # 获取节目工程列表中最新的已创建节目工程
            sleep(2)
            pro_new = self.get_newest_prog()
            print(pro_new)
            # 获取节目名称列表
            list_tag = get_list_tag()
        #
        #     if not pro_new:
        #         # 复制创建节目工程
        #         self.pmake.pac_page_pmake_copy_create_prog(copy_name, tag)
        #         # 编辑
        #         self.pmake.page_pmake_click_pro1_edit()
        #         sleep(3)
        #         # 美摄页面编辑字幕、保存、绑定提审
        #         result = self.mskj.pac_page_mskj_edit_sub_to_check(tag, month, day, date)
        #         if result:
        #             print('操作成功')
        #             GetLog.get_log().info('绑定成功')
        #         else:
        #             GetLog.get_log().info('绑定失败，返回')
        #             self.driver.back()
        #             self.test_copy_to_check()
        #     elif pro_new == tag:
        #     # # 判断当前最新和次新节目是否在列表中
        #     # if operator.contains(list_tag, tag1) or operator.contains(list_tag, tag2):
        #         # 判断当前最新节目是否为本条用例节目
        #         if tag == tag1:
        #             # 判断本条用例对应节目工程是否提审
        #             if copy1:
        #                 # 编辑
        #                 self.pmake.page_pmake_click_pro1_edit()
        #                 sleep(3)
        #                 # 美摄页面编辑字幕、保存、绑定提审
        #                 result = self.mskj.pac_page_mskj_edit_sub_to_check(tag, month, day, date)
        #                 if result and result != 'NotInList':
        #                     print('操作成功')
        #                     GetLog.get_log().info('绑定成功')
        #                     self.driver.back()
        #                     # 跳过本条用例
        #                     self.skipTest('本条用例已提审')
        #                 elif result == 'NotInList':
        #                     print('不在列表中')
        #                     GetLog.get_log().info('不在列表中')
        #                     self.driver.back()
        #                     # 跳过本条用例
        #                     self.skipTest('本条用例已提审或不在列表中')
        #                 else:
        #                     GetLog.get_log().info('绑定失败，返回')
        #                     self.driver.back()
        #                     self.test_copy_to_check()
        #             else:
        #                 # 跳过本条用例
        #                 self.skipTest('本条用例已提审')
        #
        #             # 复制创建节目工程
        #             self.pmake.pac_page_pmake_copy_create_prog(copy_name, tag)
        #             # 编辑
        #             self.pmake.page_pmake_click_pro1_edit()
        #             sleep(3)
        #             # 美摄页面编辑字幕、保存、绑定提审
        #             result = self.mskj.pac_page_mskj_edit_sub_to_check(tag, month, day, date)
        #             if result and result != 'NotInList':
        #                 print('操作成功')
        #                 GetLog.get_log().info('绑定成功')
        #             elif result == 'NotInList':
        #                 print('不在列表中')
        #                 GetLog.get_log().info('不在列表中')
        #                 self.driver.back()
        #                 # 跳过本条用例
        #                 self.skipTest('本条用例已提审或不在列表中')
        #             else:
        #                 GetLog.get_log().info('绑定失败，返回')
        #                 self.driver.back()
        #                 self.test_copy_to_check()
        #         else:
        #             # 跳过本条用例
        #             self.skipTest('本条用例已创建')
        #
        #     elif pro_new != tag:
        #         # 跳过本条用例
        #         self.skipTest('本条用例已创建')
        #
        #     # 重新运行
        #     self.test_copy_to_check()
        #
        #     # 复制创建节目工程
        #     self.pmake.pac_page_pmake_copy_create_prog(copy_name, tag)
        #     # 编辑
        #     self.pmake.page_pmake_click_pro1_edit()
        #     sleep(3)
        #     # 美摄页面编辑字幕、保存、绑定提审
        #     self.mskj.pac_page_mskj_edit_sub_to_check(tag, day, date)
        #
        #     print(11)
        except:
            print(22)
            # self.driver.back()
            # self.driver.back()
            # self.pmake.page_click_project_btn()
            # self.test_copy_to_check()

