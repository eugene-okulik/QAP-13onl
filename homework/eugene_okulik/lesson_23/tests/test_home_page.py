from selenium.webdriver.common.by import By


def test_search_exists(driver):
    driver.get('https://magento.softwaretestingboard.com/')
    assert driver.find_element(By.NAME, 'q').is_displayed()
