from pages.login_page import LoginPage
from pages.home_page import HomePage
from time import sleep
import allure


# def test_login_failed(driver):
#     sleep(5)
#     driver.get('https://magento.softwaretestingboard.com/customer/account/login')
#     login = driver.find_element(By.ID, 'email')
#     passw = driver.find_element(By.ID, 'pass')
#     button = driver.find_element(By.ID, 'send2')
#     login.send_keys('sjddh@sdlfks')
#     passw.send_keys('dkfjhkdjfhg')
#     button.click()
#     driver.implicitly_wait(3)
#     error_message = driver.find_element(By.ID, 'email-error')
#     assert error_message.text == 'Please enter a valid email address (Ex: johndoe@domain.com).'

@allure.feature('Login')
@allure.story('negative cases')
def test_login_failed_new(driver):
    # sleep(5)
    with allure.step('Open login page'):
        login_page = LoginPage(driver)
        login_page.open()
    with allure.step('Enter email'):
        login_page.enter_email('sjddh@sdlfks')
    with allure.step('enter password'):
        login_page.enter_password('dkfjhkdjfhg')
    with allure.step('click sign in'):
        login_page.click_sign_in_button()
    with allure.step('Check message'):
        assert login_page.error_message.text == 'Please enter a valid email address (Ex: johndoe@domain.com).'


@allure.feature('Login')
@allure.story('negative cases')
def test_login_failed_new2(driver):
    sleep(5)
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login_as('sdfsdfsdf', 'sdfsdfsdf')
    assert login_page.error_message.text == 'Please enter a valid email address (Ex: johndoe@domain.com).'


@allure.feature('Login')
@allure.story('logo')
def test_logo_click(driver):
    sleep(5)
    login_page = LoginPage(driver)
    login_page.open()
    login_page.click_logo()
    home_page = HomePage(driver)
    assert home_page.action_button.is_displayed()


@allure.feature('Login')
@allure.story('logo')
def test_logo_click2(driver):
    sleep(5)
    login_page = LoginPage(driver)
    login_page.open()
    home_page = login_page.click_logo()
    assert home_page.action_button.is_displayed()
