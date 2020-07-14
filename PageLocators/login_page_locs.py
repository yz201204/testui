# -*- coding:utf-8 -*-
"""
-------------------------------------------
@Time : 2020/7/11 13:56 
@Auth : 杨哲
@File : login_page_locs.py
@IDE : PyCharm
@Motto : Never Stop Learning
-------------------------------------------
"""
from selenium.webdriver.common.by import By


class LoginLocators:
    # 用户名输入框
    user_input = (By.NAME, "account")
    # 密码输入框
    password_input = (By.NAME, "pass")
    # 登陆按钮
    login_button = (By.XPATH, "//input[@name='pass']/parent::div/following-sibling::a[@class='btn-btn']")
    # 登陆表单区域 - 错误提示
    error_msg = (By.CSS_SELECTOR, "p[class='error-tips']")
