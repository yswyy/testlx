import allure
from selenium import webdriver


class Test001:

    def setup_class(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://www.taobao.com')

    @allure.step('第二步')
    def abc(self):
        print('1111')

    @allure.step('第一步')
    def test001(self):
        self.abc()
        allure.attach(self.driver.get_screenshot_as_png(), "截图—淘宝", allure.attachment_type.PNG)
        print('\n----test01')
        print('\n你过来啊！')
