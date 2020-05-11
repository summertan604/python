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

testData = getyaml(setting.TEST_Element_YAML + '/' + 'newNum.yaml')


class NewNum(Page):
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
        # 输入公众号

    input_pubid = (By.XPATH, testData.get_elementinfo(2))
    # 查詢按鈕
    query_pubid = (By.XPATH, testData.get_elementinfo(3))
    # 选择查询结果
    choose_pubid = (By.XPATH, testData.get_elementinfo(4))

    def query_pid(self, pubid):
        """
        搜索公众号
        :param pubid:公众号
        :return:
        """
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

    # 点击新增接入码
    click_add_num = (By.XPATH, testData.get_elementinfo(5))
    # 输入接入码
    input_num = (By.ID, testData.get_elementinfo(6))
    # 单击区域框
    click_area = (By.ID, testData.get_elementinfo(7))
    # 选择上线方式
    choose_type = (By.ID, testData.get_elementinfo(8))
    # 下一步
    next_btn = (By.ID, testData.get_elementinfo(9))
    # 确定
    confirm = (By.XPATH, testData.get_elementinfo(10))

    def add_num(self, phone, areas, type):
        """
        新增号码
        :param phone: 号码
        :param area: 区域
        :param type: 上线方式
        :return:
        """
        #点击新增号码按钮
        self.find_element(*self.click_add_num).click()
        # 输入号码
        self.find_element(*self.input_num).send_keys(phone)
        # 点击区域选择框
        ActionChains(self.driver).click(self.find_element(*self.click_area)).perform()
        # 点击选择按钮.
        for area in areas.split(';'):
            self.find_element(By.XPATH, "//a[@title='" + area + "']").click()
        # 选择上线方式
        if type == 'N':
            select_ele = self.find_element(*self.choose_type)
            Select(select_ele).select_by_value('2')
        # 取消区域选择选中
        self.find_element(*self.input_num).click()
        sleep(1)
        # 点击下一步
        ActionChains(self.driver).click(self.find_element(*self.next_btn)).perform()
        sleep(1)
        # 接受弹出框
        alert_is_present = self.switch_alert()
        if alert_is_present:
            alert_is_present.accept()
        # 点击确定
        self.find_element(*self.confirm).click()
        sleep(1)
        # 接受弹出框
        alert_is_present = self.switch_alert()
        if alert_is_present:
            alert_is_present.accept()

    # 输入新增号码
    query_new_num = (By.ID, testData.get_elementinfo(11))
    # # 选择状态框
    # choose_state = (By.XPATH, testData.get_elementinfo(12))
    # # 选择未验证
    # choose_no_pass = (By.XPATH, testData.get_elementinfo(13))
    # 点击查找框
    click_query_button = (By.XPATH, testData.get_elementinfo(12))
    # 全选
    choose_all = (By.XPATH, testData.get_elementinfo(13))
    # 验证通过
    check_pass = (By.XPATH, testData.get_elementinfo(14))
    # # 选择已验证
    # choose_pass = (By.XPATH, testData.get_elementinfo(17))
    # 设为启用
    set_true = (By.XPATH, testData.get_elementinfo(15))

    def set_num_work(self, phone, pubid):
        # 输入新增号码
        self.find_element(*self.query_new_num).send_keys(phone)
        # 选择公众号
        self.query_pid(pubid)
        # 选择状态框
        # ActionChains(self.driver).click(self.find_element(*self.choose_state)).perform()
        # sleep(1)
        # 选择未验证
        # ActionChains(self.driver).click(self.find_element(*self.choose_no_pass)).perform()
        # 点击查找
        # self.find_element(*self.click_query_button).click()
        sleep(1)
        # 全选
        ActionChains(self.driver).click(self.find_element(*self.choose_all)).perform()
        # 验证通过
        ActionChains(self.driver).click(self.find_element(*self.check_pass)).perform()
        sleep(1)
        # 选择状态框
        # ActionChains(self.driver).click(self.find_element(*self.choose_state)).perform()
        # sleep(1)
        # 选择已验证
        # ActionChains(self.driver).click(self.find_element(*self.choose_pass)).perform()
        # 点击查找
        # self.find_element(*self.click_query_button).click()
        # 选择公众号
        self.query_pid(pubid)
        sleep(1)
        # 全选
        ActionChains(self.driver).click(self.find_element(*self.choose_all)).perform()
        # 设为启用
        ActionChains(self.driver).click(self.find_element(*self.set_true)).perform()
        sleep(2)

    def new_num(self, pubid, phone, area, type):
        """
        新增号码
        :param pubid: 公众号id
        :param phone: 接入码
        :param area: 地区
        :param type: 上线方式
        :return:
        """
        self.choose_add_page()
        self.query_pid(pubid)
        self.add_num(phone, area, type)
        self.set_num_work(phone,pubid)
