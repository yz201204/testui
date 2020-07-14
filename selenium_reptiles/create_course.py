# -*- coding:utf-8 -*-
"""
-------------------------------------------
@Time : 2020/7/11 18:44 
@Auth : 杨哲
@File : create_course.py
@IDE : PyCharm
@Motto : Never Stop Learning
-------------------------------------------
"""
import time

from selenium import webdriver
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from TestDatas import common_datas as cd
from API import api_course_operate

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(cd.login_url)
lp = LoginPage(driver)
lp.login(*cd.teacher_user)
l = IndexPage(driver)
time.sleep(8)
top = l.stu_top_courses()
other = l.stu_other_courses()
count1 = 0
# login = api_course_operate.CourseOperate(*cd.teacher_user)
for i in top:
    x = i.get_attribute("data-id")
    print(x)
    # count1 += 1
    # if count1 <= 10:
    #     print(count1)
    #     login.delete_couse(x, cd.teacher_user[-1])
print(len(top))
count2 = 0
for i in other:
    y = i.get_attribute("data-id")
    print(y)
    # count2 += 1
    # if count2 <= 180:
    #     print(count2)
    #     login.delete_couse(y, cd.teacher_user[-1])
print(len(other))
time.sleep(1)
driver.quit()
