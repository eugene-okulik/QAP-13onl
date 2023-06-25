from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.qa-practice.com/elements/checkbox/mult_checkbox')
driver.maximize_window()

checkboxes_one = driver.find_element(By.ID, 'id_checkboxes_0')
checkboxes_two = driver.find_element(By.ID, 'id_checkboxes_1')
checkboxes_three = driver.find_element(By.ID, 'id_checkboxes_2')
submit_button = driver.find_element(By.ID, 'submit-id-submit')

checkboxes_one.click()
checkboxes_three.click()

submit_button.click()

text_result = driver.find_element(By.ID, 'result')
text_button = driver.find_element(By.ID, 'submit-id-submit')
print(text_result.text)
print(text_button.get_attribute('value'))

sleep(2)

