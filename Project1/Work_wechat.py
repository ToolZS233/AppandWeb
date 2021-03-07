from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Options
import json


class TestTmp():
    def test_login(self):
        driver_arg = Options()
        driver_arg.debugger_address = "localhost:9333"
        driver = webdriver.Chrome(options=driver_arg)
        driver.find_element_by_id("menu_contacts").click()
        sleep(5)
        cookies = driver.get_cookies()
        print('cookies', cookies)
        with open("tmp.txt", 'w', encoding="utf-8") as f:
            json.dump(cookies, f)

    def test_cookie(self):
        driver = webdriver.Chrome()
        sleep(3)
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        with open("tmp.txt", 'r', encoding="utf-8") as f:
            cookies = json.load(f)
        for i in cookies:
            driver.add_cookie(i)
        driver.refresh()
        sleep(3)
