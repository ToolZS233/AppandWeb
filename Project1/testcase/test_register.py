from time import sleep

from Project1.login_page.main_page import MainPage


class TestRegister:
    def test_register(self):
        main = MainPage()
        main.goto_register().register()
        sleep(5)

    def test_login_register(self):
        main = MainPage()
        main.goto_login().goto_register()
        sleep(5)
