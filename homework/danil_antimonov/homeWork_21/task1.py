from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture()
def driver():
    driver_options = Options()
    driver_options.add_argument('--window-size=1300,1000')
    driver_chr = webdriver.Chrome(options=driver_options)
    driver_chr.implicitly_wait(2)
    return driver_chr


def test_one(driver):
    driver.get('https://www.demoblaze.com/index.html')
    original_tab = driver.current_window_handle
    driver.find_element(By.LINK_TEXT, 'Samsung galaxy s6').send_keys(Keys.CONTROL, Keys.ENTER)
    all_tabs = driver.window_handles
    for w in all_tabs:
        if w != original_tab:
            driver.switch_to.window(w)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[onclick='addToCart(1)']")))
    driver.find_element(By.LINK_TEXT, 'Add to cart').click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    Alert(driver).accept()
    driver.close()
    driver.switch_to.window(original_tab)
    driver.find_element(By.LINK_TEXT, 'Cart').click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='tbodyid']/tr/td[2]")))
    assert driver.find_element(By.XPATH, "//td[text()='Samsung galaxy s6']").is_displayed()


def test_two(driver):
    driver.get('https://demoqa.com/menu#')
    driver.find_element(By.XPATH, "//a[text()='Main Item 2']").click()
    driver.find_element(By.XPATH, "//a[text()='SUB SUB LIST »']").click()
    driver.find_element(By.XPATH, "//a[text()='Sub Sub Item 2']").click()


def test_three(driver):
    driver.get('https://www.qa-practice.com/elements/alert/prompt#')
    driver.find_element(By.XPATH, "//a[text()='Click']").click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    text = 'dfdfdfdsfdsfdsf'
    Alert(driver).send_keys(keysToSend=text)
    Alert(driver).accept()
    assert driver.find_element(By.ID, 'result-text').text == text
