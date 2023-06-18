from pages.create_page import AccountCreatePage


def test_confirm_password(driver):
    create_page = AccountCreatePage(driver)
    create_page.open()
    create_page.enter_first_name("Petya")
    create_page.enter_last_name("Petrov")
    create_page.enter_email("gwolf@yahoo.com")
    create_page.enter_password("123456aA!@")
    create_page.confirm_password("123456aA!#")
    create_page.click_create_an_account_button()
    assert create_page.confirmation_error.text == 'Please enter the same value again.'


def test_short_password(driver):
    create_page = AccountCreatePage(driver)
    create_page.open()
    create_page.enter_first_name("Petya")
    create_page.enter_last_name("Petrov")
    create_page.enter_email("gwolf@yahoo.com")
    create_page.enter_password("1234567")
    create_page.confirm_password("1234567")
    create_page.click_create_an_account_button()
    assert create_page.password_error.text == 'Minimum length of this field must be equal or greater than 8 symbols. ' \
                                              'Leading and trailing spaces will be ignored.'


def test_missing_required_field(driver):
    create_page = AccountCreatePage(driver)
    create_page.open()
    create_page.enter_first_name("Petya")
    create_page.enter_email("gwolf@yahoo.com")
    create_page.enter_password("123456aA!@")
    create_page.confirm_password("123456aA!@")
    create_page.click_create_an_account_button()
    assert create_page.last_name_error.text == 'This is a required field.'
