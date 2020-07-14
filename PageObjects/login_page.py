# -*- coding:utf-8 -*-
"""
-------------------------------------------
@Time : 2020/7/11 1:16 
@Auth : 杨哲
@File : login_page.py
@IDE : PyCharm
@Motto : Never Stop Learning
-------------------------------------------
"""
# from selenium.webdriver.remote.webdriver import WebDriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from PageLocators.login_page_locs import LoginLocators as loc
from Common.basepage import BasePage


class LoginPage(BasePage):

    def login(self, username, password):
        # self.wait.until(EC.visibility_of_element_located(loc.user_input))
        # # 登陆页面 - 输入用户名
        # self.driver.find_element(*loc.user_input).send_keys(username)
        # # 登陆页面 - 输入密码
        # self.driver.find_element(*loc.password_input).send_keys(password)
        # # 登陆页面 - 点击登陆按钮
        # self.driver.find_element(*loc.login_button).click()
        self.input_text(loc.user_input, username, "登陆页面_输入用户名")
        self.input_text(loc.password_input, password, "登陆页面_输入密码")
        self.click_element(loc.login_button, "登陆页面_点击登陆按钮")

    def get_err_msg(self):
        # 获取错误提示信息
        # self.wait.until(EC.visibility_of_element_located(loc.error_msg))
        # return self.driver.find_element(*loc.error_msg).text
        return self.get_element_text(loc.error_msg, "登陆页面_获取错误提示信息")

    def get_err_msgs(self):
        # self.wait.until(EC.visibility_of_element_located(loc.error_msg))
        # return self.driver.find_elements(*loc.error_msg)
        return self.get_elements_text(loc.error_msg, "登陆页面_获取多个错误提示信息")
