import operator
from time import sleep

from po1 import page
from po1.base.base import Base
from po1.tools.dtd import Dtd
from po1.tools.get_log import GetLog


class PageMskj(Base):

    # 点击时间线字幕
    def page_mskj_click_tl_sub(self):
        GetLog.get_log().info('点击时间线字幕')
        self.base_click(page.mskj_timeline_subtitles)

    # 点击时间线字幕
    def page_mskj_double_click_tl_sub(self):
        GetLog.get_log().info('点击时间线字幕')
        self.base_mouse_double_click(page.mskj_timeline_subtitles_mouse)

    # 点击时间线字幕
    def page_mskj_input_sub_text(self, tag):
        GetLog.get_log().info('点击时间线字幕')
        self.base_input(page.mskj_subtitles_text, tag)

    # 点击字幕向下居中
    def page_mskj_click_centerdown(self):
        GetLog.get_log().info('点击字幕向下居中')
        self.base_click(page.mskj_subtitles_centerdown)

    # 鼠标移动到保存菜单处
    def page_mskj_move_to_save_menu(self):
        GetLog.get_log().info('鼠标移动到保存菜单处')
        self.base_mouse_move_to(page.mskj_pro_save_menu)

    # 点击菜单保存按钮
    def page_mskj_click_save_btn(self):
        GetLog.get_log().info('点击菜单保存按钮')
        self.base_click(page.mskj_pro_save_menu_save_btn)

    # 点击导出视频按钮
    def page_mskj_click_export_btn(self):
        GetLog.get_log().info('点击导出视频按钮')
        self.base_click(page.mskj_pro_export_btn)

    # 详情页输入节目名称
    def page_mskj_input_export_porg_name(self, tag):
        GetLog.get_log().info('详情页输入节目名称')
        self.base_input(page.mskj_pro_export_name, tag)

    # 详情页选择电视播出选项
    def page_mskj_select_export_tv(self):
        GetLog.get_log().info('详情页选择电视播出选项')
        self.base_click(page.mskj_pro_export_tv)

    # 详情页点击获取封面按钮
    def page_mskj_click_export_get_cover_btn(self):
        GetLog.get_log().info('详情页点击获取封面按钮')
        self.base_click(page.mskj_pro_export_get_cover_btn)

    # 详情页点击提交审核按钮
    def page_mskj_click_export_check(self):
        GetLog.get_log().info('详情页点击提交审核按钮')
        self.base_click(page.mskj_pro_export_check_btn)

    # 点击预播日期选择日期按钮
    def page_mskj_binding_click_select_date(self):
        GetLog.get_log().info('点击预播日期选择日期')
        self.base_click(page.mskj_binding_date)

    # 获取日期窗口当前月份
    def page_mskj_binding_get_month(self):
        GetLog.get_log().info('获取日期窗口当前月份')
        return self.base_get_text(page.mskj_binding_date_month_btn)

    # 判断预播日期月份是否相等
    def page_mskj_binding_month_is_equal(self, month):
        GetLog.get_log().info('判断预播日期月份是否相等')
        month0 = self.page_mskj_binding_get_month()
        month1 = Dtd().date_c_to_date_n(month).strip()
        return month0 == month1

    # 日期窗口点击月份按钮
    def page_mskj_binding_click_month_btn(self):
        GetLog.get_log().info('日期窗口点击月份按钮')
        self.base_click(page.mskj_binding_date_month_btn)

    # 日期窗口选择月份
    def page_mskj_binding_click_select_month(self, month):
        GetLog.get_log().info('日期窗口选择月份')
        loc = page.mskj_binding_date_select_month
        self.base_click((loc[0], loc[1].format(month)))

    # 日期窗口选择日期
    def page_mskj_binding_click_select_day(self, day):
        GetLog.get_log().info('日期窗口选择日期')
        loc = page.mskj_binding_date_select_day
        self.base_click((loc[0], loc[1].format(day)))

    # 获取绑定窗口节目1日期
    def page_mskj_binding_get_pro1_date(self):
        GetLog.get_log().info('获取绑定窗口节目1日期')
        return self.base_get_text(page.mskj_binding_pro1_date)

    # 获取绑定窗口节目1名称
    def page_mskj_binding_get_pro1_name(self):
        GetLog.get_log().info('获取绑定窗口节目1名称')
        return self.base_get_text(page.mskj_binding_pro1_name)

    # 获取绑定窗口节目2名称
    def page_mskj_binding_get_pro2_name(self):
        GetLog.get_log().info('获取绑定窗口节目2名称')
        return self.base_get_text(page.mskj_binding_pro2_name)

    # 节目绑定窗口点击绑定按钮1
    def page_mskj_binding_click_binding1_btn(self):
        GetLog.get_log().info('节目绑定窗口点击绑定按钮1')
        self.base_click(page.mskj_binding1_btn)

    # 节目绑定窗口点击绑定按钮2
    def page_mskj_binding_click_binding2_btn(self):
        GetLog.get_log().info('节目绑定窗口点击绑定按钮2')
        self.base_click(page.mskj_binding2_btn)

    # 点击绑定并提交按钮
    def page_mskj_binding_click_binding_and_submit_btn(self):
        GetLog.get_log().info('点击绑定并提交按钮')
        self.base_click(page.mskj_binding_submit_btn)

    # 点击审核通过按钮
    def page_mskj_click_check_pass_btn(self):
        GetLog.get_log().info('点击审核通过按钮')
        self.base_click(page.mskj_pro_check_pass_btn)

    # 获取操作完成提示信息
    def page_mskj_get_result_message(self):
        GetLog.get_log().info('获取操作完成提示信息')
        return self.base_get_text(page.mskj_result_message)

    # 修改字幕保存
    def pac_page_mskj_edit_sub_save(self, tag):
        GetLog.get_log().info('修改字幕保存')
        self.page_mskj_click_tl_sub()
        self.page_mskj_double_click_tl_sub()
        self.page_mskj_input_sub_text(tag)
        self.page_mskj_click_centerdown()
        self.page_mskj_move_to_save_menu()
        self.page_mskj_click_save_btn()

    # 导出视频详情页编辑并提交审核
    def pac_page_mskj_export_to_check(self, tag):
        GetLog.get_log().info('导出视频详情页编辑并提交审核')
        self.page_mskj_click_export_btn()
        self.page_mskj_input_export_porg_name(tag)
        self.page_mskj_select_export_tv()
        self.page_mskj_click_export_get_cover_btn()
        sleep(1)
        self.page_mskj_click_export_check()

    # 节目绑定窗口选择月份
    def pac_page_mskj_select_month(self, month):
        GetLog.get_log().info('节目绑定窗口选择月份')
        self.page_mskj_binding_click_select_date()
        eq = self.page_mskj_binding_month_is_equal(month)
        if not eq:
            self.page_mskj_binding_click_month_btn()
            self.page_mskj_binding_click_select_month(month)
        else:
            return

    # 节目绑定窗口选择日期
    def pac_page_mskj_select_date(self, day):
        GetLog.get_log().info('节目绑定窗口选择日期')
        self.page_mskj_binding_click_select_day(day)

    # 节目绑定窗口绑定节目1
    def pac_page_mskj_binding_prog1(self):
        GetLog.get_log().info('节目绑定窗口绑定节目1')
        self.page_mskj_binding_click_binding1_btn()
        self.page_mskj_binding_click_binding_and_submit_btn()

    # 节目绑定窗口绑定节目2
    def pac_page_mskj_binding_prog2(self):
        GetLog.get_log().info('节目绑定窗口绑定节目2')
        self.page_mskj_binding_click_binding2_btn()
        self.page_mskj_binding_click_binding_and_submit_btn()

    # 修改字幕保存导出绑定提审，并返回结果
    def pac_page_mskj_edit_sub_to_check(self, tag, month, day, date):
        GetLog.get_log().info('开始 编辑字幕保存导出绑定提审，并返回结果')
        try:
            # 修改字幕保存
            self.pac_page_mskj_edit_sub_save(tag)
            sleep(2)
            # 导出视频详情页编辑并提交审核
            self.pac_page_mskj_export_to_check(tag)
            sleep(2)
            # 节目绑定窗口选择月份
            self.pac_page_mskj_select_month(month)
            sleep(1)
            # 节目绑定窗口选择日期
            self.pac_page_mskj_select_date(day)
            sleep(1)
            # 获取节目绑定窗口节目1日期
            date1 = self.page_mskj_binding_get_pro1_date()
            # 获取节目绑定窗口节目1名称
            name1 = self.page_mskj_binding_get_pro1_name().replace(' ', '')
            # 获取节目绑定窗口节目2名称
            name2 = self.page_mskj_binding_get_pro2_name().replace(' ', '')
            if name1 == '法治测试卡*':
                name1 = '法治测试卡 *'
            if date == date1:
                if tag[6:] == name1:
                    # 节目绑定窗口绑定节目1
                    self.pac_page_mskj_binding_prog1()
                if tag[6:] == name2:
                    # 节目绑定窗口绑定节目2
                    self.pac_page_mskj_binding_prog2()
                if tag[6:] != name1 and tag[6:] != name2:
                    return 'NotInList'
                result = self.page_mskj_get_result_message()
                if operator.contains(result, '成功'):
                    return True
                else:
                    return False
            return True
        except:
            return False