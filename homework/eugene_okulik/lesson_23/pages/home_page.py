from pages.base_page import BasePage
# from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

action_button = ('css selector', '.action.more.button')


class HomePage(BasePage):
    page_url = '/'

    @property
    def action_button(self):
        return self.find(action_button)

    # def click_sign_in(self):
    #     return LoginPage(self.driver)
