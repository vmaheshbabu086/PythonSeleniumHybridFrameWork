from datetime import datetime
import pytest
from selenium.webdriver.common.by import By

from PageObject.AccountPage import AccountPage
from PageObject.HomePage import HomePage
from PageObject.LoginPage import LoginPage
from tests.BaseTest import BaseTest
from utilities import ExcelUtils


class TestLogin(BaseTest):
    @pytest.mark.parametrize("email_address,password",ExcelUtils.get_cate_from_excel("ExcelFiles/tutorialsninja.xlsx","Sheet1"))
    def test_login_with_valid_credentials(self,email_address,password):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        login_page = home_page.select_login_option()
        login_page.enter_email_address(email_address)
        login_page.enter_password(password)
        account_page = login_page.click_on_login_button()
        assert account_page.display_status_of_your_account_information_option()

    def test_login_with_invalid_email_and_valid_password(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        login_page = home_page.select_login_option()
        login_page.enter_email_address(self.generate_email_with_time_stamp())
        login_page.enter_password("12345")
        login_page.click_on_login_button()
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__contains__(
            expected_warning_message)

    def test_login_with_valid_mail_and_invalid_password(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        login_page = home_page.select_login_option()
        login_page.enter_email_address("sidhartha028@gmail.com")
        login_page.enter_password("12345645")
        login_page.click_on_login_button()
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__contains__(
            expected_warning_message)

    def test_login_without_entering_credentials(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        login_page = home_page.select_login_option()
        login_page.enter_email_address("")
        login_page.enter_password("")
        login_page.click_on_login_button()
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__contains__(
            expected_warning_message)



