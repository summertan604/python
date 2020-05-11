import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest, ddt, yaml
from config import setting
from public.models import myunit, screenshot
from public.page_obj.loginHubuPage import login
from public.models.log import Log

try:
    f =open(setting.TEST_DATA_YAML + '/' + 'loginHubu_data.yaml', encoding='utf-8')
    testData = yaml.load(f)
except FileNotFoundError as file:
    log = Log()
    log.error("文件不存在：{0}".format(file))


@ddt.ddt
class LoginTest(myunit.MyTest):
    """戶部登录测试"""
    def user_login_verify(self, phone, password):
        """
        用户登录
        :param phone: 手机号
        :param password: 密码
        :return:
        """
        login(self.driver).user_login(phone, password)

    def exit_login_check(self):
        """
        退出登录
        :return:
        """
        login(self.driver).login_exit()

    @ddt.data(*testData)
    def test_login(self, datayaml):
        """
        登录测试
        :param datayaml: 加载login_data登录测试数据
        :return:
        """
        log = Log()
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(datayaml['id'], datayaml['detail']))
        # 调用登录方法
        self.user_login_verify(datayaml['data']['phone'],datayaml['data']['password'])
        po = login(self.driver)
        log.info("检查点-> {0}".format(po.user_login_success_hint()))
        self.assertEqual(po.user_login_success_hint(), datayaml['check'][0], "成功登录，返回实际结果是->: {0}".format(po.user_login_success_hint()))
        log.info("成功登录，返回实际结果是->: {0}".format(po.user_login_success_hint()))
        screenshot.insert_img(self.driver, datayaml['screenshot'] + '.jpg')


if __name__ == '__main__':
    unittest.main()