from pages.base_page import BasePage
from pages.locators import create_account_locators as loc


class CreateAccountPage(BasePage):
    page_url = 'customer/account/create/'

    @property
    def correct_title(self):
        return self.find(loc.title_loc)

    def enter_first_name(self, first_name):
        self.find(loc.first_name_loc).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.find(loc.last_name_loc).send_keys(last_name)

    def enter_email(self, email):
        self.find(loc.email_loc).send_keys(email)

    def enter_password(self, passw):
        self.find(loc.password_loc).send_keys(passw)

    def enter_confirm_password(self, confirm_passw):
        self.find(loc.confirm_password_loc).send_keys(confirm_passw)

    def click_button_to_create(self):
        return self.find(loc.button_loc).click()

    @property
    def email_error_message(self):
        return self.find(loc.email_error_mess)

    @property
    def short_password_error_message(self):
        return self.find(loc.short_passw_error_mess)

    def wait_loading(self):
        return self.wait_until_visibility(loc.wait_loc)
