from pages.sale_page import SalePage


def test_title_correct(driver):
    sale_page = SalePage(driver)
    sale_page.open()
    assert sale_page.title_correct.text == 'Sale'


def test_clickable_button(driver):
    sale_page = SalePage(driver)
    sale_page.open()
    assert sale_page.clickable_button.is_displayed()


def test_logo_click(driver):
    sale_page = SalePage(driver)
    sale_page.open()
    assert sale_page.click_logo.is_displayed()
