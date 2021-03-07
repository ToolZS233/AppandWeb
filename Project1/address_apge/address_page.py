from time import sleep

from selenium.webdriver.support.wait import WebDriverWait


class AddressPage1:
    def __init__(self, driver):
        self.driver = driver

    def add_member(self):
        def waite_username(x):
            self.driver.find_elements_by_xpath("//*[@class='qui_btn ww_btn js_add_member']")[1].click()
            elem = self.driver.find_elements_by_xpath("//*[@id='username']")
            return len(elem) > 0

        WebDriverWait(self.driver, 10).until(waite_username)


        # 输入姓名
        self.driver.find_element_by_xpath("//*[@id='username']").send_keys('zs')
        # 输入账号
        self.driver.find_element_by_xpath("//*[@id='memberAdd_acctid']").send_keys('20210307')
        # 输入手机号
        self.driver.find_element_by_xpath("//*[@id='memberAdd_phone']").send_keys('17603224568')
        # 提交保存
        self.driver.find_element_by_xpath("//*[@class='qui_btn ww_btn js_btn_save']").click()
