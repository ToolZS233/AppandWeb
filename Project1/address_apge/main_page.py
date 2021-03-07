from selenium import webdriver

from Project1.address_apge.address_page import AddressPage1


class Main_Page1:
    def __init__(self):
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_arg)

    def goto_address(self):
        self.driver.find_element_by_id("menu_contacts").click()
        return AddressPage1(self.driver)
