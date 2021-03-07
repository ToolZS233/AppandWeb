from selenium.webdriver.common.by import By

from Project1.login_page.register_page import RegisterPage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def goto_register(self):
        self.driver.find_element(By.XPATH, "//*[@class='login_registerBar_link']").click()
        RegisterPage(self.driver)