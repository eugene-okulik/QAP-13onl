import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime


@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture(scope='session')
def db_connection():
    print('Opening connection')
    db = ...
    yield db
    print('Closing connection')


@pytest.fixture()
def say():
    print('before')
    yield None
    print('after')


@pytest.mark.regression
def test_dropdown(driver):
    print('in test')
    driver.get('https://www.google.com/')
    search = driver.find_element(By.NAME, 'q')
    assert search.is_displayed()


@pytest.mark.skipif(datetime.now().weekday() == 1, reason='Not working on tuesdays')
@pytest.mark.smoke
def test_cookies_test(driver):
    print('in test')
    driver.get('https://www.google.com/')
    button = driver.find_element(By.NAME, 'btnI')
    assert button.is_displayed()


@pytest.mark.smoke
def test_one(say, db_connection):
    summ = 1 + 2
    assert summ == 3


@pytest.mark.parametrize(
    'numb',
    [0, 1, 2]
)
# @pytest.mark.skip('Bug #345')
def test_two(numb):
    summ = numb + 3
    assert summ == 4
