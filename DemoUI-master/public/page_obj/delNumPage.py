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

testData = getyaml(setting.TEST_Element_YAML + '/' + 'delNum.yaml')


class DelNum(Page):
    """
    用户登录页面
    """
    url = '/'
    # 定位器，通过元素属性定位元素对象





    # 签名统计
    choose_add_page_qmtj = (By.XPATH, testData.get_elementinfo(0))
    # 新增接入码
    choose_add_page_xzjrm = (By.ID, testData.get_elementinfo(1))

    def choose_add_page(self):
        """
        选择签名统计-新增接入码
        :return:
        """
        above = self.find_element(*self.choose_add_page_qmtj)
        # 悬浮签名统计
        ActionChains(self.driver).move_to_element(above).perform()
        sleep(1)
        # 点击新增接入码
        self.find_element(*self.choose_add_page_xzjrm).click()
        # 切换表单
        query_frame = self.find_element(By.CSS_SELECTOR, 'iframe[id="neiqiankuangjia"]')
        self.switch_frame(query_frame)
    # 输入删除号码
    input_del_num = (By.ID, testData.get_elementinfo(2))
    # 输入公众号
    input_pubid = (By.XPATH, testData.get_elementinfo(3))
    # 查詢按鈕
    query_pubid = (By.XPATH, testData.get_elementinfo(4))
    # 选择查询结果
    choose_pubid = (By.XPATH, testData.get_elementinfo(5))

    def query_pid(self, pubid, phone):
        """
        搜索公众号
        :param pubid:公众号
        :return:
        """
        # 输入下线号码
        self.find_element(*self.input_del_num).send_keys(phone)
        # 清空输入框
        self.find_element(*self.input_pubid).clear()
        # 输入公众号
        self.find_element(*self.input_pubid).send_keys(pubid)
        # 点击查询
        self.find_element(*self.query_pubid).click()
        sleep(1)
        # 选择查询结果
        self.find_element(*self.choose_pubid).click()
        sleep(1)

    # 全选
    choose_all = (By.XPATH, testData.get_elementinfo(6))
    # 删除
    choose_del = (By.XPATH, testData.get_elementinfo(7))

    def set_num_del(self):
        # 全选
        ActionChains(self.driver).click(self.find_element(*self.choose_all)).perform()
        # 删除
        ActionChains(self.driver).click(self.find_element(*self.choose_del)).perform()
        sleep(1)
        self.switch_alert().accept()
        sleep(5)

    def del_num(self, pubid, phone):
        """
        新增号码
        :param pubid: 公众号id
        :param phone: 接入码
        :return:
        """
        self.choose_add_page()
        self.query_pid(pubid, phone)
        self.set_num_del()
