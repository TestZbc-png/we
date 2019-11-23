import unittest
import time
from time import sleep
from parameterized import parameterized
from selenium import webdriver


def add(a, b):
    """加法函数"""
    return a + b


def data_jason():
    return [(0, 1, 1), (1, 1, 1)]


class Unitest01(unittest.TestCase):

    # def setUp(self) -> None:
    #     self.driver = webdriver.Chrome()
    #     self.driver.get('http://localhost/Home/user/login.html')
    #     self.driver.implicitly_wait(6)
    #     self.driver.maximize_window()
    #
    # def tearDown(self) -> None:
    #     sleep(2)
    #     self.driver.quit()

    # unittest.skip('该版本已作废，跳过执行该模块')
    # def test_lgn(self):
    #     print('12313213')

    # def test_login01(self):
    #     self.driver.find_element_by_css_selector('[id="username"]').send_keys('15810217308')
    #     self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('123456')
    #     self.driver.find_element_by_id('verify_code').send_keys()
    #     self.driver.find_element_by_link_text('登    录').click()
    #     tag_name = self.driver.find_element_by_css_selector('[class="layui-layer-content layui-layer-padding"]').text
    #     self.driver.find_element_by_link_text('确定').click()
    #     try:
    #         self.assertIn('验证码不能为空!', tag_name)
    #     except Exception as e:
    #         print('没有提示框')
            # time_new = time.strftime('%Y%m%d%H%M%S')
            # self.driver.get_screenshot_as_file('./info_{}.png'.format(time_new))
            # self.driver.refresh()

    @parameterized.expand(data_jason())
    def test_login02(self, x, y, z):
        result = add(x, y)
        self.assertEqual(z, result)
