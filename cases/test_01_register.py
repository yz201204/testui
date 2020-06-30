# -*- coding:utf-8 -*-
"""
-------------------------------------------
@Time : 2020/5/24 16:21 
@Auth : 杨哲
@File : test_01_register.py
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

do_excel = HandleExcel(filename, "register")
cases = do_excel.get_cases()


@ddt
class TestRegister(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        do_log.info("{:=^40s}".format("开始执行注册测试用例"))
        cls.session = HandleRequests()

    @classmethod
    def tearDownClass(cls):
        do_log.info("{:=^40s}".format("注册测试用例执行结束"))
        cls.session.close()

    @data(*cases)
    def test_register(self, case):
        data = ConText.register_parameterization(case["data"])
        url_1 = testcase_config.get_value("url", "url")
        url_2 = case["url"]
        url = url_1 + url_2
        res = self.session.to_requests(url, data, method=case["method"])
        expect_result = case["expected"]
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
