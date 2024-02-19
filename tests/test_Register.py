import time

import pytest

from selenium.webdriver.common.by import By
from PageObject.AccountSuccessPage import AccountSuccessPage
from PageObject.HomePage import HomePage
from PageObject.RegisterPage import RegisterPage
from datetime import datetime
from tests.BaseTest import BaseTest


class TestRegister(BaseTest):
    def test_register_with_mandatory_fields(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        register_page = home_page.select_register_option()
        register_page.enter_first_name("Sai")
        register_page.enter_last_name("Sidhartha")
        register_page.enter_email(self.generate_email_with_time_stamp())
        register_page.enter_telephone("9553754595")
        register_page.enter_password("12345")
        register_page.enter_password_confirm("12345")
        register_page.select_agree_checkbox_field()
        account_success_page = register_page.click_on_continue_button()
        expected_heading_text = "Your Account Has Been Created!"
        assert account_success_page.retrieve_account_creation_message().__eq__(expected_heading_text)

    def test_register_with_all_fields(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        register_page = home_page.select_register_option()
        register_page.enter_first_name("Sai")
        register_page.enter_last_name("Sidhartha")
        register_page.enter_email(self.generate_email_with_time_stamp())
        register_page.enter_telephone("9553754595")
        register_page.enter_password("12345")
        register_page.enter_password_confirm("12345")
        register_page.select_yes_radio_button()
        register_page.select_agree_checkbox_field()
        account_success_page = register_page.click_on_continue_button()
        expected_text = "Your Account Has Been Created!"
        assert account_success_page.retrieve_account_creation_message().__eq__(expected_text)

    def test_register_with_duplicate_email(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        register_page = home_page.select_register_option()
        register_page.enter_first_name("Sai")
        register_page.enter_last_name("Sidhartha")
        register_page.enter_email("sidhartha028@gmail.com")
        register_page.enter_telephone("9553754595")
        register_page.enter_password("12345")
        register_page.enter_password_confirm("12345")
        register_page.select_yes_radio_button()
        register_page.select_agree_checkbox_field()
        register_page.click_on_continue_button()
        expected_warning_message = "Warning: E-Mail Address is already registered!"
        assert register_page.retrieve_duplicate_email_warning().__contains__(
            expected_warning_message)

    # def test_register_without_entering_any_fields(self):
    #     home_page = HomePage(self.driver)
    #     home_page.click_on_my_account_drop_menu()
    #     register_page = home_page.select_register_option()
    #     register_page.enter_first_name("")
    #     register_page.enter_last_name("")
    #     register_page.enter_email("")
    #     register_page.enter_telephone("")
    #     register_page.enter_password("")
    #     register_page.enter_password_confirm("")
    #     register_page.select_yes_radio_button()
    #     register_page.select_agree_checkbox_field()
    #     register_page.click_on_continue_button()
    #
    #     expected_privacy_policy_warning_message = "Warning: You must agree to the Privacy Policy!"
    #     assert register_page.retrieve_privacy_policy_warning().__contains__(
    #         expected_privacy_policy_warning_message)
    #
    #     expected_first_name_warning_message = "First Name must be between 1 and 32 characters!"
    #     assert register_page.retrieve_first_name_warning().__eq__(
    #         expected_first_name_warning_message)
    #
    #     expected_last_name_warning_message = "Last Name must be between 1 and 32 characters!"
    #     assert register_page.retrieve_last_name_warning().__eq__(
    #         expected_last_name_warning_message)
    #
    #     expected_email_warning_message = "E-Mail Address does not appear to be valid!"
    #     assert register_page.retrieve_email_warning().__eq__(
    #         expected_email_warning_message)
    #
    #     expected_telephone_warning_message = "Telephone must be between 3 and 32 characters!"
    #     assert register_page.retrieve_telephone_warning().__eq__(
    #         expected_telephone_warning_message)
    #
    #     expected_password_password_warning_message = "Password must be between 4 and 20 characters!"
    #     assert register_page.retrieve_password_warning().__eq__(
    #         expected_password_password_warning_message)


