import json
from time import sleep

import pytest
from selenium import webdriver

class TestLogin():

    def setup_method(self, method):
        # 和浏览器打开的调试端口进行通信
        # 命令行启动 chrome -remote-debugging-port=9222
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_arg)

    def teardown_method(self, method):
        self.driver.quit()

    def test_tmp(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        self.driver.find_element_by_id("menu_contacts").click()
        sleep(3)

    def test_login_with_cookie(self):
        '''
        利用cookie进行登录
        :return:
        '''

        # cookies = self.driver.get_cookies()
        # # print(cookies)
        # with open("tmp2.txt", "w", encoding="utf-8") as f:
        #     # 序列化
        #     # f.write(json.dumps(cookies)) 或者 下面的写法
        #     json.dump(cookies, f)

        # # 读取 cookie
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        with open("tmp2.txt", "r", encoding="utf-8") as f:
            # 反序列化
            # raw_cookie = f.read()  或者 下面的写法
            # cookies = json.loads(raw_cookie) 或者 下面的写法
            cookies = json.load(f)
        for i in cookies:
            self.driver.add_cookie(i)
        self.driver.refresh()
        sleep(6)






