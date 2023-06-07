from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.qa-practice.com/elements/checkbox/mult_checkbox')
sleep(1)

checkboxes = driver.find_elements(By.NAME, "checkboxes")
for checkbox in checkboxes:
    checkbox.click()
sleep(1)

submit = driver.find_element(By.NAME, "submit")
submit.click()
sleep(1)

result = driver.find_element(By.ID, "result-text")
print(result.text)

attribute = driver.find_element(By.NAME, "submit")
button_text = attribute.get_attribute("value")
print(button_text)
