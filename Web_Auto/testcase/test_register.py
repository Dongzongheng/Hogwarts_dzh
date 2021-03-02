#! /usr/bin/python
# -*- coding: utf-8 -*-
from time import sleep

from Web_Auto.login_page.main_page import MainPage


class TestRegister:
    def  test_register(self):
        main = MainPage()
        main.goto_register().register()
        sleep(6)

    def test_register1(self):
        main = MainPage()
        main.goto_login().goto_register().register()
        sleep(6)

