# -*- coding:utf-8 -*-
"""
-------------------------------------------
@Time : 2020/5/26 10:54 
@Auth : 杨哲
@File : test_05_invest.py
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

do_excel = HandleExcel(filename, "invest")
cases = do_excel.get_cases()


@ddt
class TestInvest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        do_log.info("{:=^40s}".format("开始执行投资测试用例"))
        cls.session = HandleRequests()
        cls.do_mysql = HandleMysql()

    @classmethod
    def tearDownClass(cls):
        do_log.info("{:=^40s}".format("投资测试用例执行结束"))
        cls.session.close()
        cls.do_mysql.close()

    @data(*cases)
    def test_invest(self, case):
        data = ConText.invest_parameterization(case["data"])
        url = testcase_config.get_value("url", "url") + case["url"]
        res = self.session.to_requests(url, data, method=case["method"])
        if "加标成功" in res.text:
            check_sql = ConText.invest_parameterization(case["check_sql"])
            result = self.do_mysql.run(check_sql)
            # ConText.loan_id = result.get("id")
            setattr(ConText, "loan_id", str(result.get("id")))
        expect_result = str(case["expected"])
        msg = case["title"]
        success_msg = log_config.get_value("msg", "success_result")
        fail_msg = log_config.get_value("msg", "fail_result")
        real_result = res.text
        try:
            self.assertEqual(expect_result, real_result, msg=msg)
            do_log.info("{},执行的结果为：{}".format(msg, success_msg))
            do_excel.write_result(case["case_id"] + 1, real_result, success_msg)
        except AssertionError as e:
            do_log.error("{},执行的结果为：{}；\n具体异常为：{}".format(msg, fail_msg, e))
            do_excel.write_result(case["case_id"] + 1, real_result, fail_msg)
            raise e


if __name__ == '__main__':
    unittest.main()
