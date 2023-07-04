from pages.sale_page import SalePage


def test_sale_text(driver):
    sale_page = SalePage(driver)
    sale_page.open()
    assert sale_page.sale_text.text == 'Sale'


def test_compare_products(driver):
    sale_page = SalePage(driver)
    sale_page.open()
    assert sale_page.compare_products.is_displayed()


def test_women_deals_button(driver):
    sale_page = SalePage(driver)
    sale_page.open()
    assert sale_page.women_deals_button.is_displayed()
