from pages.create_account_page import CreateAccountPage


def test_title_correct(driver):
    create_account_page = CreateAccountPage(driver)
    create_account_page.open()
    assert create_account_page.correct_title.text == 'Create New Customer Account'


def test_create_acc(driver):
    create_account_page = CreateAccountPage(driver)
    create_account_page.open()
    create_account_page.enter_first_name('sdfsdfsdf')
    create_account_page.enter_last_name('sdfsdfsdf')
    create_account_page.enter_email('ekjd@k')
    create_account_page.enter_password('qwertyui')
    create_account_page.enter_confirm_password('qwertyui')
    create_account_page.scroll(600)
    create_account_page.wait_loading()
    create_account_page.click_button_to_create()
    email_error_mess = 'Please enter a valid email address (Ex: johndoe@domain.com).'
    assert create_account_page.email_error_message.text == email_error_mess


def test_create_acc_short_passw(driver):
    create_account_page = CreateAccountPage(driver)
    create_account_page.open()
    create_account_page.enter_first_name('sdfsdfsdf')
    create_account_page.enter_last_name('sdfsdfsdf')
    create_account_page.enter_email('ekjd@k')
    create_account_page.enter_password('qwerty')
    create_account_page.enter_confirm_password('qwerty')
    create_account_page.scroll(600)
    create_account_page.wait_loading()
    create_account_page.click_button_to_create()
    short_passw_error_mess = ('Minimum length of this field must be equal or greater than 8 symbols. '
                              'Leading and trailing spaces will be ignored.')
    assert create_account_page.short_password_error_message.text == short_passw_error_mess
