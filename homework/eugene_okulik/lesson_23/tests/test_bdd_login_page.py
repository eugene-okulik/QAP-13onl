from pytest_bdd import scenario, when, given, then
from pages.login_page import LoginPage


@scenario('login.feature', 'incorrect login alert')
def test_login_validation():
    pass


@scenario('login.feature', 'password validation displayed')
def test_passw_validation():
    pass


@given('I am on the login page')
def open_login_page(driver):
    LoginPage(driver).open()


@when('I enter non-existing user email into email field')
def enter_incorrect_email(driver):
    LoginPage(driver).enter_email('sksldkdhs19384@hjhf.ry')


@when('I enter correct email')
def enter_correct_email(driver):
    LoginPage(driver).enter_email('roni_cost@example.com')


@when('I enter correct password')
def enter_correct_password(driver):
    LoginPage(driver).enter_password('sdfsdfsdf')


@when('I click Sign In button')
def click_sign_in(driver):
    LoginPage(driver).click_sign_in_button()


@then('I see alert message')
def check_alert_message(driver):
    assert LoginPage(driver).error_message.is_displayed()


@then('I see password validation')
def check_passw_validation(driver):
    assert LoginPage(driver).pass_validation.is_displayed()
