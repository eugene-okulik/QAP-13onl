from pages.base_page import BasePage
from pages.locators import sale_page_locators as SPL
from selenium.webdriver.common.keys import Keys


class SalePage(BasePage):
    page_url = 'sale.html'

    def subscribe_news(self, email):
        self.find(SPL.news_letter).send_keys(email + Keys.ENTER)

    @property
    def check_items(self):
        return self.find(SPL.check_products)

    @property
    def check_messages(self):
        return self.find(SPL.check_subscribe).text

    def click_jackets_women(self):
        self.find(SPL.jackets_women).click()

    @property
    def compare_items(self):
        return len(self.finds(SPL.compare_products))

    def clear_compare(self):
        self.find_message_compare(SPL.compare_clear).click()

    def accept_clear(self):
        self.find_window_alert(SPL.accept_clear).click()
