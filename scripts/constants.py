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
MYSQL_CONFIG_PATH = os.path.join(os.path.join(BASE_DIR, "configs"), "mysql.conf")
LOG_CONFIG_PATH = os.path.join(os.path.join(BASE_DIR, "configs"), "log.conf")
REPORT_CONFIG_PATH = os.path.join(os.path.join(BASE_DIR, "configs"), "report.conf")
TESTCASE_CONFIG_PATH = os.path.join(os.path.join(BASE_DIR, "configs"), "testcase.conf")
USER_ACCOUNTS_PATH = os.path.join(os.path.join(BASE_DIR, "configs"), "user_accounts.conf")
CONFIG_DIR = os.path.join(BASE_DIR, "configs")
LOGS_DIR = os.path.join(BASE_DIR, "logs")
REPORT_DIR = os.path.join(BASE_DIR, "reports")
CASES_DIR = os.path.join(BASE_DIR, "cases")
DATA_DIR = os.path.join(BASE_DIR, "datas")
