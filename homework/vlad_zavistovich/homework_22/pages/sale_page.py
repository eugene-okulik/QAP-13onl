from pages.base_page import BasePage
from pages.locators import sale_page_locators as loc


class SalePage(BasePage):
    page_url = '/sale.html'

    @property
    def sale_text(self):
        return self.find(loc.title_loc)

    @property
    def compare_products(self):
        return self.find(loc.button_loc)

    @property
    def women_deals_button(self):
        return self.find(loc.compare_products_loc)
