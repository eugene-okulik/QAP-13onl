from pages.base_page import BasePage
from pages.locators import eco_friendli_locators as loc


class EcoFriendlyPage(BasePage):
    page_url = '/collections/eco-friendly.html'

    @property
    def correct_title(self):
        return self.find(loc.title_loc)

    @property
    def sorter_button(self):
        return self.find(loc.button_sorter_loc)

    @property
    def mode_list_button(self):
        return self.find(loc.list_button_loc)
