# -*- coding:utf-8 -*-
"""
-------------------------------------------
@Time : 2020/7/13 22:49 
@Auth : 杨哲
@File : conftest.py.py
@IDE : PyCharm
@Motto : Never Stop Learning
-------------------------------------------
"""
import pytest

# 定义前置后置
from selenium import webdriver
from TestDatas import common_datas as cd
from PageObjects.login_page import LoginPage

from API.api_course_operate import CourseOperate
from TestDatas import course_datas as bj
from PageObjects.index_page import IndexPage


@pytest.fixture(scope="function")
def init_driver():
    # 前置
    # 静默执行
    # options = webdriver.ChromeOptions()
    # options.add_argument("headless")
    # driver = webdriver.Chrome(options=options)
    # 非静默执行
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(cd.login_url)
    lp = LoginPage(driver)
    # 分割线
    yield driver, lp
    # 后置
    driver.quit()


@pytest.fixture(scope="session", autouse=True)
def init_course():
    # 调用接口，用老师账号新建课程
    c = CourseOperate(*cd.teacher_user)
    course_id, course_code = c.add_course(bj.course_name, bj.class_name)
    yield course_id, course_code, c
    # 会话结束，调用接口删除课程
    c.delete_couse(course_id, cd.teacher_user[1])
    c.close()


@pytest.fixture(scope="class")
def login_web(init_course):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(cd.login_url)
    LoginPage(driver).login(*cd.student_user)
    ip = IndexPage(driver)
    yield driver, ip, init_course
    driver.quit()


@pytest.fixture
def course_grid(init_course):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(cd.login_url)
    LoginPage(driver).login(*cd.student_user)
    ip = IndexPage(driver)
    yield driver, ip, init_course
    driver.quit()



