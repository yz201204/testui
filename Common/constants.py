# -*- coding:utf-8 -*-
"""
-------------------------------------------
@Time : 2020/5/23 22:50 
@Auth : 杨哲
@File : constants.py
@IDE : PyCharm
@Motto : Never Stop Learning
-------------------------------------------
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGS_DIR = os.path.join(BASE_DIR, "logs")
LOG_CONFIG_PATH = os.path.join(os.path.join(BASE_DIR, "Configs"), "log.conf")
SCREENSHOT_DIR = os.path.join(BASE_DIR, "Screenshots")
REPORT_DIR = os.path.join(BASE_DIR, "reports")
REPORT_CONFIG_PATH = os.path.join(os.path.join(BASE_DIR, "Configs"), "report.conf")
TestCASES_DIR = os.path.join(BASE_DIR, "TestCases")
