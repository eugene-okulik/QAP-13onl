from pages.sale_page import SalePage


def test_shop_womens_deals_link(driver):
    sale_page = SalePage(driver)
    sale_page.open()
    sale_page.click_sale_link("women's deals")
    assert driver.current_url == f'{sale_page.base_url}promotions/women-sale.html'


def test_shop_mens_deals_link(driver):
    sale_page = SalePage(driver)
    sale_page.open()
    sale_page.click_sale_link("men's deals")
    assert driver.current_url == f'{sale_page.base_url}promotions/men-sale.html'


def test_shop_luma_gear_link(driver):
    sale_page = SalePage(driver)
    sale_page.open()
    sale_page.click_sale_link("luma gear")
    assert driver.current_url == f'{sale_page.base_url}gear.html'
