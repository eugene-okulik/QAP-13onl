from pages.base_page import BasePage
from pages.locators import confirm_locators as CL


class ConfirmPage(BasePage):
    page_url = 'customer/account/'

    def click_select_out(self):
        self.find_log_in(CL.button_select).click()

    def click_sign_out(self):
        self.find_log_in(CL.sign_out).click()

    @property
    def check_result(self):
        return self.find(CL.result).text
