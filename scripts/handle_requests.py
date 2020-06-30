# -*- coding:utf-8 -*-
"""
-------------------------------------------
@Time : 2020/5/23 16:32 
@Auth : 杨哲
@File : test_requests.py
@IDE : PyCharm
@Motto : Never Stop Learning
-------------------------------------------
"""
import requests
import json


class HandleRequests:
    def __init__(self):
        self.session = requests.Session()

    def to_requests(self, url, data=None, method='get', is_josn=False, **kwargs):
        method = method.upper()
        data = str(data)
        try:
            data = json.loads(data)
        except Exception:
            data = eval(data)

        if method == 'GET':
            res = self.session.get(url, params=data, **kwargs)
        elif method == 'POST':
            if is_josn:
                res = self.session.post(url, json=data, **kwargs)
            else:
                res = self.session.post(url, data=data, **kwargs)
        else:
            res = None
        return res

    def close(self):
        self.session.close()


if __name__ == '__main__':
    register_url = 'http://test.lemonban.com/futureloan/mvc/api/member/register'
    login_url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
    recharge_url = 'http://test.lemonban.com/futureloan/mvc/api/member/recharge'
    register_data = {
        "mobilephone": "13312412345",
        "pwd": "123456"
    }
    login_data = {
        "mobilephone": "13312222233",
        "pwd": "123456"
    }
    recharge_data = {
        "mobilephone": "13312222233",
        "amount": 1000
    }
    headers = {
        "User-Agent": "Mozilla/5.0 yangzhe"
    }
    session = HandleRequests()
    register_res = session.to_requests(register_url, register_data, headers=headers)
    login_res = session.to_requests(login_url, login_data, 'post', headers=headers)
    recharge_res = session.to_requests(recharge_url, recharge_data, 'post', headers=headers)
    session.close()
