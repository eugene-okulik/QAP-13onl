from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.qa-practice.com/elements/alert/prompt")

driver.find_element(By.CLASS_NAME, 'a-button').click()
Alert(driver).send_keys('Hello')
Alert(driver).accept()

result_text = driver.find_element(By.ID, 'result-text')
assert result_text.text == 'Hello'

driver.quit()
