from pages.base_page import BasePage
from pages.locators import sale_page_locators as loc


class SalePage(BasePage):
    page_url = '/sale.html'

    @property
    def title_correct(self):
        return self.find(loc.title_loc)

    @property
    def clickable_button(self):
        return self.find(loc.button_loc)

    @property
    def click_logo(self):
        return self.find(loc.logo_click_loc)
