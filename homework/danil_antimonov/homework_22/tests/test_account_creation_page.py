from pages.locators import account_creation_page_locators as loc
from pages.account_creation_page import CreateAccount


def test_create_account_button_is_present(driver):
    creation_page = CreateAccount(driver)
    creation_page.open()
    assert creation_page.find(loc.button_loc).is_displayed()


def test_all_required_fields_not_filled(driver):
    creation_page = CreateAccount(driver)
    creation_page.open()
    creation_page.click_button()
    assert creation_page.find(loc.firstname_error_loc).is_displayed()
    assert creation_page.find(loc.lastname_error_loc).is_displayed()
    assert creation_page.find(loc.email_error_loc).is_displayed()
    assert creation_page.find(loc.passw_confirm_error_loc).is_displayed()
    assert creation_page.find(loc.passw_error_loc).is_displayed()
