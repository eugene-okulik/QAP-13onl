from pages.base_page import BasePage
from pages.locators import sale_page_locators as locs


class SalePage(BasePage):
    page_url = 'sale.html'

    def click_sale_link(self, sale):
        self.wait_until_visibility(locs.wait_loc)
        if sale == "women's deals":
            self.find(locs.main_sale_loc).click()
            self.wait_until_visibility(locs.wait_loc)
        elif sale == "men's deals":
            self.find(locs.men_sale_loc).click()
            self.wait_until_visibility(locs.wait_loc)
        elif sale == 'luma gear':
            self.find(locs.women_sale_loc).click()
            self.wait_until_visibility(locs.wait_loc)
