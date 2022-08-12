from po1 import page
from po1.base.base import Base
from po1.tools.get_log import GetLog


class PageHome(Base):

    # 点击节目制作
    def page_home_click_pmake(self):
        GetLog.get_log().info('点击主页节目制作')
        self.base_click(page.home_pmake_btn)