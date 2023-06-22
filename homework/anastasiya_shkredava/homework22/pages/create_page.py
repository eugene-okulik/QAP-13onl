from pages.base_page import BasePage
from pages.locators import create_page_locators as locs


class AccountCreatePage(BasePage):
    page_url = 'customer/account/create/'

    def enter_first_name(self, firstname):
        self.find(locs.first_name_loc).send_keys(firstname)

    def enter_last_name(self, lastname):
        self.find(locs.last_name_loc).send_keys(lastname)

    def enter_email(self, email):
        self.find(locs.e_mail_loc).send_keys(email)

    def enter_password(self, password):
        self.find(locs.passw_loc).send_keys(password)

    def confirm_password(self, confirm_password):
        self.find(locs.confirm_passw_loc).send_keys(confirm_password)

    def click_create_an_account_button(self):
        self.find(locs.create_button_loc).click()

    @property
    def confirmation_error(self):
        return self.find(locs.confirmation_error_loc)

    @property
    def password_error(self):
        return self.find(locs.password_error_loc)

    @property
    def last_name_error(self):
        return self.find(locs.last_name_error)
