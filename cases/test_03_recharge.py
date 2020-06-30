# -*- coding:utf-8 -*-
"""
-------------------------------------------
@Time : 2020/5/25 18:21 
@Auth : 杨哲
@File : test_03_recharge.py
@IDE : PyCharm
@Motto : Never Stop Learning
-------------------------------------------
"""
from libs.ddt import ddt, data
import unittest
from scripts.handle_excel import HandleExcel
from scripts.handle_config import log_config, testcase_config
from scripts.handle_log import do_log
from scripts.handle_excel import filename
from scripts.handle_requests import HandleRequests
from scripts.handle_context import ConText
from scripts.handle_pymysql import HandleMysql
import json

do_excel = HandleExcel(filename, "recharge")
cases = do_excel.get_cases()


@ddt
class TestRecharge(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        do_log.info("{:=^40s}".format("开始执行充值测试用例"))
        cls.session = HandleRequests()
        cls.do_mysql = HandleMysql()

    @classmethod
    def tearDownClass(cls):
        do_log.info("{:=^40s}".format("充值测试用例执行结束"))
        cls.session.close()
        cls.do_mysql.close()

    @data(*cases)
    def test_recharge(self, case):
        data = ConText.recharge_parameterization(case["data"])
        url = testcase_config.get_value("url", "url") + case["url"]
        if case["check_sql"]:
            check_sql = ConText.recharge_parameterization(case["check_sql"])
            before_leaveamount = self.do_mysql.run(check_sql)["leaveamount"]
        res = self.session.to_requests(url, data, method=case["method"])
        expect_result = str(case["expected"])
        msg = case["title"]
        success_msg = log_config.get_value("msg", "success_result")
        fail_msg = log_config.get_value("msg", "fail_result")
        real_result = res.text
        try:
            self.assertRegex(real_result, 'code.*' + expect_result + '.*data', msg=msg)
            if case["check_sql"]:
                recharge_amount = json.loads(data)["amount"]
                after_leaveamount = self.do_mysql.run(check_sql)["leaveamount"]
                expect_calc_result = round(float(before_leaveamount) + recharge_amount, 2)
                real_calc_result = round(float(after_leaveamount), 2)
                self.assertEqual(expect_calc_result, real_calc_result, msg="数据库中金额判断错误")
            do_log.info("{},执行的结果为：{}".format(msg, success_msg))
            do_excel.write_result(case["case_id"] + 1, real_result, success_msg)
        except AssertionError as e:
            do_log.error("{},执行的结果为：{}；\n具体异常为：{}".format(msg, fail_msg, e))
            do_excel.write_result(case["case_id"] + 1, real_result, fail_msg)
            raise e


if __name__ == '__main__':
    unittest.main()
