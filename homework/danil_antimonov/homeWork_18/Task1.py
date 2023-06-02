from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://www.qa-practice.com/elements/checkbox/mult_checkbox')
find_checkbox1 = driver.find_element(By.ID, 'id_checkboxes_0')
find_checkbox2 = driver.find_element(By.ID, 'id_checkboxes_1')
find_checkbox3 = driver.find_element(By.ID, 'id_checkboxes_2')
find_submit_button = driver.find_element(By.NAME, "submit")
find_checkbox1.click()
find_checkbox2.click()
find_checkbox3.click()
find_submit_button.click()
print('Button name is', driver.find_element(By.NAME, "submit").get_attribute('value'))
result_of_selection = driver.find_element(By.ID, 'result')
print(result_of_selection.text)
