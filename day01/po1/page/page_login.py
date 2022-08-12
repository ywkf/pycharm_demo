from time import sleep

from po1 import page
from po1.base.base import Base
from po1.tools.get_google_code import GetGoogleCode
from po1.tools.get_log import GetLog


class PageLogin(Base):

    # 输入用户名
    def page_input_username(self, username):
        GetLog.get_log().info('输入用户名: {}'.format(username))
        self.base_input(page.login_username, username)

    # 输入密码
    def page_input_pwd(self, pwd):
        GetLog.get_log().info('输入密码: {}'.format(pwd))
        self.base_input(page.login_pwd, pwd)

    # 点击登录按钮
    def page_click_login_btn(self):
        GetLog.get_log().info('点击登录按钮')
        self.base_click(page.login_btn)

    # 获取登录提示信息
    def page_get_login_message(self):
        msg = self.base_get_text(page.login_message)
        GetLog.get_log().info('获取登录提示信息: {}'.format(msg))
        return msg

    # 获取谷歌验证码
    @staticmethod
    def page_get_google_code(secret):
        code = GetGoogleCode().calGoogleCode(secret)
        GetLog.get_log().info('获取谷歌验证码: {}'.format(code))
        return code

    # 输入验证码
    def page_input_vcode(self, vcode):
        GetLog.get_log().info('输入验证码: {}'.format(vcode))
        # vcode = self.page_get_google_code(secret)
        self.base_input(page.login_verify_code, vcode)

    # 获取验证码输入
    def page_get_vcode_value(self):
        value = self.base_input_get_value(page.login_verify_code)
        GetLog.get_log().info('获取验证码输入: {}'.format(value))
        return value

    # 点击验证码提交按钮
    def page_click_vcode_btn(self):
        GetLog.get_log().info('点击验证码提交按钮')
        self.base_click(page.login_code_btn)

    # 点击验证码取消按钮
    def page_click_vcode_cancel_btn(self):
        GetLog.get_log().info('点击验证码取消按钮')
        self.base_click(page.login_code_cancel_btn)

    # 登录（无验证码）获取登录信息
    def page_login_ignore_vcode(self, username, pwd):
        GetLog.get_log().info('开始登录（无验证码）')
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()
        sleep(0.5)
        return self.page_get_login_message()
        # return message

    # 登录
    def page_login(self, username, pwd, vcode):
        GetLog.get_log().info('开始登录')
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()
        # vcode = input('input:')
        sleep(1)
        self.page_input_vcode(vcode)
        value = self.page_get_vcode_value()
        sleep(0.5)
        self.page_click_vcode_btn()
        sleep(0.5)
        msg = self.page_get_login_message()
        if len(value) == 0:
            self.page_click_vcode_cancel_btn()
        return msg