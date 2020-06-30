# -*- coding:utf-8 -*-
"""
-------------------------------------------
@Time : 2020/5/7 12:52 
@Auth : 杨哲
@File : python_discover.py
@IDE : PyCharm
@Motto : Never Stop Learning
-------------------------------------------
"""
import unittest
import time
from libs.HTMLTestRunnerNew import HTMLTestRunner
from scripts.handle_config import report_config
from scripts.constants import REPORT_DIR, CASES_DIR, USER_ACCOUNTS_PATH
from scripts.handle_user import HandleUser
import os
if not os.path.exists(USER_ACCOUNTS_PATH):
    HandleUser().generate_users_config()


report_name = "report_" + str(time.strftime("%Y%m%d_%H%M%S", time.localtime())) + ".html"
report_full_name = os.path.join(REPORT_DIR, report_name)

with open(report_full_name, mode="wb") as save_to_file:
    HTMLTestRunner(stream=save_to_file,
                   title=report_config.get_value("report", "title"),
                   verbosity=report_config.get_int("report", "verbosity"),
                   description=report_config.get_value("report", "description"),
                   tester=report_config.get_value("report", "tester")). \
        run(unittest.defaultTestLoader.discover(CASES_DIR))
