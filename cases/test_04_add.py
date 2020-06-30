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

do_excel = HandleExcel(filename, "add")
cases = do_excel.get_cases()


@ddt
class TestAdd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        do_log.info("{:=^40s}".format("开始执行加标测试用例"))
        cls.session = HandleRequests()

    @classmethod
    def tearDownClass(cls):
        do_log.info("{:=^40s}".format("加标测试用例执行结束"))
        cls.session.close()

    @data(*cases)
    def test_add(self, case):
        data = ConText.add_parameterization(case["data"])
        url = testcase_config.get_value("url", "url") + case["url"]
        res = self.session.to_requests(url, data, method=case["method"])
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
