from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()


def dropdown():
    driver.get('https://magento.softwaretestingboard.com/sales/guest/form/')
    find_by = driver.find_element(By.ID, 'quick-search-type-id')
    select = Select(find_by)
    select.select_by_value('zip')


def cookies_test():
    driver.get('https://magento.softwaretestingboard.com/sales/guest/form/')
    driver.delete_all_cookies()
    print(driver.get_cookie('PHPSESSID'))
    driver.add_cookie({'name': 'test', 'value': 'bar'})
    print(driver.get_cookies())
    contact_us = driver.find_element(By.PARTIAL_LINK_TEXT, 'Contact')
    contact_us.click()


dropdown()
cookies_test()
