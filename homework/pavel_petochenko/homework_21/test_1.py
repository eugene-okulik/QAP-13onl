import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert


@pytest.fixture
def driver():
    driver_chrome = webdriver.Chrome()
    driver_chrome.maximize_window()
    return driver_chrome


def test_one(driver):
    driver.get('https://www.demoblaze.com/index.html')
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'card-block')))
    element = driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[1]/div/div/h4/a')
    action_chains = ActionChains(driver)
    action_chains.key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "[onclick='addToCart(1)']"))
    ).click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    Alert(driver).accept()
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.ID, "cartur").click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='tbodyid']/tr/td[2]")))
    assert driver.find_element(By.XPATH, '//*[@id="tbodyid"]/tr/td[2]').is_displayed()


def test_two(driver):
    driver.get('https://demoqa.com/menu#')
    driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/a').click()
    driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/ul/li[3]/a').click()
    driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/ul/li[3]/ul/li[2]/a').click()


def test_three(driver):
    driver.get('https://www.qa-practice.com/elements/alert/prompt')
    driver.find_element(By.XPATH, '//*[@id="content"]/a[1]').click()
    text = 'Glory to the soviet union'
    Alert(driver).send_keys(text)
    Alert(driver).accept()
    result = driver.find_element(By.ID, 'result-text').text
    assert result == text
