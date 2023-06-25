from pages.eco_friendly_page import EcoFriendlyPage


def test_title_correct(driver):
    eco_friendly_page = EcoFriendlyPage(driver)
    eco_friendly_page.open()
    assert eco_friendly_page.correct_title.text == 'Eco Friendly'


def test_clickable_button(driver):
    eco_friendly_page = EcoFriendlyPage(driver)
    eco_friendly_page.open()
    driver.implicitly_wait(3)
    assert eco_friendly_page.click_mode_list_button.is_displayed()


def test_sorted_prods(driver):
    eco_friendly_page = EcoFriendlyPage(driver)
    eco_friendly_page.open()
    eco_friendly_page.wait_loading()
    eco_friendly_page.sorted_prods()
    eco_friendly_page.wait_loading()
    sorted_names = [prod.text for prod in eco_friendly_page.find_names]
    assert sorted(sorted_names) == sorted_names
