from selenium.webdriver.common.by import By


def test_title_correct(driver):
    driver.get('https://magento.softwaretestingboard.com/what-is-new.html')
    assert driver.find_element(By.ID, 'page-title-heading').text == "What's New"
