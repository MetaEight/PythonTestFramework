from .BasePage import BasePage
from locators.locators import LoginPageLocators as Locators
from test_data import users


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_login_page(self):
        self.go_to_page()

    def auth(self, name="user_1"):
        user = users.get_user(name)
        self.input_username(user['username'])
        self.input_password(user['password'])
        self.click_to_submit_login_button()

    def input_username(self, username):
        username_input_field = self.find_element(Locators.USERNAME_FORM)
        username_input_field.send_keys(username)

    def input_password(self, password):
        password_input_field = self.find_element(Locators.PASSWORD_FORM)
        password_input_field.send_keys(password)

    def click_to_submit_login_button(self):
        button = self.find_element(Locators.SUBMIT_LOGIN_BUTTON)
        button.click()

    def check_auth_is_correct(self):
        self.page_has_loaded()
        login_logo = self.find_elements(Locators.LOGIN_LOGO)
        if login_logo:
            error_block = self.find_elements(Locators.LOGIN_ERROR_BLOCK)
            if error_block:
                error_msg = error_block[0].text
                assert error_msg is None, f"Authorization failed, error message: {error_msg}"
            else:
                raise AssertionError("Authorization failed")
