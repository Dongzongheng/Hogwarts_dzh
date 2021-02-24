#! /usr/bin/python
# -*- coding: utf-8 -*-
import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class Testselenium():
    def setup(self):
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9345'
        self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_reuse(self):
        self.driver.get('https://work.weixin.qq.com/')
        self.driver.find_element_by_class_name("index_head_info_pCDownloadBtn").click()
        self.driver.find_element_by_xpath("//*[@id='corp_name']").click()
        self.driver.find_element_by_xpath("//*[@id='corp_name']").send_keys("dzh")
        sleep(5)
        self.driver.close()

    def test_login_tmp(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()

    def test_login_cookie(self):

        # 存入 cookie
        # cookies = self.driver.get_cookies()
        # with open("tmp2.text","w", encoding="utf-8") as f:
        #     json.dump(cookies, f)

        # 读取 cookie
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        cookie = self.driver.get_cookies()
        with open("tmp_cookie.txt","w", encoding="utf-8") as f:
            json.dump(cookie, f)
        with open("tmp_cookie.txt","r", encoding="utf-8") as f:
            cookie = json.load(f)
        for i in cookie:
            self.driver.add_cookie(i)
        self.driver.refresh()
        sleep(6)
