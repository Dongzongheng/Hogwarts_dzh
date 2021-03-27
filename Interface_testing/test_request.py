#! /usr/bin/python
# -*- coding: utf-8 -*-
import json

import requests

class TestRequest():
    def setup(self):
        self.token = self.get_token()

    def get_token(self):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww1a99454a1569bc1a&corpsecret=5uCd436Dozlqx_r5rFDKojdYF3MzjQv0urCqjjZPXYg")
        return r.json()['access_token']

    def test_get_info(self):
        user_id = "DongZongHeng"
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={user_id}")
        print(r.json())

    def test_create_user(self):
        data = {
            "userid": "ADCCCCCCCCCCCC",
            "name": "UZI",
            "alias": "xiaogou",
            "mobile": "+86 13812345678",
            "department": [1, 2],
        }
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}", json=data)
        print(r.json())

    def test_update_user(self):
        data = {
            "userid": "ADCCCCCCCCCCCC",
            "name": "UZIIIIII",
        }
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}", json=data)
        print(r.json())

    def test_del_user(self):
        user_id = "ADCCCCCCCCCCCC"
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={user_id}")
        print(r.json())