# Выберите несколько чекбоксов и нажмите на кнопку Submit, получите со страницы тот текст, который появится
# в секции "Selected checkboxes". Распечатайте этот текст. Получите название кнопки и распечатайте его.
#
#     Для того, чтобы выбрать чекбокс, нужно этот элемент найти на странице, а потом выполнить для него click()
#     Для того, чтобы нажать на кнопку, нужно найти элемент кнопки на странице, а потом выполнить для нее click()
#     Для того, чтобы получить название кнопки, нужно будет воспользоваться методом get_attribute(),
#     который я показывал на занятии

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument('start-maximized')
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.qa-practice.com/elements/checkbox/mult_checkbox')

checkbox_one = driver.find_element(By.ID, 'id_checkboxes_0')
checkbox_two = driver.find_element(By.ID, 'id_checkboxes_1')
submit = driver.find_element(By.ID, 'submit-id-submit')
checkbox_one.click()
checkbox_two.click()
submit.click()

res = driver.find_element(By.ID, 'result')
button_submit = driver.find_element(By.ID, 'submit-id-submit')
print(f'\nResult text:\n\n{res.text}')
print(f'\nButton name - {button_submit.get_attribute("value")}')
