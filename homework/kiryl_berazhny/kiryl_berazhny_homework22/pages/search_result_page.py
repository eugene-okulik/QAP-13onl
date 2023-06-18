from pages.base_page import BasePage
from pages.locators import search_result_locators as SRL


class SearchResult(BasePage):
    page_url = 'catalogsearch/result/?q=Blue'

    @property
    def quantity_blue(self):
        return len(self.finds(SRL.color_blue))
