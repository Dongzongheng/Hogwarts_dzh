#! /usr/bin/python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from UI_Framework.ui_framework.page.basepage import BasePage


class Search(BasePage):
    def search(self):
        self.find_and_send(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/search_input_text"]', "alibaba")
