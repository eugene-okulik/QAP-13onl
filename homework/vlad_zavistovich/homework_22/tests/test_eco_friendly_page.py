from pages.eco_friendly_page import EcoFriendlyPage


def test_title_correct(driver):
    eco_friendly_page = EcoFriendlyPage(driver)
    eco_friendly_page.open()
    assert eco_friendly_page.correct_title.text == 'Eco Friendly'


def test_sorter_button_displayed(driver):
    eco_friendly_page = EcoFriendlyPage(driver)
    eco_friendly_page.open()
    assert eco_friendly_page.sorter_button.is_displayed()


def test_mode_list_button(driver):
    eco_friendly_page = EcoFriendlyPage(driver)
    eco_friendly_page.open()
    assert eco_friendly_page.mode_list_button.is_displayed()
