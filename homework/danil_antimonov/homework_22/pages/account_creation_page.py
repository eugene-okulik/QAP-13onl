from pages.base_page import BasePage
from pages.locators import account_creation_page_locators as loc


class CreateAccount(BasePage):
    page_url = 'customer/account/create/'

    def click_button(self):
        self.find(loc.button_loc).click()
