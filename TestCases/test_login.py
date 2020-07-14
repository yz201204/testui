# -*- coding:utf-8 -*-
"""
-------------------------------------------
@Time : 2020/7/11 0:57 
@Auth : 杨哲
@File : test_login.py
@IDE : PyCharm
@Motto : Never Stop Learning
-------------------------------------------
"""
import time
from PageObjects.index_page import IndexPage
from TestDatas import common_datas as cd
from TestDatas import login_datas as ld
import pytest


@pytest.mark.login
@pytest.mark.usefixtures("init_driver")
class TestLogin:

    @pytest.mark.slow
    def test_login_success(self, init_driver):
        # 步骤
        # 登陆页面 - 输入用户名 - 1303845892@qq.com
        # 登陆页面 - 输入密码 - nmb_python
        # 登陆页面 - 点击登陆按钮
        # 断言
        # 首页 - 获取用户元素，确认是否存在
        init_driver[1].login(ld.correct_data_teacher["username"], ld.correct_data_teacher["password"])
        ip = IndexPage(init_driver[0])
        assert ip.if_user_is_exist()
        assert cd.index_url == ip.get_current_url()

    # @data(*ld.incorrect_datas)
    # def test_incorrect(self, incorrect_data):
    #     self.lp.login(incorrect_data["username"], incorrect_data["password"])
    #     self.assertEqual(incorrect_data["check"], self.lp.get_err_msg())
    #     time.sleep(2)

    @pytest.mark.parametrize("incorrect_data", ld.incorrect_datas)
    def test_incorrect(self, incorrect_data, init_driver):
        init_driver[1].login(incorrect_data["username"], incorrect_data["password"])
        assert incorrect_data["check"] == init_driver[1].get_err_msg()
        time.sleep(2)

    @pytest.mark.parametrize("a,b,c", [(1, 3, 4), (10, 35, 45), (22.22, 22.22, 44.44)])
    def test_add(self, a, b, c):
        res = a + b
        assert res == c

    @pytest.mark.fail
    def test_login_no_username_and_password(self, init_driver):
        # 步骤
        # 登陆页面 - 不输入用户名
        # 登陆页面 - 不输入密码
        # 登陆页面 - 点击登陆按钮
        # 断言
        # 登陆页面 - 获取错误提示信息，确认是否为：1、账号不能为空 2、密码不能为空 - p[class="error-tips"]
        init_driver[1].login(ld.null_data["username"], ld.null_data["password"])
        msgs = init_driver[1].get_err_msgs()
        assert ld.null_data["check"][0] == msgs[0]
        assert ld.null_data["check"][1] == msgs[1]
        time.sleep(2)

    def test_login_err_password(self, init_driver):
        # 步骤
        # 登陆页面 - 输入用户名 - 1303845892@qq.com
        # 登陆页面 - 输入错误密码 - nmb_python1
        # 登陆页面 - 点击登陆按钮
        # 断言
        # 登陆页面 - 获取错误提示信息，确认是否为：密码错误, 你还可以尝试X次 - p[class="error-tips"]
        init_driver[1].login(ld.err_passwd["username"], ld.err_passwd["password"])
        assert ld.err_passwd["check"] == init_driver[1].get_err_msg()
        time.sleep(2)

    @pytest.mark.fail
    def test_fail(self):
        assert True


if __name__ == '__main__':
    pass
