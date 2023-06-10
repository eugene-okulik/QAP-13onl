from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from time import sleep


@pytest.fixture()
def driver():
    c_driver = webdriver.Chrome()
    # c_driver.implicitly_wait(10)
    return c_driver


def test_enter(driver):
    text = 'sdsdfsdfsdf'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    input_field = driver.find_element(By.NAME, 'text_string')
    input_field.send_keys(text)
    input_field.send_keys(Keys.ENTER)
    assert driver.find_element(By.ID, 'result-text').text == text


def test_order_by_price(driver):
    driver.get('https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html')
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), 'Default welcome msg!')
    )
    sorter = driver.find_element(By.ID, 'sorter')
    sorter_select = Select(sorter)
    sorter_select.select_by_value('price')
    prices = driver.find_elements(By.CLASS_NAME, 'price-wrapper')
    price_values = [float(x.text.lstrip('$')) for x in prices]
    assert sorted(price_values) == price_values
    # sleep(3)


def test_delayed_button(driver):
    driver.get('https://demoqa.com/dynamic-properties')
    # button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'visibleAfter')))
    driver.implicitly_wait(4)
    assert driver.find_element(By.ID, 'visibleAfter').is_displayed()


def test_iframe(driver):
    driver.get('https://www.qa-practice.com/elements/iframe/iframe_page')
    driver.implicitly_wait(10)
    iframe = driver.find_element(By.TAG_NAME, 'iframe')
    driver.switch_to.frame(iframe)
    hamb_menu = driver.find_element(By.CSS_SELECTOR, '[aria-label="Toggle navigation"]')
    hamb_menu.click()
    driver.switch_to.default_content()
    tab = driver.find_element(By.LINK_TEXT, 'Iframe')
    tab.click()
    sleep(3)


def test_men_jackets(driver):
    driver.get('https://magento.softwaretestingboard.com/')
    driver.implicitly_wait(2)
    men = driver.find_element(By.ID, 'ui-id-5')
    tops = driver.find_element(By.ID, 'ui-id-17')
    jackets = driver.find_element(By.ID, 'ui-id-19')
    actions = ActionChains(driver)
    actions.move_to_element(men)
    actions.move_to_element(tops)
    actions.click(jackets)
    actions.perform()


def test_drag_ad_drop(driver):
    driver.maximize_window()
    driver.get('https://www.qa-practice.com/elements/dragndrop/boxes')
    draggable = driver.find_element(By.ID, 'rect-draggable')
    droppable = driver.find_element(By.ID, 'rect-droppable')
    # ActionChains(driver).drag_and_drop(draggable, droppable).perform()
    ActionChains(driver).click_and_hold(draggable).move_to_element(droppable).release(droppable).perform()
    drop_text = driver.find_element(By.ID, 'text-droppable').text
    assert drop_text == 'Dropped!'
    # sleep(3)


def test_alert(driver):
    driver.get('https://www.qa-practice.com/elements/alert/alert')
    driver.save_screenshot('screen.png')
    driver.find_element(By.CLASS_NAME, 'a-button').click()
    sleep(1)
    Alert(driver).accept()
    sleep(3)
