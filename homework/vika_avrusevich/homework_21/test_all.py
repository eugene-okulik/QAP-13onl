from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture()
def driver():
    chr_driver = webdriver.Chrome()
    chr_driver.maximize_window()
    return chr_driver


def test_one(driver):
    driver.get('https://www.demoblaze.com/index.html')
    driver.implicitly_wait(10)
    # откройте товар в новой вкладке
    item = driver.find_elements(By.CLASS_NAME, 'card-title')
    item_to_add = item[0].text
    ActionChains(driver).key_down(Keys.CONTROL).click(item[0]).key_up(Keys.CONTROL).perform()
    # Перейдите на вкладку с товаром
    driver.switch_to.window(driver.window_handles[1])
    # Добавьте товар в корзину
    driver.find_element(By.LINK_TEXT, 'Add to cart').click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    Alert(driver).accept()
    # Закройте вкладку с товаром
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    # На начальной вкладке откройте корзину
    driver.find_element(By.ID, 'cartur').click()
    # Убедитесь, что в корзине тот товар, который вы добавляли
    item_in_cart = driver.find_element(By.XPATH, '//*[@id="tbodyid"]/tr/td[2]').text
    driver.implicitly_wait(10)
    assert item_in_cart == item_to_add


# https://demoqa.com/menu# выбрать Main item2 -> SUB SUB List -> Sub Sub Item 2
# - здесь никакого ассерта не получится сделать
def test_two(driver):
    driver.get('https://demoqa.com/menu#')
    first_button = driver.find_element(By.LINK_TEXT, 'Main Item 2')
    second_button = driver.find_element(By.XPATH, '//*[text()="SUB SUB LIST »"]')
    third_button = driver.find_element(By.XPATH, '//*[text()="Sub Sub Item 2"]')
    ActionChains(driver).move_to_element(first_button).move_to_element(second_button).click(third_button).perform()


# https://www.qa-practice.com/elements/alert/prompt
# Нажать на кнопку "Click", ввести в алерт какой-то ваш текст, нажать ок, проверить, что текст,
# который вы ввели, появился в секции результата.
def test_three(driver):
    driver.get('https://www.qa-practice.com/elements/alert/prompt')
    driver.find_element(By.CLASS_NAME, 'a-button').click()
    Alert(driver).send_keys('Hello!')
    Alert(driver).accept()
    res = driver.find_element(By.ID, 'result-text').text
    assert res == 'Hello!'
