# Задание
# Выберите несколько чекбоксов и нажмите на кнопку Submit, получите со страницы тот текст, который появится в секции
# "Selected checkboxes". Распечатайте этот текст. Получите название кнопки и распечатайте его.
from selenium import webdriver
from selenium.webdriver.common.by import By


ch_driver = webdriver.Chrome()
ch_driver.get('https://www.qa-practice.com/elements/checkbox/mult_checkbox')
checkboxes0 = ch_driver.find_element(By.ID, 'id_checkboxes_0')
checkboxes0.click()
checkboxes2 = ch_driver.find_element(By.ID, 'id_checkboxes_2')
checkboxes2.click()
checkboxes1 = ch_driver.find_element(By.ID, 'id_checkboxes_1')
checkboxes1.click()
button = ch_driver.find_element(By.ID, 'submit-id-submit')
print("Название кнопки: ", button.get_attribute('name'))
button.click()
selected_checkboxes = ch_driver.find_element(By.NAME, "result")
print(selected_checkboxes.text)
