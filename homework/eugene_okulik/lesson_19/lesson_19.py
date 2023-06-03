from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep


driver = webdriver.Chrome()


def first():
    driver.get('https://magento.softwaretestingboard.com/')
    contact_us = driver.find_element(By.PARTIAL_LINK_TEXT, 'Contact')
    contact_us.click()


def second():
    driver.get('https://magento.softwaretestingboard.com/women.html')
    # compare = driver.find_element(By.ID, 'block-compare-heading')
    compare = driver.find_element(By.CSS_SELECTOR, '#block-compare-heading')
    print(compare.text)
    footer_links = driver.find_element(By.CSS_SELECTOR, 'ul.footer.links')
    footer_links_by_xpath = driver.find_element(By.XPATH, '//ul[@class="footer links"]')
    # footer_links = driver.find_element(By.CSS_SELECTOR, '.footer.links')
    # footer_links_by_xpath = driver.find_element(By.XPATH, '//*[@class="footer links"]')
    print(footer_links.text)
    print(footer_links.get_attribute('innerText'))
    print(footer_links_by_xpath.text)
    print(footer_links.value_of_css_property('color'))
    print(footer_links.tag_name)
    # block-compare-heading


def all_products():
    driver.get('https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html')
    sleep(2)
    products = driver.find_elements(By.CSS_SELECTOR, 'div[data-container="product-grid"]')
    products_by_xpath = driver.find_elements(By.XPATH, '//div[@data-container="product-grid"]')
    print('first', products[0].text)
    print('first', products_by_xpath[0].text)
    print('second', products[-1].text)
    print('second', products_by_xpath[-1].text)
    strong = products[0].find_element(By.TAG_NAME, 'strong')
    print(strong.text)


def search():
    driver.get('https://magento.softwaretestingboard.com')
    search_field = driver.find_element(By.NAME, 'q')
    print(search_field.id)
    search_field.send_keys('jacket')
    # search_button = driver.find_element(By.CSS_SELECTOR, 'button[title="Search"]')
    # search_button.click()
    search_field.submit()
    sleep(1)
    search_field = driver.find_element(By.NAME, 'q')  # чинит StaleElementReferenceException
    search_field.clear()
    search_field.send_keys('yoga')
    search_field.submit()


def checkbox():
    driver.get('https://www.qa-practice.com/elements/checkbox/single_checkbox')
    checkbox_elt = driver.find_element(By.ID, 'id_checkbox_0')
    # checkbox.click()
    print(checkbox_elt.is_selected())
    print(driver.find_element(By.ID, 'submit-id-submit').is_displayed())


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


def tabs():
    driver.get('https://www.qa-practice.com/elements/new_tab/link')
    link = driver.find_element(By.ID, 'new-page-link')
    link.click()
    all_tabs = driver.window_handles
    driver.switch_to.window(all_tabs[1])
    result = driver.find_element(By.ID, 'result-text')
    print(result.text)
    driver.close()
    all_tabs = driver.window_handles
    driver.switch_to.window(all_tabs[0])
    link = driver.find_element(By.ID, 'new-page-link')


tabs()

sleep(3)
