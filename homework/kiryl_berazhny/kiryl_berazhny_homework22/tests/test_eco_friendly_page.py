from pages.eco_friendly_page import EcoFriendlyPage as EFP
from pages.search_result_page import SearchResult as SR


def test_strong_password(driver):  # максимальное количество товаров на странице при отображении сеткой
    ef_page = EFP(driver)
    ef_page.open_page()
    assert ef_page.quantity_products == 12


def test_sort_price_list(driver):  # проверка сортировки по цене в порядке убывания при отображении списком
    ef_page = EFP(driver)
    ef_page.open_page()
    ef_page.click_button_list()
    ef_page.click_sort_select()
    ef_page.click_sort_price()
    ef_page.click_sort_arrow()
    after_sort = ef_page.list_sort_price
    correct_sort = ef_page.correct_sort_list(after_sort)
    assert after_sort == correct_sort


def test_search_blue(driver):  # проверяем поиск, дает ли он нужный результат
    ef_page = EFP(driver)
    ef_page.open_page()
    ef_page.click_search('Blue')
    search_page = SR(driver)
    quantity = search_page.quantity_blue
    assert quantity == 12
