#! /usr/bin/python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from UI_Framework.ui_framework.page.app import  App




class TestMarket:
    def setup(self):
        self.app = App()

    def test_goto_market(self):
        self.app.start().goto_main().goto_market().goto_Search().search()
