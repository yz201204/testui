# -*- coding:utf-8 -*-
"""
-------------------------------------------
@Time : 2020/5/23 20:18 
@Auth : 杨哲
@File : test_pymysql.py
@IDE : PyCharm
@Motto : Never Stop Learning
-------------------------------------------
"""
import pymysql
from scripts.handle_config import mysql_config
import random


class HandleMysql:
    def __init__(self):
        self.conn = pymysql.connect(host=mysql_config.get_value("lemon", "host"),
                                    database=mysql_config.get_value("lemon", "database"),
                                    user=mysql_config.get_value("lemon", "user"),
                                    password=mysql_config.get_value("lemon", "password"),
                                    port=mysql_config.get_int("lemon", "port"),
                                    charset=mysql_config.get_value("lemon", "charset"),
                                    cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.conn.cursor()

    def run(self, sql, args=None, is_more=False):
        self.cursor.execute(sql, args=args)
        self.conn.commit()
        if is_more:
            return self.cursor.fetchall()
        else:
            return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def not_existed_tel(self):
        self.mobilephone = self.range_number()
        self.flag = True
        while self.flag:
            self.sql = "select * from member where MobilePhone = %s;"
            self.res = self.run(self.sql, args=(self.mobilephone,))
            if not self.res:
                self.flag = False
            else:
                self.mobilephone = self.range_number()
        return self.mobilephone

    def invest_user_tel(self):
        self.sql_one = "select * from member limit 1 OFFSET 0"
        self.res_one = self.run(self.sql_one)
        return self.res_one['MobilePhone']

    def not_existed_loan_id(self):
        self.loan_id = self.create_number(6)
        self.flag = True
        while self.flag:
            self.sql = "select * from loan where id = %s;"
            self.res = self.run(self.sql, args=(self.loan_id,))
            if not self.res:
                self.flag = False
            else:
                self.loan_id = self.create_number(6)
        return self.loan_id

    def not_existed_user_id(self):
        self.member_id = self.create_number(4)
        self.flag = True
        while self.flag:
            self.sql = "select * from member where id = %s;"
            self.res = self.run(self.sql, args=(self.member_id,))
            if not self.res:
                self.flag = False
            else:
                self.member_id = self.create_number(4)
        return self.member_id

    @staticmethod
    def range_number():
        start_num = random.choice(mysql_config.get_eval_data("mobile phone",
                                                             "start_num"))
        end_num = []
        for i in range(8):
            end_num.append(random.sample("0123456789", 1)[0])
        end_num = ''.join(end_num)
        return str(start_num) + end_num

    @staticmethod
    def create_number(num=3):
        list_num = []
        for i in range(num):
            list_num.append(random.sample("0123456789", 1)[0])
        if list_num[0] == '0':
            list_num[0] = random.sample("123456789", 1)[0]
        range_num = ''.join(list_num)
        return range_num


if __name__ == '__main__':
    mobiephoe = '18330372028'
    sql_1 = "select * from member where MobilePhone = %s;"
    sql_2 = "select * from member limit 10 OFFSET 0"
    do_mysql = HandleMysql()
    res1 = do_mysql.run(sql_1, args=(mobiephoe,))
    res2 = do_mysql.run(sql_2, is_more=True)
    my_range_num = do_mysql.not_existed_tel()
    print(my_range_num)
    print(do_mysql.invest_user_tel())
    print(do_mysql.not_existed_user_id())
    do_mysql.close()
