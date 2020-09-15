import allure
from selenium import webdriver


class Test01:

    def setup_class(self):
        self.driver = webdriver.Chrome
        self.driver.get('http://www.taobao.com')

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step('第一步')
    def test01(self):
        print('\n你过来啊')
         allure.attach(self.driver.get_screenshot_as_png(), "淘宝截图", allure.attachment_type.PNG)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step('第二步')
    def test02(self):
        print('\n你再过来啊')
        assert False

    @allure.severity(allure.severity_level.NORMAL)
    @allure.step('第三步')
    def test03(self):   
        print('\n你别过来啊')

    @allure.severity(allure.severity_level.MINOR)
    @allure.step('第四步')
    def test04(self):
        print('\n你走开啊')

    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.step('第五步')
    def test04(self):
        print('\n你又来啊')
