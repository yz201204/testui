# -*- coding:utf-8 -*-
"""
-------------------------------------------
@Time : 2020/7/13 0:53 
@Auth : 杨哲
@File : main.py
@IDE : PyCharm
@Motto : Never Stop Learning
-------------------------------------------
"""
import pytest
import datetime

report_name = "report_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".html"
html_report_para = "--html=Reports\\html\\{}".format(report_name)

if __name__ == '__main__':
    pytest.main(["--reruns", "3", "--reruns-delay", "5",
                 html_report_para, "--junitxml=Reports\\xml\\report.xml",
                 "--alluredir=Reports\\allure"])
