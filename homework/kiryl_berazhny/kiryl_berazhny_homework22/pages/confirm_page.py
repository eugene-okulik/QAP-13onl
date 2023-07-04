from pages.base_page import BasePage
from pages.locators import confirm_locators as CL
import allure


class ConfirmPage(BasePage):
    page_url = 'customer/account/'

    @allure.step('Click select button')
    def click_select_out(self):
        self.find_log_in(CL.button_select).click()

    @allure.step('Click button sign out')
    def click_sign_out(self):
        self.find_log_in(CL.sign_out).click()

    @property
    @allure.step('Result of verification of the confirmation text')
    def check_result(self):
        return self.find(CL.result).text
