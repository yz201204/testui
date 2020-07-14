# -*- coding:utf-8 -*-
"""
-------------------------------------------
@Time : 2020/7/12 11:15 
@Auth : 杨哲
@File : handle_log.py
@IDE : PyCharm
@Motto : Never Stop Learning
-------------------------------------------
"""
import logging
from Common.handle_config import log_config
from Common.constants import LOGS_DIR
import os


class HandleLog:
    """

    """

    def __init__(self):
        self.case_logger = logging.getLogger(log_config.get_value("log", "logger_name"))
        self.case_logger.setLevel(log_config.get_value("log", "logger_level"))
        console_handle = logging.StreamHandler()
        file_handle = logging.FileHandler(os.path.join(LOGS_DIR, log_config.get_value("log", "log_filename")),
                                          encoding="utf-8")
        console_handle.setLevel(log_config.get_value("log", "console_level"))
        file_handle.setLevel(log_config.get_value("log", "file_level"))
        simple_formatter = logging.Formatter(log_config.get_value("log", "simple_formatter"))
        verbose_formatter = logging.Formatter(log_config.get_value("log", "verbose_formatter"))
        console_handle.setFormatter(simple_formatter)
        file_handle.setFormatter(verbose_formatter)
        self.case_logger.addHandler(console_handle)
        self.case_logger.addHandler(file_handle)

    def get_logger(self):
        return self.case_logger


do_log = HandleLog().get_logger()

if __name__ == '__main__':
    pass
    test_log = HandleLog()
    case_logger = test_log.get_logger()
    case_logger.debug("这是一个debug级别的日志")
    case_logger.info("这是一个info级别的日志")
    case_logger.warning("这是一个warning级别的日志")
    case_logger.error("这是一个error级别的日志")
    case_logger.critical("这是一个critical级别的日志")
