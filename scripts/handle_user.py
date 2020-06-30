# -*- coding:utf-8 -*-
"""
-------------------------------------------
@Time : 2020/5/25 15:21 
@Auth : 杨哲
@File : handle_user.py
@IDE : PyCharm
@Motto : Never Stop Learning
-------------------------------------------
"""
from scripts.handle_pymysql import HandleMysql
from scripts.handle_requests import HandleRequests
from scripts.handle_config import testcase_config
from scripts.constants import USER_ACCOUNTS_PATH


class HandleUser:
    def create_new_user(self, regname, pwd='123456'):
        self.handle_mysql = HandleMysql()
        self.send_requests = HandleRequests()
        self.url = testcase_config.get_value("url", "url") + "/member/register"
        self.sql = "select id from member where mobilephone = %s;"
        while True:
            self.mobilephone = self.handle_mysql.not_existed_tel()
            self.data = {"mobilephone": self.mobilephone, "pwd": pwd, "regname": regname}
            self.send_requests.to_requests(self.url, data=self.data, method='post')
            result = self.handle_mysql.run(self.sql, args=(self.mobilephone,))
            if result:
                self.user_id = result["id"]
                break
        self.user_dict = {
            regname: {
                "Id": self.user_id,
                "regname": regname,
                "mobilephone": self.mobilephone,
                "pwd": pwd
            }
        }
        self.handle_mysql.close()
        self.send_requests.close()
        return self.user_dict

    def generate_users_config(self):
        self.users_datas_dict = {}
        self.user_filename = USER_ACCOUNTS_PATH
        self.users_datas_dict.update(self.create_new_user("admin_user"))
        self.users_datas_dict.update(self.create_new_user("invest_user"))
        self.users_datas_dict.update(self.create_new_user("borrow_user"))
        testcase_config.write_config(self.users_datas_dict, self.user_filename)


if __name__ == '__main__':
    HandleUser().generate_users_config()
