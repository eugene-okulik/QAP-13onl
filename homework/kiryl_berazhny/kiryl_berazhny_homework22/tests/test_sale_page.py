from pages.sale_page import SalePage
from pages.jacket_women_page import JacketWomenPage
import random


def test_subscribe(driver):  # проверяем есть ли уведомление о подписке на новости
    sale = SalePage(driver)
    sale.open_page()
    sale.scroll()
    sale.subscribe_news(f'q@{str(random.randint(1, 99999))}.com')
    assert sale.check_messages == 'Thank you for your subscription.'


def test_compare_check(driver):  # добавился ли товар во вкладку сравнения
    sale = SalePage(driver)
    sale.open_page()
    sale.click_jackets_women()
    jw_page = JacketWomenPage(driver)
    jw_page.add_to_compare()
    sale.open_page()
    assert sale.compare_items == 1


def test_clear_compare(driver):  # очистился ли список для сравнения товаров
    sale = SalePage(driver)
    sale.open_page()
    sale.click_jackets_women()
    jw_page = JacketWomenPage(driver)
    jw_page.add_to_compare()
    sale.open_page()
    sale.clear_compare()
    sale.accept_clear()
    assert sale.check_messages == 'You cleared the comparison list.'
