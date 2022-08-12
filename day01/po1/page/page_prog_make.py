import operator

from po1 import page
from po1.base.base import Base
from po1.page import page_login
from po1.tools import get_driver
from po1.tools.get_log import GetLog


class PageProgMake(Base):

    # 点击工程文件菜单按钮
    def page_click_project_btn(self):
        GetLog.get_log().info('点击工程文件菜单按钮')
        self.base_click(page.pmake_project_btn)

    # 点击节目工程1编辑按钮
    def page_pmake_click_pro1_edit(self):
        GetLog.get_log().info('点击节目工程1编辑按钮')
        self.base_click(page.pmake_project1_edit_btn)

    # 搜索框输入节目名称模板
    def page_pmake_search_input_copy_name(self, copy_name):
        GetLog.get_log().info('搜索框输入节目名称模板: {}'.format(copy_name))
        self.base_input(page.pmake_project_search, copy_name)

    # 点击搜索按钮
    def page_pmake_click_search_btn(self):
        GetLog.get_log().info('点击搜索按钮')
        self.base_click(page.pmake_project_search_btn)

    # 点击工程文件1复制按钮
    def page_pmake_click_pro1_copy_btn(self):
        GetLog.get_log().info('点击工程文件1复制按钮')
        self.base_click(page.pmake_project1_copy_btn)

    # 工程文件复制文件名输入
    def page_pmake_input_copy_tag(self, tag):
        GetLog.get_log().info('工程文件复制文件名输入: {}'.format(tag))
        self.base_input(page.pmake_project1_copy_name, tag)

    # 点击工程文件复制文件确定按钮
    def page_pmake_click_copy_name_btn(self):
        GetLog.get_log().info('点击工程文件复制文件确定按钮')
        self.base_click(page.pmake_project1_copy_name_btn)

    # 点击重置按钮
    def page_pmake_click_reset(self):
        GetLog.get_log().info('点击重置按钮')
        self.base_click(page.pmake_project_reset)

    # 获取节目工程名称列表
    def page_pmake_get_pro_name_list(self):
        GetLog.get_log().info('获取节目工程名称列表')
        loc = page.pmake_project_name_list
        list1 = []
        for i in range(1, 11):
            list1.append(self.base_get_text((loc[0], loc[1].format(i))))
        return list1

    # 获取最新节目工程名称
    def page_pmake_get_pro1_name(self):
        name = self.base_get_text(page.pmake_project1_name)
        GetLog.get_log().info('获取最新节目工程名称: {}'.format(name))
        return name

    # 获取次新节目工程名称
    def page_pmake_get_pro2_name(self):
        name = self.base_get_text(page.pmake_project2_name)
        GetLog.get_log().info('获取次新节目工程名称: {}'.format(name))
        return name

    # 判断最新节目工程复制按钮是否可用
    def page_pmake_copy_is_enable(self):
        GetLog.get_log().info('判断最新节目工程复制按钮是否可用')
        return self.base_ele_is_enable(page.pmake_project1_copy_btn)

    # # 判断最新节目提审按钮是否可用
    # def page_pmake_check_is_enable(self):
    #     return self.base_ele_is_enable(page.pmake_project1_check_btn)

    # 判断工程名称1是否在列表中
    def page_pmake_pro1_name_in_list(self, list_tag):
        GetLog.get_log().info('判断工程名称1是否在列表中')
        name1 = self.page_pmake_get_pro1_name()
        return operator.contains(list_tag, name1)

    # 复制创建当前节目工程
    def pac_page_pmake_copy_create_prog(self, copy_name, tag):
        GetLog.get_log().info('开始 复制创建当前节目工程: {}'.format(tag))
        self.page_pmake_search_input_copy_name(copy_name)
        self.page_pmake_click_search_btn()
        self.page_pmake_click_pro1_copy_btn()
        self.page_pmake_input_copy_tag(tag)
        self.page_pmake_click_copy_name_btn()
        self.driver.refresh()
        self.page_pmake_click_reset()






