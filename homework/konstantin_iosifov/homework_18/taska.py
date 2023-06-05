import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.qa-practice.com/elements/checkbox/mult_checkbox")

driver.find_element(By.ID, value="id_checkboxes_0").click()
driver.find_element(By.ID, value="id_checkboxes_1").click()
driver.find_element(By.ID, value="id_checkboxes_2").click()

driver.find_element(By.ID, value="submit-id-submit").click()

print(driver.find_element(By.ID, value="result-text").text)
print(driver.find_element(By.ID, value="submit-id-submit").get_attribute("value"))

# time.sleep(3)