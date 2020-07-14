# -*- coding:utf-8 -*-
"""
-------------------------------------------
@Time : 2020/7/11 22:45 
@Auth : 杨哲
@File : class_page.py
@IDE : PyCharm
@Motto : Never Stop Learning
-------------------------------------------
"""
# from selenium.webdriver.remote.webdriver import WebDriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from PageLocators.class_page_locs import ClassLocators as cl
from Common.basepage import BasePage


class ClassPage(BasePage):

    def get_current_url(self):
        return self.get_window_url("课程页面_获取url")

    def if_active_is_exist(self):
        try:
            self.get_element(cl.active, "课程页面_判断课程互动存在")
        except:
            return False
        else:
            return True
