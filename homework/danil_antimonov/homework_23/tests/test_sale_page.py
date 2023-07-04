from pages.locators import sale_page_locators as loc
from pages.sale_page import CheckSalePage
import allure


@allure.feature('SalePage')
def test_page_title(driver):
    creation_page = CheckSalePage(driver)
    creation_page.open()
    assert creation_page.find(loc.title_loc).text == 'Sale'
