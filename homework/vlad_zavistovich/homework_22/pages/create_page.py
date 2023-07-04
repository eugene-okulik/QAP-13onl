from pages.base_page import BasePage
from pages.locators import create_page_locators as loc


class CreatePage(BasePage):
    page_url = '/customer/account/create/'

    def enter_name(self, name):
        first_name = self.find(loc.name_loc)
        first_name.send_keys(name)

    def enter_surname(self, surname):
        second_name = self.find(loc.surname_loc)
        second_name.send_keys(surname)

    def enter_email(self, email):
        user_email = self.find(loc.email_loc)
        user_email.send_keys(email)

    def enter_password(self, passw):
        password = self.find(loc.password_loc)
        password.send_keys(passw)

    def enter_password_confirmation(self, passw_2):
        password_confirmation = self.find(loc.password_2_loc)
        password_confirmation.send_keys(passw_2)

    def click_create_button(self):
        self.find(loc.button_loc).click()

    @property
    def email_message_error(self):
        return self.find(loc.email_message_error_loc)

    @property
    def password_message_error(self):
        return self.find(loc.password_message_error_loc)

    @property
    def surname_message_error(self):
        return self.find(loc.surname_message_error_loc)
