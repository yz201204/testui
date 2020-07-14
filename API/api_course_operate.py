# -*- coding:utf-8 -*-
"""
-------------------------------------------
@Time : 2020/7/11 17:02 
@Auth : 杨哲
@File : api_course_operate.py
@IDE : PyCharm
@Motto : Never Stop Learning
-------------------------------------------
"""
import requests
from TestDatas import common_datas as cd


class CourseOperate:
    # 登陆
    def __init__(self, user, passwd):
        url = cd.base_url + "/UserApi/login"
        data = {"email": user, "password": passwd, "remember": "0"}
        self.s = requests.Session()
        self.s.post(url, data, verify=False)
        # res1 = self.s.post(url, data, verify=False)
        # print(res1.text)

    # 添加课程
    def add_course(self, coursename, classname, semester="2020-2021"):
        url = cd.base_url + "/CourseApi/createCourse"
        data = {"coursename": coursename, "relation": 0, "teachClassid": "", "neednatureclass": 0, "needgrade": 0,
                "needentrance": 0, "canview": 0, "coid": "", "classname": classname, "semester": semester, "term": 1}
        res2 = self.s.post(url, data)
        res_json = res2.json()
        # print(res_json)
        course_id = res_json["data"]["id"]
        course_code = res_json["data"]["code"]
        return course_id, course_code

    # 删除课程
    def delete_couse(self, courseid, password):
        url = cd.base_url + "/CourseApi/delCourse"
        data = {"courseid": courseid, "password": password}
        self.s.post(url, data)
        # res3 = self.s.post(url, data)
        # print(res3.text)

    # 允许退课
    def allow_quit(self, courseid, allowquit=0):
        url = cd.base_url + "/CourseApi/setCourseAllowQuit"
        data = {"courseid": courseid, "isallowquit": allowquit}
        self.s.post(url, data)
        # res4 = self.s.post(url, data)
        # print(res4.text)

    def close(self):
        self.s.close()


if __name__ == '__main__':
    req = CourseOperate(*cd.teacher_user)
    res = req.add_course("webauto", "ysstech")
    req.delete_couse(res[0], cd.teacher_user[1])
