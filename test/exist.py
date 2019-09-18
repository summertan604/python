# -*- coding:utf-8 -*-
from dingdingTest import SendMsg
import win32com.client
import time


def check_exist(process_name, send_text):
    wmi = win32com.client.GetObject('winmgmts:')
    process_code_cov = wmi.ExecQuery("select * from Win32_Process where Name='%s'" % process_name)
    if len(process_code_cov) > 0:
        print('%s is exists' % process_name)
    else:
        print('%s is not exists' % process_name)
        SendMsg.msg(send_text)


if __name__ == '__main__':
    while True:
        check_exist('QQ.exe', '您的QQ已退出')
        check_exist('chrome.exe', '您的chrome已退出')
        time.sleep(5)
