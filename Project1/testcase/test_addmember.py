from Project1.address_apge.main_page import Main_Page1


class Test_addmember:

    def test_addmember(self):
        main = Main_Page1()
        main.goto_address().add_member()
