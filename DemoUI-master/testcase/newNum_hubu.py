import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest, ddt, yaml
from config import setting
from public.models import myunit, screenshot
from public.page_obj.newNumPage import NewNum
from public.page_obj.loginHubuPage import login
from public.models.log import Log

f_login = open(setting.TEST_DATA_YAML + '/' + 'loginHubu_data.yaml',encoding='utf-8')
LoginData = yaml.load(f_login)
ph = LoginData[0]['data']['phone']
pwd = LoginData[0]['data']['password']

try:
    f = open(setting.TEST_DATA_YAML + '/' + 'newNum_data.yaml', encoding='utf-8')
    testData = yaml.load(f)
except FileNotFoundError as file:
    log = Log()
    log.error("文件不存在：{0}".format(file))


@ddt.ddt
class NewNumTest(myunit.MyTest):
    """新增号码测试"""

    def user_login_verify(self, phone, password):
        """
        用户登录
        :param phone: 手机号
        :param password: 密码
        :return:
        """
        login(self.driver).user_login(phone, password)

    def add_num(self, pubid, phone, area, type):
        """
        新增号码
        :param pubid: 公众号id
        :param phone: 接入码
        :param area: 地区
        :param type: 上线方式
        :return:
        """
        NewNum(self.driver).new_num(pubid, phone, area, type)

    @ddt.data(*testData)
    def test_add_num(self, datayaml):
        """
        新增号码测试
        :param datayaml: 加载newNum_data测试数据
        :return:
        """
        log = Log()
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(datayaml['id'],datayaml['detail']))
        # 调用登录方法
        self.user_login_verify(ph, pwd)
        # 调用新增号码方法
        self.add_num(datayaml['data']['pubid'],
                     datayaml['data']['num'],
                     datayaml['data']['area'],
                     datayaml['data']['type'])


if __name__ == '__main__':
    unittest.main()
