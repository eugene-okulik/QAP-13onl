from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.locators import login_page_locators as loc


class LoginPage(BasePage):
    page_url = '/customer/account/login'

    def enter_email(self, email):
        login = self.find(loc.login_loc)
        login.send_keys(email)

    def enter_password(self, password):
        passw = self.find(loc.passw_loc)
        passw.send_keys(password)

    def click_sign_in_button(self):
        self.find(loc.button_loc).click()

    @property
    def error_message(self):
        return self.find(loc.email_error)

    def login_as(self, username, password):
        self.find(loc.login_loc).send_keys(username)
        self.find(loc.passw_loc).send_keys(password)
        self.find(loc.button_loc).click()

    def click_logo(self):
        self.find(loc.logo).click()
        return HomePage(self.driver)
