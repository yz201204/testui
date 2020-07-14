# -*- coding:utf-8 -*-
"""
-------------------------------------------
@Time : 2020/7/11 13:59 
@Auth : 杨哲
@File : index_page_locs.py
@IDE : PyCharm
@Motto : Never Stop Learning
-------------------------------------------
"""
from selenium.webdriver.common.by import By


class IndexLocators:
    # ==================学生==================
    # 用户logo
    user_logo = (By.ID, "user")
    # 加入课程按钮
    add_in_course = (By.CSS_SELECTOR, "div[class='ktcon1l fr']")
    # 加课验证码输入框
    add_course_code = (By.CSS_SELECTOR, "input[placeholder = '请输入课程加课验证码']")
    # 加入课程框，加入按钮
    add_course_button = (By.XPATH, "//a[text()='加入']")
    # 学生置顶课程
    stu_top_courses = (By.XPATH, "//div[@id='viewer-container-toplists']/dl")
    # 学生其他课程
    stu_other_courses = (By.XPATH, "//div[@id='viewer-container-lists']/dl")
    # 查找新加课程 ，通过id
    course_id = (By.XPATH, "//dl[@data-id='{}']")
    # 课程名字链接
    course_name_link = (By.XPATH, "//dl[@data-id='{}']//a[@class='jumptoclass']")
    # 更多按钮
    more_button = (By.XPATH, "//dl[@data-id='{}']//span[text()='更多']")
    # 退课按钮
    quit_button = (By.XPATH, "//dl[@data-id='{}']//a[text()='退课']")
    # 退课确认密码验证框可见
    password_text = (By.XPATH, "//div[@class='deletekt' and @style='display: block;']//input[@type='password']")
    # 退课确认按钮可点击
    quit_confirm_button = (By.XPATH, "//a[contains(@class,'btn-positive') and text()='退课']")
