import random
from pages.base_page import BasePage
from pages.locators import jackets_women_locators as JWL
from selenium.webdriver.common.action_chains import ActionChains


class JacketWomenPage(BasePage):
    page_url = 'women/tops-women/jackets-women.html'

    def click_sale(self):
        self.find(JWL.button_sale).click()

    def add_to_compare(self):
        n = random.randint(0, 12)  # для выбора товара - всего 12 позиций на странице
        ActionChains(self.driver).\
            move_to_element(self.finds(JWL.all_products)[n]).\
            move_to_element(self.finds(JWL.add_to_compare)[n]).\
            click().\
            perform()
