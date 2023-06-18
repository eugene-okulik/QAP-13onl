from pages.base_page import BasePage
from pages.locators import Eco_Friendly_locators as EFL
from selenium.webdriver.common.keys import Keys


class EcoFriendlyPage(BasePage):
    page_url = 'collections/eco-friendly.html'

    def click_button_list(self):
        self.find(EFL.list_button).click()

    def click_button_grid(self):
        self.find(EFL.grid_button).click()

    def click_sort_arrow(self):
        self.find(EFL.sort_arrow).click()

    def click_sort_select(self):
        self.find(EFL.sort_select).click()

    def click_sort_price(self):
        self.find(EFL.sort_price).click()

    @property
    def quantity_products(self):
        return len(self.finds(EFL.quantity))

    @property
    def list_sort_price(self):
        return list(map(lambda el: el.text, self.finds(EFL.quantity)))

    def correct_sort_list(self, sort_list: list):
        correct_list = sort_list.copy()
        correct_list.sort()
        return correct_list[::-1]

    def click_search(self, text: str):
        self.find(EFL.search).send_keys(text + Keys.ENTER)
