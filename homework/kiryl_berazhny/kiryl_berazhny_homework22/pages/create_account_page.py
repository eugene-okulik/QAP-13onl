from pages.base_page import BasePage
from pages.locators import Create_Account_locators as CAL


class CreateAccountPage(BasePage):
    page_url = 'customer/account/create/'

    def enter_first_name(self, first_name):
        name = self.find(CAL.first_name)
        name.send_keys(first_name)

    def enter_second_name(self, sec_name):
        second_name = self.find(CAL.last_name)
        second_name.send_keys(sec_name)

    def enter_email(self, email):
        name_email = self.find(CAL.email_address)
        name_email.send_keys(email)

    def enter_pass_one(self, password):
        passw = self.find(CAL.password)
        passw.send_keys(password)

    def enter_pass_two(self, password):
        passw = self.find(CAL.password_confirmation)
        passw.send_keys(password)

    def click_submit(self):
        self.find(CAL.submit).click()

    @property
    def check_password(self):
        return self.find(CAL.check_pass)

    @property
    def error_text(self):
        return self.find(CAL.error_text)
