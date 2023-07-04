from pages.base_page import BasePage
from pages.locators import eco_friendly_locators as loc
from selenium.webdriver.support.select import Select


class EcoFriendlyPage(BasePage):
    page_url = '/collections/eco-friendly.html'

    @property
    def correct_title(self):
        return self.find(loc.title_loc)

    @property
    def click_mode_list_button(self):
        return self.find(loc.mode_list_button)

    @property
    def find_names(self):
        return self.find_all(loc.names_loc)

    def sorted_prods(self):
        return Select(self.find(loc.sort_button)).select_by_value('name')

    def wait_loading(self):
        return self.wait_until_visibility(loc.wait_loc)
