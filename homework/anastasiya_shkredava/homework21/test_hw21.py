import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    return chrome_driver


def test_one(driver):
    driver.get('https://www.demoblaze.com/index.html')
    driver.execute_script("window.scrollTo(0, 900)")
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'card-block')))
    items = driver.find_elements(By.CLASS_NAME, "card-title")
    item_to_add = items[0].text
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(items[0]).key_up(Keys.CONTROL).perform()
    driver.switch_to.window(driver.window_handles[1])
    add_to_card_loc = (By.CSS_SELECTOR, "[onclick='addToCart(1)']")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(add_to_card_loc))
    driver.find_element(*add_to_card_loc).click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    Alert(driver).accept()
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.ID, "cartur").click()
    added_item_loc = (By.XPATH, "//*[@id='tbodyid']/tr/td[2]")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(added_item_loc))
    added_item = driver.find_element(*added_item_loc)
    assert item_to_add == added_item.text


def test_two(driver):
    driver.get('https://demoqa.com/menu#')
    driver.execute_script("window.scrollTo(0, 300)")
    actions = ActionChains(driver)
    actions.move_to_element(driver.find_element(By.LINK_TEXT, 'Main Item 2'))
    actions.move_to_element(driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/ul/li[3]/a'))
    actions.move_to_element(driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/ul/li[3]/ul/li[2]/a'))
    actions.perform()


def test_three(driver):
    driver.get('https://www.qa-practice.com/elements/alert/prompt')
    driver.find_element(By.LINK_TEXT, 'Click').click()
    text = 'some text'
    Alert(driver).send_keys(text)
    Alert(driver).accept()
    result_text = driver.find_element(By.ID, 'result-text').text
    assert result_text == text
