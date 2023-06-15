from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():

    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    return chrome_driver


def test_1(driver):

    driver.get('https://www.demoblaze.com/index.html')
    driver.implicitly_wait(3)
    ActionChains(driver). \
        key_down(Keys.COMMAND).\
        click(driver.find_elements(By.CLASS_NAME, 'card-title')[0]).\
        key_up(Keys.COMMAND).\
        perform()
    product = driver.find_elements(By.CLASS_NAME, 'card-title')[0].text
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.XPATH, '//div//a[@onclick="addToCart(1)"]').click()
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    Alert(driver).accept()
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.ID, 'cartur').click()
    buy_product = driver.find_element(By.XPATH, '//*[@id="tbodyid"]/tr/td[2]').text
    assert product == buy_product


def test_2(driver):

    driver.get('https://demoqa.com/menu#')
    ActionChains(driver).\
        move_to_element(driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/a')).\
        move_to_element(driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/ul/li[3]/a')).\
        move_to_element(driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/ul/li[3]/ul/li[2]/a')).perform()
    driver.save_screenshot('result.png')


def test_3(driver):

    driver.get('https://www.qa-practice.com/elements/alert/prompt')
    driver.find_element(By.CLASS_NAME, 'a-button').click()
    text = 'Ну привет, куда я попал?'
    Alert(driver).send_keys(text)
    Alert(driver).accept()
    assert text == driver.find_element(By.ID, 'result-text').text
