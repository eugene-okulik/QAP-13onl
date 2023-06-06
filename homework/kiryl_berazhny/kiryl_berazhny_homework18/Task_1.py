# Homework_18

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.qa-practice.com/elements/checkbox/mult_checkbox')
button1 = driver.find_element(By.ID, 'id_checkboxes_0')
button2 = driver.find_element(By.ID, 'id_checkboxes_1')
button3 = driver.find_element(By.ID, 'id_checkboxes_2')
sub_button = driver.find_element(By.ID, 'submit-id-submit')
button1.click()
button2.click()
button3.click()
sub_button.click()
text_result = driver.find_element(By.ID, 'result')
text_button = driver.find_element(By.ID, 'submit-id-submit')
print(text_result.text)
print(text_button.get_attribute('name'))
