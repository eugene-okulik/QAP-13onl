from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import allure
import pytest


@allure.feature('Text Input')
class TestTextInput:

    @pytest.fixture()
    def test_driver(self):
        chrome_driver = webdriver.Chrome()
        chrome_driver.maximize_window()
        with allure.step('open the page'):
            chrome_driver.get('https://www.qa-practice.com/elements/input/simple')
        return chrome_driver

    @allure.story('positive case')
    def test_input(self, test_driver):
        input_field = test_driver.find_element(By.CLASS_NAME, "textinput")
        with allure.step('enter the text'):
            input_field.send_keys('12')
        with allure.step('press Enter'):
            input_field.send_keys(Keys.ENTER)
        result_field = test_driver.find_element(By.CLASS_NAME, "result")
        with allure.step('get the result'):
            assert result_field.text == '12'

    @pytest.mark.parametrize(
        'text',
        ['1', '123456789' * 3]
    )
    @allure.story('negative cases')
    def test_length_limits(self, test_driver, text):
        input_field = test_driver.find_element(By.CLASS_NAME, "textinput")
        with allure.step('enter the text'):
            input_field.send_keys(text)
        with allure.step('press Enter'):
            input_field.send_keys(Keys.ENTER)
        result_field = test_driver.find_element(By.ID, "error_1_id_text_string")
        with allure.step('get the error'):
            assert result_field.is_displayed()


@allure.feature('Buttons')
class TestButtons:

    @pytest.fixture()
    def test_driver(self):
        chrome_driver = webdriver.Chrome()
        chrome_driver.maximize_window()
        return chrome_driver

    @allure.story('simple button')
    def test_simple_button(self, test_driver):
        with allure.step('open the page'):
            test_driver.get('https://www.qa-practice.com/elements/button/simple')
        with allure.step('click Submit button'):
            test_driver.find_element(By.ID, 'submit-id-submit').click()
        with allure.step('check that button is submitted'):
            assert test_driver.find_element(By.ID, 'result').is_displayed()

    @pytest.mark.parametrize(
        'value',
        ['disabled', 'enabled']
    )
    @allure.story('disabled button')
    def test_disabled_button(self, test_driver, value):
        with allure.step('open the page'):
            test_driver.get('https://www.qa-practice.com/elements/button/disabled')
        with allure.step(f'make button {value}'):
            select = test_driver.find_element(By.ID, 'id_select_state')
            Select(select).select_by_value(value)
        with allure.step('click Submit button'):
            test_driver.find_element(By.ID, 'submit-id-submit').click()
        with allure.step('check that button is submitted'):
            assert test_driver.find_element(By.ID, 'result').is_displayed()

    @pytest.mark.skip('Bug #111')
    def test_requirements(self, test_driver):
        test_driver.get('https://www.qa-practice.com/elements/button/disabled')
        test_driver.find_element(By.ID, 'req_header').click()
        assert test_driver.find_element(By.ID, 'req_text').is_displayed()
