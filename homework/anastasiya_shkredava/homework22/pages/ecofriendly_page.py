from pages.base_page import BasePage
from pages.locators import ecofirendly_page_locators as locs
from selenium.webdriver.support.select import Select


class EcoFriendlyPage(BasePage):
    page_url = 'collections/eco-friendly.html'

    @property
    def title(self):
        return self.find(locs.title_loc)

    def wait_page_loaded(self):
        return self.wait_until_visibility(locs.wait_loc)

    @property
    def find_all_items(self):
        return self.find_all(locs.items_loc)

    def sort_by_name(self):
        return Select(self.find(locs.sort_button_loc)).select_by_value("name")

    def sort_ascending_order(self):
        return self.find(locs.ascending_sort_loc).click()
