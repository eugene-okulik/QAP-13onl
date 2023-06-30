from pages.locators import collections_page_locators as loc
from pages.collections_page import Collections
import allure

@allure.feature('Collections')
def test_check_page_title(driver):
    page_title = Collections(driver)
    page_title.open()
    assert page_title.find(loc.page_title_loc).is_displayed()
