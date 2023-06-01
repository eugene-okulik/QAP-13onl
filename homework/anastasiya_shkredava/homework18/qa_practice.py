from selenium import webdriver
from selenium.webdriver.common.by import By


chrom_driver = webdriver.Chrome()
chrom_driver.get('https://www.qa-practice.com/elements/checkbox/mult_checkbox')
one = chrom_driver.find_element(By.ID, "id_checkboxes_0")
two = chrom_driver.find_element(By.ID, "id_checkboxes_1")
button = chrom_driver.find_element(By.NAME, "submit")
one.click()
two.click()
button.click()
clicked_button = chrom_driver.find_element(By.NAME, "submit")
print('Button name is', clicked_button.get_attribute("value"))
selected_checkboxes = chrom_driver.find_element(By.NAME, "result")
print(selected_checkboxes.text)
