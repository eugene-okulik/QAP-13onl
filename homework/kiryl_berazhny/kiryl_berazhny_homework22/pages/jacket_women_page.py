from pages.base_page import BasePage
from pages.locators import jackets_women_locators as JWL
from selenium.webdriver.common.action_chains import ActionChains


class JacketWomenPage(BasePage):
    page_url = 'women/tops-women/jackets-women.html'

    def click_sale(self):
        self.find(JWL.button_sale).click()

    def add_to_compare(self):
        ActionChains(self.driver).\
            move_to_element(self.finds(JWL.all_products)[0]).\
            move_to_element(self.finds(JWL.add_to_compare)[0]).\
            click().\
            perform()
