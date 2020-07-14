# -*- coding:utf-8 -*-
"""
-------------------------------------------
@Time : 2020/7/11 22:56 
@Auth : 杨哲
@File : class_page_locs.py
@IDE : PyCharm
@Motto : Never Stop Learning
-------------------------------------------
"""
from selenium.webdriver.common.by import By


class ClassLocators:
    # 课堂互动
    active = (By.XPATH, "//div[@id='third-nav']//a[@class='active']")
