from pages.create_page import CreatePage


def test_account_create_email_failed_by_email(driver):
    create_page = CreatePage(driver)
    create_page.open()
    create_page.enter_name('Vladislav')
    create_page.enter_surname('Zavistovich')
    create_page.enter_email('vladzevarcom')
    create_page.enter_password('12345678Aa!')
    create_page.enter_password_confirmation('12345678Aa!')
    create_page.click_create_button()
    driver.implicitly_wait(3)
    assert create_page.email_message_error.is_displayed()


def test_account_create_email_failed_by_password(driver):
    create_page = CreatePage(driver)
    create_page.open()
    create_page.enter_name('Vladislav')
    create_page.enter_surname('Zavistovich')
    create_page.enter_email('vladzevar@gmail.com')
    create_page.enter_password('12345678')
    create_page.enter_password_confirmation('12345678')
    create_page.click_create_button()
    driver.implicitly_wait(3)
    assert create_page.password_message_error.is_displayed()


def test_account_create_lastname_requiared(driver):
    create_page = CreatePage(driver)
    create_page.open()
    create_page.enter_name('Vladislav')
    create_page.enter_email('vladzevar@gmail.com')
    create_page.enter_password('12345678')
    create_page.enter_password_confirmation('12345678')
    create_page.click_create_button()
    driver.implicitly_wait(3)
    assert create_page.surname_message_error.is_displayed()
