from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    return chrome_driver


def test_one(driver):
    driver.get('https://www.demoblaze.com/index.html')
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//*[@href="prod.html?idp_=2"]').send_keys(Keys.CONTROL, Keys.ENTER)
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    driver.find_element(By.XPATH, '// *[ @ id = "tbodyid"]/div[2]/div/a').click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    Alert(driver).accept()
    driver.switch_to.window(tabs[1])
    driver.close()
    driver.switch_to.window(tabs[0])
    driver.find_element(By.XPATH, '// *[ @ id = "cartur"]').click()
    basket = driver.find_element(By.XPATH, '//*[@id="tbodyid"]/tr/td[2]')
    assert basket.text == 'Nokia lumia 1520'


def test_two(driver):
    driver.get('https://demoqa.com/menu#')
    main_item = driver.find_element(By.LINK_TEXT, 'Main Item 2')
    sub_list = driver.find_element(By.XPATH, '//*[text()="SUB SUB LIST »"]')
    sub_item = driver.find_element(By.XPATH, '//*[text()="Sub Sub Item 2"]')
    actions = ActionChains(driver)
    actions.move_to_element(main_item)
    actions.move_to_element(sub_list)
    actions.move_to_element(sub_item)
    actions.perform()


def test_three(driver):
    driver.maximize_window()
    driver.get('https://www.qa-practice.com/elements/alert/prompt')
    driver.find_element(By.CLASS_NAME, 'a-button').click()
    text = 'hi'
    Alert(driver).send_keys(text)
    Alert(driver).accept()
    assert text == driver.find_element(By.ID, 'result-text').text
