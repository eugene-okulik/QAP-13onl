from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import allure


@pytest.fixture()
def driver():
    c_driver = webdriver.Chrome()
    c_driver.implicitly_wait(7)
    return c_driver


@allure.feature('Online shopping')
@allure.story('Positive case')
def test_1(driver):
    with allure.step('Open home page'):
        driver.get('https://www.demoblaze.com/index.html')
    with allure.step('Open the product in the new page'):
        ActionChains(driver). \
            key_down(Keys.COMMAND). \
            click(driver.find_elements(By.CLASS_NAME, 'card-title')[0]). \
            key_up(Keys.COMMAND). \
            perform()
    product = driver.find_elements(By.CLASS_NAME, 'card-title')[0].text
    with allure.step('Switch to second page'):
        driver.switch_to.window(driver.window_handles[1])
    with allure.step('Add the selected product to the shopping cart'):
        driver.find_element(By.XPATH, '//div//a[@onclick="addToCart(1)"]').click()
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    with allure.step('Alert message accepting'):
        Alert(driver).accept()
        driver.close()
    with allure.step('Switch to the first page'):
        driver.switch_to.window(driver.window_handles[0])
    with allure.step('Opening the cart'):
        driver.find_element(By.ID, 'cartur').click()
    with allure.step('Check if the product in our cart'):
        assert product == driver.find_element(By.XPATH, '//*[@id="tbodyid"]/tr/td[2]').text


@pytest.fixture(scope='session')
def s_session():
    print('Test start')
    yield ...
    print('Testing is finished')


@pytest.fixture(scope='function')
def s_test():
    print('Before all')
    yield ...
    print('After all')


@allure.feature('Summarize')
@allure.story('Positive case')
@pytest.mark.simple
def test_plus(s_session, s_test):
    result = 1 + 1
    assert result == 2


@allure.feature('Subtraction')
@allure.story('Positive case')
@pytest.mark.simple
def test_minus(s_session, s_test):
    result = 2 - 1
    assert result == 1


@allure.feature('Multiplication')
@allure.story('Negative case')
@pytest.mark.hard
def test_mult(s_session, s_test):
    result = 2 * 2
    assert result == 5


@pytest.mark.parametrize(
    'numb',
    [2, 4, 22]
)
@allure.feature('Summarize with 3 options')
@allure.story('Positive/Negative cases')
@pytest.mark.hard
def test_summ_par(s_session, s_test, numb):
    result = 2 + numb
    assert result == 4


@allure.feature('Division')
@allure.story('Positive case')
@pytest.mark.hard
def test_division(s_session, s_test):
    result = 5 / 1
    assert result == 5


@allure.feature('Lower case text')
@allure.story('Negative case')
@pytest.mark.skip('Bug #123')
@pytest.mark.hard
def test_text(s_session, s_test):
    text_1 = 'AAAAAAA'
    assert text_1.lower() == text_1


@allure.feature('Lower case text')
@allure.story('Positive case')
@pytest.mark.simple
def test_text_2(s_session, s_test):
    text_2 = 'bbbbbbb'
    assert text_2.lower() == text_2


@allure.feature('Number of letters')
@allure.story('Positive case')
@pytest.mark.simple
def test_text_3(s_session, s_test):
    name_country = 'Argentina'
    assert len(name_country) == 9


@allure.feature('True test')
@allure.story('Negative case')
@pytest.mark.hard
def test_true(s_session, s_test):
    number_r = True
    assert number_r is False


@allure.feature('word summation')
@allure.story('Positive case')
@pytest.mark.hard
def test_summ_words(s_session, s_test):
    first_part = 'United '
    second_part = 'Kingdom'
    assert first_part + second_part == 'United Kingdom'
