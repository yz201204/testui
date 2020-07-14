# -*- coding:utf-8 -*-
"""
-------------------------------------------
@Time : 2020/7/11 16:01 
@Auth : 杨哲
@File : login_datas.py
@IDE : PyCharm
@Motto : Never Stop Learning
-------------------------------------------
"""
# 老师正常登陆数据
correct_data_teacher = {"username": "1303845892@qq.com", "password": "nmb_python"}
# 学生正常登陆数据
correct_data_student = {"username": "408848063@qq.com", "password": "nmb_python"}
# 异常登陆数据
incorrect_datas = [
    {"username": "1303845892@qq.com", "password": "", "check": "密码不能为空"},
    {"username": "", "password": "nmb_python", "check": "账号不能为空"},
    {"username": "1303845892", "password": "nmb_python", "check": "用户不存在"}
]
# 错误密码登陆
err_passwd = {"username": "1303845892@qq.com", "password": "nmb_python1", "check": "密码错误, 你还可以尝试4次"}
# 不输入用户名、密码提示信息
null_data = {"username": "", "password": "", "check": ["账号不能为空", "密码不能为空"]}
