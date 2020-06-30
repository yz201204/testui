# -*- coding:utf-8 -*-
"""
-------------------------------------------
@Time : 2020/5/24 16:11 
@Auth : 杨哲
@File : handle_re.py
@IDE : PyCharm
@Motto : Never Stop Learning
-------------------------------------------
"""
import re
from scripts.handle_pymysql import HandleMysql
from scripts.handle_config import HandleConfig
from scripts.constants import USER_ACCOUNTS_PATH


class ConText:
    not_existed_tel_pattern = r"\${not_existed_tel}"
    invest_user_tel_pattern = r"\${invest_user_tel}"
    invest_user_pwd_pattern = r'\${invest_user_pwd}'
    admin_user_tel_pattern = r'\${admin_user_tel}'
    admin_user_pwd_pattern = r'\${admin_user_pwd}'
    borrow_user_id_pattern = r'\${borrow_user_id}'
    invest_user_id_pattern = r'\${invest_user_id}'
    loan_id_pattern = r'\${loan_id}'
    not_existed_loan_id_pattern = r'\${not_existed_loan_id}'
    not_existed_user_id_pattern = r'\${not_existed_user_id}'
    handle_user_config = HandleConfig(USER_ACCOUNTS_PATH)

    @classmethod
    def not_existed_tel_replace(cls, data):
        if re.search(cls.not_existed_tel_pattern, data):
            do_mysql = HandleMysql()
            data = re.sub(cls.not_existed_tel_pattern, do_mysql.not_existed_tel(), data)
            do_mysql.close()
        return data

    @classmethod
    def invest_user_tel_replace(cls, data):
        if re.search(cls.invest_user_tel_pattern, data):
            data = re.sub(cls.invest_user_tel_pattern,
                          cls.handle_user_config.get_value("invest_user", "mobilephone"),
                          data)
        return data

    @classmethod
    def invest_user_pwd_replace(cls, data):
        if re.search(cls.invest_user_pwd_pattern, data):
            data = re.sub(cls.invest_user_pwd_pattern,
                          cls.handle_user_config.get_value("invest_user", "pwd"),
                          data)
        return data

    @classmethod
    def admin_user_tel_replace(cls, data):
        if re.search(cls.admin_user_tel_pattern, data):
            data = re.sub(cls.admin_user_tel_pattern,
                          cls.handle_user_config.get_value("admin_user", "mobilephone"),
                          data)
        return data

    @classmethod
    def admin_user_pwd_replace(cls, data):
        if re.search(cls.admin_user_pwd_pattern, data):
            data = re.sub(cls.admin_user_pwd_pattern,
                          cls.handle_user_config.get_value("admin_user", "pwd"),
                          data)
        return data

    @classmethod
    def borrow_user_id_replace(cls, data):
        if re.search(cls.borrow_user_id_pattern, data):
            data = re.sub(cls.borrow_user_id_pattern,
                          cls.handle_user_config.get_value("borrow_user", "id"),
                          data)
        return data

    @classmethod
    def invest_user_id_replace(cls, data):
        if re.search(cls.invest_user_id_pattern, data):
            data = re.sub(cls.invest_user_id_pattern,
                          cls.handle_user_config.get_value("invest_user", "id"),
                          data)
        return data

    @classmethod
    def loan_id_replace(cls, data):
        if re.search(cls.loan_id_pattern, data):
            data = re.sub(cls.loan_id_pattern,
                          # str(cls.loan_id),
                          getattr(ConText, "loan_id"),
                          data)
        return data

    @classmethod
    def not_existed_loan_id_replace(cls, data):
        if re.search(cls.not_existed_loan_id_pattern, data):
            do_mysql = HandleMysql()
            data = re.sub(cls.not_existed_loan_id_pattern,
                          do_mysql.not_existed_loan_id(),
                          data)
            do_mysql.close()
        return data

    @classmethod
    def not_existed_user_id_replace(cls, data):
        if re.search(cls.not_existed_user_id_pattern, data):
            do_mysql = HandleMysql()
            data = re.sub(cls.not_existed_user_id_pattern,
                          do_mysql.not_existed_user_id(),
                          data)
            do_mysql.close()
        return data

    @classmethod
    def register_parameterization(cls, data):
        data = cls.not_existed_tel_replace(data)
        data = cls.invest_user_tel_replace(data)
        return data

    @classmethod
    def login_parameterization(cls, data):
        data = cls.not_existed_tel_replace(data)
        data = cls.invest_user_tel_replace(data)
        data = cls.invest_user_pwd_replace(data)
        return data

    @classmethod
    def recharge_parameterization(cls, data):
        data = cls.not_existed_tel_replace(data)
        data = cls.invest_user_tel_replace(data)
        data = cls.invest_user_pwd_replace(data)
        return data

    @classmethod
    def add_parameterization(cls, data):
        data = cls.admin_user_tel_replace(data)
        data = cls.admin_user_pwd_replace(data)
        data = cls.not_existed_user_id_replace(data)
        data = cls.borrow_user_id_replace(data)
        return data

    @classmethod
    def invest_parameterization(cls, data):
        data = cls.admin_user_tel_replace(data)
        data = cls.admin_user_pwd_replace(data)
        data = cls.borrow_user_id_replace(data)
        data = cls.invest_user_tel_replace(data)
        data = cls.invest_user_id_replace(data)
        data = cls.invest_user_pwd_replace(data)
        data = cls.loan_id_replace(data)
        data = cls.not_existed_loan_id_replace(data)
        data = cls.not_existed_user_id_replace(data)

        return data


