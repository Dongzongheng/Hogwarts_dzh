#! /usr/bin/python
# -*- coding: utf-8 -*-

# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from Appium_Auto.AppModule.test_appium_swipe_find import swipe_up_search_element


class TestAppium:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        # caps["undefined"] = undefined
        caps["ensureWebviewsHavePages"] = True

        # 客户端与appium服务器建立链接的代码

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(30)

    def teardown(self):
        self.driver.quit()

    def test_appium(self):
        el1 = self.driver.find_element_by_id("com.tencent.wework:id/igk")
        el1.click()
        el2 = self.driver.find_element_by_id("com.tencent.wework:id/gy9")
        el2.send_keys("霍格沃兹")
        el3 = self.driver.find_element_by_id("com.tencent.wework:id/dtv")
        el3.click()

    def test_daka(self):
        '''
        前提条件：已登录状态（noReset=True）
        打卡用例：
        1.打开【企业微信】应用
        2，进入【工作台】
        3.点击【打卡】
        4.选择【外出打卡】tab
        5.点击【第N次打卡】
        6.验证【外出打卡成功】
        7.退出【企业微信】应用
        :return:
        '''
        self.driver.find_element(MobileBy.XPATH, "//android.view.ViewGroup//*[@text='工作台']").click()
        # android_uiautomator 里面要用双引号，外面用单引号。
        # 向下滑动两次，再向上查找，直到找到元素
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("打卡").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "次外出")]').click()
        print(self.driver.page_source)
        # sleep(2)
        # assert "外出打卡成功" in self.driver.page_source
        # 激活隐式等待
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡成功']")

    def test_address(self, username, mobilephone):
        '''
        前提条件：已登录
        打卡用例：
        1、打开【企业微信】应用
        2、进入【通讯录】
        3、滑动页面查询【添加成员】并点击
        4、点击【手动输入添加】
        5、输入【姓名】、【手机号】，点击【保存】
        6、退出【企业微信】应用
        :return:
        '''
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 滑动查找  目前是向下滑动两次，再向上查找，知道找到元素
        # 方案一
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
        #                                                 'scrollable(true).instance(0)).'
        #                                                 'scrollIntoView(new UiSelector().text("添加成员").'
        #                                                 'instance(0));').click()
        # 方案二
        Add_locator = (MobileBy.XPATH, "//*[@text='添加成员']")
        swipe_up_search_element(self.driver, Add_locator)

        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='必填']").send_keys(username)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手机号']").send_keys(mobilephone)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()

