from time import sleep

from po1 import page
from po1.base.base import Base
from po1.tools.get_log import GetLog


class PageCheck(Base):

    # 点击待审节目菜单按钮
    def page_click_prog2check_btn(self):
        GetLog.get_log().info('点击待审节目菜单按钮')
        self.base_click(page.pmake_prog2check_btn)

    # 点击审核按钮
    def page_check_click_check_btn(self):
        GetLog.get_log().info('点击审核按钮')
        self.base_click(page.pmake_prog2check_check_btn)

    # 获取节目1审核状态是否为技审确认
    def page_check_state_is_check_confirm(self):
        GetLog.get_log().info('获取节目1审核状态是否为技审确认')
        return self.base_ele_is_exist(page.pmake_prog2check_pro1_state)

    # 获取审核列表节目1名称
    def page_check_get_prog1_name(self):
        name = self.base_get_text(page.pmake_prog2check_pro1_name)
        GetLog.get_log().info('获取审核列表节目1名称: {}'.format(name))
        return name

    # 获取审核列表节目1日期
    def page_check_get_prog1_date(self):
        date = self.base_get_text(page.pmake_prog2check_pro1_date)
        GetLog.get_log().info('获取审核列表节目1日期: {}'.format(date))
        return date

    # 点击技审确认按钮
    def page_check_click_check_confirm_btn(self):
        GetLog.get_log().info('点击技审确认按钮')
        self.base_click(page.pmake_prog2check_confirm_btn)

    # 点击审核通过按钮
    def page_check_click_pass_btn(self):
        GetLog.get_log().info('点击审核通过按钮')
        self.base_click(page.pmake_prog2check_check_pass_btn)

    # 节目技审确认通过
    def pac_page_check_prog_check_pass(self):
        GetLog.get_log().info('开始节目技审 确认 通过')
        self.page_check_click_check_btn()
        sleep(1)
        self.page_check_click_check_confirm_btn()
        self.page_check_click_pass_btn()