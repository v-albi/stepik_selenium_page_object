from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "'Login' is not in presented URL"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        put_email = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        put_email.send_keys(email)
        put_password1 = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        put_password1.send_keys(password)
        put_password2 = self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD)
        put_password2.send_keys(password)
        register = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register.click()



