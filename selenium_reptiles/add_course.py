# -*- coding:utf-8 -*-
"""
-------------------------------------------
@Time : 2020/7/11 18:43 
@Auth : 杨哲
@File : add_course.py
@IDE : PyCharm
@Motto : Never Stop Learning
-------------------------------------------
"""
import time

from selenium import webdriver
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from TestDatas import common_datas as cd

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(cd.login_url)
lp = LoginPage(driver)
lp.login(*cd.student_user)
l = IndexPage(driver)
time.sleep(8)
top = l.stu_top_courses()
other = l.stu_other_courses()
for i in top:
    x = i.get_attribute("data-id")
    print(x)
print(len(top))
for i in other:
    y = i.get_attribute("data-id")
    print(y)
print(len(other))
time.sleep(1)
driver.quit()
