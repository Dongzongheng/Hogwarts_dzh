#! /usr/bin/python
# -*- coding: utf-8 -*-
import yaml
from selenium.webdriver.common.by import By

from UI_Framework.ui_framework.page.basepage import BasePage
from UI_Framework.ui_framework.page.search import Search


class MarketPage(BasePage):
    def goto_Search(self):
        # self.find_and_click(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/action_search"]')
        with open("../page/market_page.yaml", mode='r', encoding="utf-8") as f:
            function = yaml.load(f)
        # 从关键字中取出一个函数
        steps = function.get("goto_search")
        # 解析每一组关键字
        for step in steps:
            # 如果发现关键字是 find_and_click , 就调用已经封装好的 find_and_click 即可
            if step.get("action") == "find_and_click":
                self.find_and_click(step.get('locator'),step.get('value'))
        return Search(self.driver)