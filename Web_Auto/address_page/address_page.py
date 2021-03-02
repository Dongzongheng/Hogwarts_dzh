#! /usr/bin/python
# -*- coding: utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class AddressPage:
    def __init__(self,driver):
        self.driver = driver

    def add_member(self):
        def wait_name(driver):
            sleep(1)
            driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn js_add_member']")[-1].click()
            eles = driver.find_elements(By.XPATH, "//*[@id='username']")
            return len(eles) > 0
        WebDriverWait(self.driver, 20).until(wait_name)
        self.driver.find_element(By.XPATH, "//*[@id='username']").send_keys("Dzh")
        self.driver.find_element(By.XPATH, "//*[@id='memberAdd_english_name']").send_keys("9527")
        self.driver.find_element(By.XPATH, "//*[@id='memberAdd_acctid']").send_keys("123456")
        self.driver.find_element(By.XPATH, "//*[@class='qui_inputText ww_inputText ww_telInput_mainNumber']").send_keys("15658095274")
        self.driver.find_element(By.XPATH, "//*[@class='qui_btn ww_btn js_btn_save']").click()

