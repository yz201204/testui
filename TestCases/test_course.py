# -*- coding:utf-8 -*-
"""
-------------------------------------------
@Time : 2020/7/11 18:02 
@Auth : 杨哲
@File : test_course.py
@IDE : PyCharm
@Motto : Never Stop Learning
-------------------------------------------
"""
import time
from TestDatas import common_datas as cd
from PageObjects.class_page import ClassPage
import pytest


@pytest.mark.usefixtures("course_grid")
class TestCourseG:

    def test_add_in_course(self, course_grid):
        # 1、首页：点击加入课程
        course_grid[1].add_in_course(course_grid[2][1])
        # 判断加课是否成功
        assert course_grid[1].if_course_is_exsits(course_grid[2][0])
        # time.sleep(2)

    def test_enter_class(self, course_grid):
        # 1、有已加入的课程
        # course_grid[1].add_in_course(course_grid[2][1])
        course_grid[1].enter_class(course_grid[2][0])
        cp = ClassPage(course_grid[0])
        cur_url = cd.base_url + cd.class_url.format(course_grid[2][0])
        assert cp.if_active_is_exist()
        assert cur_url == cp.get_current_url()
        # time.sleep(2)

    def test_quit_course(self, course_grid):
        # 设置允许退课
        course_grid[2][2].allow_quit(course_grid[2][0])
        # 1、首页：点击加入课程
        # course_grid[1].add_in_course(course_grid[2][1])
        # 退课
        course_grid[1].quit_class(course_grid[2][0])
        # 判断前刷新
        course_grid[1].refresh()
        # 判断退课成功
        assert not course_grid[1].if_course_is_not_exsits(course_grid[2][0])
        # time.sleep(2)



