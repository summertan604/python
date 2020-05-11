#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'YinJia'

import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import setting
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from public.page_obj.base import Page
from time import sleep
from public.models.GetYaml import getyaml

testData = getyaml(setting.TEST_Element_YAML + '/' + 'loginHubu.yaml')

class login(Page):
    """
    用户登录页面
    """
    url = '/'
    # 定位器，通过元素属性定位元素对象
    # 账号输入框
    login_phone_loc = (By.NAME, testData.get_elementinfo(0))
    # 密码输入框
    login_password_loc = (By.NAME, testData.get_elementinfo(1))
    # 单击登录
    login_user_loc = (By.ID, testData.get_elementinfo(2))
    # 检查登录页
    login_url = testData.get_CheckElementinfo(0)

    def login_phone(self,phone):
        """
        登录手机号
        :param username:
        :return:
        """
        self.find_element(*self.login_phone_loc).send_keys(phone)

    def login_password(self,password):
        """
        登录密码
        :param password:
        :return:
        """
        self.find_element(*self.login_password_loc).send_keys(password)


    def login_button(self):
        """
        登录按钮
        :return:
        """
        self.find_element(*self.login_user_loc).click()

    def user_login(self,phone,password):
        """
        登录入口
        :param username: 用户名
        :param password: 密码
        :return:
        """
        self.open()
        if self.on_page() != self.login_url:
            self.login_phone(phone)
            self.login_password(password)
            self.login_button()
            sleep(1)

    # 登录成功用户名
    def user_login_success_hint(self):
        return self.on_page()
