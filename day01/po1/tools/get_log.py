import logging.handlers
import time
from time import sleep

from selenium import webdriver

from po1 import page
import colorlog

log_colors_config = {
    'DEBUG': 'white',  # cyan white
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'bold_red',
}


class GetLog:
    logger = None

    @classmethod
    def get_log(cls):
        if cls.logger is None:
            # 获取 日志器对象
            cls.logger = logging.getLogger()

            # 设置日志器级别
            cls.logger.setLevel(logging.INFO)

            # 获取控制台处理器
            sf = logging.StreamHandler()
            # sf.setLevel(logging.INFO)

            # 获取文件处理器  1). when：时间单位
            # 				2). interval:时间间隔
            # 				3). backupcount:保留的备份数量
            th = logging.handlers.TimedRotatingFileHandler(filename="../log/log",
                                                           when='M',
                                                           interval=1,
                                                           backupCount=30,
                                                           encoding='utf-8')
            # th.setLevel(logging.ERROR)

            # 获取格式器
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            fm = logging.Formatter(fmt)
            fm1 = colorlog.ColoredFormatter(
                fmt='%(log_color)s[%(asctime)s.%(msecs)03d] %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s',
                datefmt='%Y-%m-%d  %H:%M:%S',
                log_colors=log_colors_config
            )

            # 将格式器添加到处理器中
            sf.setFormatter(fm1)
            th.setFormatter(fm)

            # 将处理器添加到日志器中
            cls.logger.addHandler(sf)
            cls.logger.addHandler(th)

        return cls.logger
