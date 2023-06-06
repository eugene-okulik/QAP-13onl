from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


chrome_options = Options()
chrome_options.add_argument('start-maximized')
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.qa-practice.com/elements/checkbox/mult_checkbox')

checkbox_1 = driver.find_element(By.ID, 'id_checkboxes_0')
checkbox_2 = driver.find_element(By.ID, 'id_checkboxes_1')
checkbox_3 = driver.find_element(By.ID, 'id_checkboxes_2')
sub_but = driver.find_element(By.ID, 'submit-id-submit')
checkbox_1.click()
checkbox_2.click()
checkbox_3.click()
sub_but.click()
text_result = driver.find_element(By.ID, 'result')
text_button = driver.find_element(By.ID, 'submit-id-submit')
print(text_result.text)
print(text_button.get_attribute('name'))
