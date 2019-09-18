import os
import sys
import subprocess
from dingdingTest import SendMsg


def get_process_id(name, send_text):
    child = subprocess.Popen(["pgrep", "-f", name], stdout=subprocess.PIPE, shell=False)
    response = child.communicate()[0]
    if not response:
        SendMsg.msg(send_text)
    else:
        print(response)


if __name__ == '__main__':
    get_process_id("python socialbanklog.py", "python socialbanklog.py未运行")