if __name__ == '__main__':
    '''one_str = '{"mobilephone": "${not_existed_tel}", "pwd": "123456"}'
    two_str = '{"mobilephone": "${not_existed_tel}", "pwd": "123456", "regname": ""}'
    three_str = '{"mobilephone": "${not_existed_tel}", "pwd": "123456", "regname": "yangzhe"}'
    four_str = '{"mobilephone": "${not_existed_tel}", "pwd": ""}'
    five_str = '{"mobilephone": "", "pwd": "123456", "regname": "yangzhe"}'
    six_str = '{"mobilephone": "1861234567", "pwd": "123456", "regname": "yangzhe"}'
    seven_str = '{"mobilephone": "186123456789", "pwd": "123456", "regname": "yangzhe"}'
    eight_str = '{"mobilephone": "${not_existed_tel}", "pwd": "12345", "regname": "yangzhe"}'
    nine_str = '{"mobilephone": "${not_existed_tel}", "pwd": "1234567890123456789", "regname": "yangzhe"}'
    ten_str = '{"mobilephone": "${invest_user_tel}", "pwd": "123456", "regname": "yangzhe"}'
    print(ConText.register_parameterization(one_str))
    print(ConText.register_parameterization(two_str))
    print(ConText.register_parameterization(three_str))
    print(ConText.register_parameterization(four_str))
    print(ConText.register_parameterization(five_str))
    print(ConText.register_parameterization(six_str))
    print(ConText.register_parameterization(seven_str))
    print(ConText.register_parameterization(eight_str))
    print(ConText.register_parameterization(nine_str))
    print(ConText.register_parameterization(ten_str))
    login_1 = '{"mobilephone": "${invest_user_tel}", "pwd": "${invest_user_pwd}"}'
    login_2 = '{"mobilephone": "", "pwd": "${invest_user_pwd}"}'
    login_3 = '{"mobilephone": "${invest_user_tel}", "pwd": ""}'
    login_4 = '{"mobilephone": "${not_existed_tel}", "pwd": "${invest_user_pwd}"}'
    login_5 = '{"mobilephone": "${invest_user_tel}", "pwd": "${invest_user_pwd}1"}'
    print(ConText.login_parameterization(login_1))
    print(ConText.login_parameterization(login_2))
    print(ConText.login_parameterization(login_3))
    print(ConText.login_parameterization(login_4))
    print(ConText.login_parameterization(login_5))
    one_recharge = '{"mobilephone": "${invest_user_tel}", "pwd": "${invest_user_pwd}"}'
    print(ConText().recharge_parameterization(one_recharge))
    one_recharge = '{"mobilephone": "${invest_user_tel}", "amount": 600}'
    print(ConText().recharge_parameterization(one_recharge))
    one_recharge = '{"mobilephone": "${invest_user_tel}", "amount": 600.1}'
    print(ConText().recharge_parameterization(one_recharge))
    one_recharge = '{"mobilephone": "${invest_user_tel}", "amount": 600.22}'
    print(ConText().recharge_parameterization(one_recharge))
    one_recharge = '{"mobilephone": "${invest_user_tel}", "amount": 500000}'
    print(ConText().recharge_parameterization(one_recharge))
    one_recharge = '{"mobilephone": "", "amount": 600}'
    print(ConText().recharge_parameterization(one_recharge))
    one_recharge = '{"mobilephone": "1861234123", "amount": 600}'
    print(ConText().recharge_parameterization(one_recharge))
    one_recharge = '{"mobilephone": "186123412345", "amount": 600}'
    print(ConText().recharge_parameterization(one_recharge))
    one_recharge = '{"mobilephone": "${not_existed_tel}", "amount": 600}'
    print(ConText().recharge_parameterization(one_recharge))
    one_recharge = '{"mobilephone": "${invest_user_tel}", "amount": 0}'
    print(ConText().recharge_parameterization(one_recharge))
    one_recharge = '{"mobilephone": "${invest_user_tel}", "amount": -600}'
    print(ConText().recharge_parameterization(one_recharge))
    one_recharge = '{"mobilephone": "${invest_user_tel}", "amount": null}'
    print(ConText().recharge_parameterization(one_recharge))
    one_recharge = '{"mobilephone": "${invest_user_tel}", "amount": 600.222}'
    print(ConText().recharge_parameterization(one_recharge))
    one_recharge = '{"mobilephone": "${invest_user_tel}", "amount": 500001}'
    print(ConText().recharge_parameterization(one_recharge))
    one_recharge = '{"mobilephone": "${invest_user_tel}", "amount": "50万"}'
    print(ConText().recharge_parameterization(one_recharge))
    one_select = 'SELECT leaveamount FROM future.`member` WHERE mobilephone ="${invest_user_tel}"'
    print(ConText().recharge_parameterization(one_select))
    one_select = 'SELECT leaveamount FROM future.`member` WHERE mobilephone ="${invest_user_tel}"'
    print(ConText().recharge_parameterization(one_select))
    one_select = 'SELECT leaveamount FROM future.`member` WHERE mobilephone ="${invest_user_tel}"'
    print(ConText().recharge_parameterization(one_select))
    one_select = 'SELECT leaveamount FROM future.`member` WHERE mobilephone ="${invest_user_tel}"'
    print(ConText().recharge_parameterization(one_select))
    add_data = '{"mobilephone": "${admin_user_tel}", "pwd": "${admin_user_pwd}"}'
    print(ConText().add_parameterization(add_data))
    add_data = '{"memberId":"${borrow_user_id}","title":"试试人品行不行，借个2w玩玩","amount":20000,"loanRate":12.0,"loanTerm":3,
    "loanDateType":0,"repaymemtWay":11,"biddingDays":5}'
    print(ConText().add_parameterization(add_data))
    add_data = '{"memberId": null, "title": "试试人品行不行，借个2w玩玩", "amount": 20000, "loanRate": 12.0, "loanTerm": 3, 
    "loanDateType": 0,"repaymemtWay": 11, "biddingDays": 5}'
    print(ConText().add_parameterization(add_data))
    add_data = '{"memberId": "${borrow_user_id}", "title": "", "amount": 20000, "loanRate": 12.0, "loanTerm": 3, 
    "loanDateType": 0,"repaymemtWay": 11, "biddingDays": 5}'
    print(ConText().add_parameterization(add_data))
    add_data = '{"memberId": "${borrow_user_id}", "title": "试试人品行不行，借个2w玩玩", "amount": null, "loanRate": 12.0,
     "loanTerm": 3, "loanDateType": 0, "repaymemtWay": 11, "biddingDays": 5}'
    print(ConText().add_parameterization(add_data))
    add_data = '{"memberId": "${borrow_user_id}", "title": "试试人品行不行，借个2w玩玩", "amount": 20000, "loanRate": null, 
    "loanTerm": 3, "loanDateType": 0, "repaymemtWay": 11, "biddingDays": 5}'
    print(ConText().add_parameterization(add_data))
    add_data = '{"memberId": "${borrow_user_id}", "title": "试试人品行不行，借个2w玩玩", "amount": 20000, "loanRate": 12.0, 
    "loanTerm": null, "loanDateType": 0, "repaymemtWay": 11, "biddingDays": 5}'
    print(ConText().add_parameterization(add_data))
    add_data = '{"memberId": "${borrow_user_id}", "title": "试试人品行不行，借个2w玩玩", "amount": 20000, "loanRate": 12.0, 
    "loanTerm": 3, "loanDateType": null, "repaymemtWay": 11, "biddingDays": 5}'
    print(ConText().add_parameterization(add_data))
    add_data = '{"memberId": "${borrow_user_id}", "title": "试试人品行不行，借个2w玩玩", "amount": 20000, "loanRate": 12.0, 
    "loanTerm": 3, "loanDateType": 0, "repaymemtWay": null, "biddingDays": 5}'
    print(ConText().add_parameterization(add_data))
    add_data = '{"memberId": "${borrow_user_id}", "title": "试试人品行不行，借个2w玩玩", "amount": 20000, "loanRate": 12.0, 
    "loanTerm": 3, "loanDateType": 0, "repaymemtWay": 11, "biddingDays": null}'
    print(ConText().add_parameterization(add_data))
    add_data = '{"memberId": "-${borrow_user_id}", "title": "试试人品行不行，借个2w玩玩", "amount": 20000, "loanRate": 12.0,
     "loanTerm": 3,  "loanDateType": 0, "repaymemtWay": 11, "biddingDays": 5}'
    print(ConText().add_parameterization(add_data))
    add_data = '{"memberId": 1.2, "title": "试试人品行不行，借个2w玩玩", "amount": 20000, "loanRate": 12.0, "loanTerm": 3,
     "loanDateType": 0, "repaymemtWay": 11, "biddingDays": 5}'
    print(ConText().add_parameterization(add_data))
    add_data = '{"memberId": "${borrow_user_id}", "title": "试试人品行不行，借个2w玩玩", "amount": -20000, "loanRate": 12.0, 
    "loanTerm": 3,"loanDateType": 0, "repaymemtWay": 11, "biddingDays": 5}'
    print(ConText().add_parameterization(add_data))
    add_data = '{"memberId": "${borrow_user_id}", "title": "试试人品行不行，借个2w玩玩", "amount": 20000.1, "loanRate": 12.0, 
    "loanTerm": 3,"loanDateType": 0, "repaymemtWay": 11, "biddingDays": 5}'
    print(ConText().add_parameterization(add_data))
    add_data = '{"memberId": "${borrow_user_id}", "title": "试试人品行不行，借个2w玩玩", "amount": 999, "loanRate": 12.0, 
    "loanTerm": 3, "loanDateType": 0, "repaymemtWay": 11, "biddingDays": 5}'
    print(ConText().add_parameterization(add_data))
    add_data = '{"memberId": "${borrow_user_id}", "title": "试试人品行不行，借个2w玩玩", "amount": 1000, "loanRate": 12.0, 
    "loanTerm": 3,"loanDateType": 0, "repaymemtWay": 11, "biddingDays": 5}'
    print(ConText().add_parameterization(add_data))'''
    one_invest = '{"mobilephone": "${admin_user_tel}", "pwd": "${admin_user_pwd}"}'
    print(ConText().invest_parameterization(one_invest))
    one_invest = '{"memberId": "${borrow_user_id}", "title": "试试人品行不行，借个2w玩玩", "amount": "20000", ' \
                 '"loanRate": 12.0, "loanTerm": 3,"loanDateType": 0, "repaymemtWay": 11, "biddingDays": 5}'
    print(ConText().invest_parameterization(one_invest))
    one_invest = '{"id": "${loan_id}", "status": 4}'
    print(ConText().invest_parameterization(one_invest))
    one_invest = '{"mobilephone": "${invest_user_tel}", "pwd": "${invest_user_pwd}"}'
    print(ConText().invest_parameterization(one_invest))
    one_invest = '{"memberId": "${invest_user_id}", "password": "${invest_user_pwd}", "loanId": "${loan_id}", ' \
                 '"amount": 100}'
    print(ConText().invest_parameterization(one_invest))
    one_invest = '{"memberId": null, "password": "${invest_user_pwd}", "loanId": "${loan_id}", "amount": 100}'
    print(ConText().invest_parameterization(one_invest))
    one_invest = '{"memberId": "${invest_user_id}", "password": "", "loanId": "${loan_id}", "amount": 100}'
    print(ConText().invest_parameterization(one_invest))
    one_invest = '{"memberId": "${invest_user_id}", "password": "${invest_user_pwd}", "loanId": null, "amount": 100}'
    print(ConText().invest_parameterization(one_invest))
    one_invest = '{"memberId": "${invest_user_id}", "password": "${invest_user_pwd}", "loanId": "${loan_id}", ' \
                 '"amount": null}'
    print(ConText().invest_parameterization(one_invest))
    one_invest = '{"memberId": "-${invest_user_id}", "password": "${invest_user_pwd}", "loanId": "${loan_id}", ' \
                 '"amount": 100}'
    print(ConText().invest_parameterization(one_invest))
    one_invest = '{"memberId": 0, "password": "${invest_user_pwd}", "loanId": "${loan_id}", "amount": 100}'
    print(ConText().invest_parameterization(one_invest))
    one_invest = '{"memberId": "${invest_user_id}", "password": "${invest_user_pwd}", "loanId": "-${loan_id}", ' \
                 '"amount": 100}'
    print(ConText().invest_parameterization(one_invest))
    one_invest = '{"memberId": "${invest_user_id}", "password": "${invest_user_pwd}", "loanId": 0, "amount": 100}'
    print(ConText().invest_parameterization(one_invest))
    one_invest = '{"memberId": "${invest_user_id}", "password": "12345", "loanId": "${loan_id}", "amount": 100}'
    print(ConText().invest_parameterization(one_invest))
    one_invest = '{"memberId": "${invest_user_id}", "password": "${invest_user_pwd}${invest_user_pwd}' \
                 '${invest_user_pwd}1","loanId": "${loan_id}", "amount": 100}'
    print(ConText().invest_parameterization(one_invest))
    one_invest = '{"memberId": "${invest_user_id}", "password": "${invest_user_pwd}1", "loanId": "${loan_id}", ' \
                 '"amount": 100}'
    print(ConText().invest_parameterization(one_invest))
    one_invest = '{"memberId": "${invest_user_id}", "password": "${invest_user_pwd}", "loanId": "${loan_id}", ' \
                 '"amount": -100}'
    print(ConText().invest_parameterization(one_invest))
    one_invest = '{"memberId": "${invest_user_id}", "password": "${invest_user_pwd}", "loanId": "${loan_id}", ' \
                 '"amount": 101}'
    print(ConText().invest_parameterization(one_invest))
    one_invest = '{"memberId": "${not_existed_user_id}", "password": "${invest_user_pwd}", "loanId": "${loan_id}", ' \
                 '"amount": 100}'
    print(ConText().invest_parameterization(one_invest))
    one_invest = '{"memberId": "${invest_user_id}", "password": "${invest_user_pwd}", "loanId": ' \
                 '"${not_existed_loan_id}","amount": 100}'
    print(ConText().invest_parameterization(one_invest))
    not_existed_user_id = '{"memberId":"${not_existed_user_id}","title":"试试人品行不行，借个2w玩玩","amount":20000,' \
                          '"loanRate":12.0,"loanTerm":3,"loanDateType":0,"repaymemtWay":11,"biddingDays":5}'
    print(ConText().add_parameterization(not_existed_user_id))
