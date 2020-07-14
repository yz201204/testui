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


@pytest.fixture
def get_home(login_web):
    yield login_web
    login_web[0].get(cd.index_url)


@pytest.mark.usefixtures("get_home")
class TestCourse:

    def test_add_in_course(self, get_home):
        # 1、首页：点击加入课程
        get_home[1].add_in_course(get_home[2][1])
        # 判断加课是否成功
        assert get_home[1].if_course_is_exsits(get_home[2][0])
        # time.sleep(2)

    def test_enter_class(self, get_home):
        get_home[1].enter_class(get_home[2][0])
        cp = ClassPage(get_home[0])
        cur_url = cd.base_url + cd.class_url.format(get_home[2][0])
        assert cp.if_active_is_exist()
        assert cur_url == cp.get_current_url()
        # time.sleep(2)

    def test_quit_course(self, get_home):
        # 设置允许退课
        get_home[2][2].allow_quit(get_home[2][0])
        # # 1、返回首页 后置处理了这里不再处理
        # get_home[1].get_url()
        # 退课
        get_home[1].quit_class(get_home[2][0])
        # 判断前刷新 删除后页面元素可能没及时消失 加了智能等待不用刷新了
        # get_home[1].refresh()
        # 判断退课成功
        assert not get_home[1].if_course_is_not_exsits(get_home[2][0])
        # time.sleep(2)



