# Напишите программу, которая зайдет на страницу https://demoqa.com/automation-practice-form
# и полностью заполнит форму (кроме загрузки файла) и нажмет Submit.

# Небольшая особенность
# Страничка эта немного кривая, иногда реклама перекрывает элементы и по ним невозможно кликнуть
# (но сейчас, смотрю, вообще реклама пропала). Если бы это было приложение, которое мы тестируем, это был бы баг.
# Но работаем с тем, что есть. И для нас это даже плюс, нужно найти как выкрутиться.
# Обойти это можно уменьшив размер экрана браузера - тогда элементы перераспределяются и становятся доступны.
# Но если реклама так и не появится, то ничего на странице не мешает.

# Для самых любопытных (выполнять необязательно)
#     Заполните также поле загрузки файла, т.е. приаттачьте файл.
#     После отправки вам будет отображено окошко с тем что вы ввели. Получите со страницы содержимое этого окошка
#     и распечатайте (выведите на экран).

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_argument('--window-size=700,1080')
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://demoqa.com/automation-practice-form')

driver.find_element(By.ID, 'firstName').send_keys('Vika')  # name
driver.find_element(By.ID, 'lastName').send_keys('Avr')  # last name
driver.find_element(By.ID, 'userEmail').send_keys('Vika@gmail.com')  # mail
driver.find_element(By.CSS_SELECTOR, 'label[for="gender-radio-2"]').click()  # gender
driver.find_element(By.ID, 'userNumber').send_keys('1234567890')  # phone number

driver.execute_script("window.scrollTo(0, 1080)")

# birthday
driver.find_element(By.ID, 'dateOfBirthInput').click()
driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Choose Wednesday, June 7th, 2023"]').click()
# another method to search birthday
# Select(driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select')).select_by_value('6')
# Select(driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select')).select_by_value('2023')
# driver.find_element(By.CLASS_NAME, 'react-datepicker__day--007').click()

# subjects
driver.find_element(By.ID, 'subjectsInput').send_keys('Maths')
driver.find_element(By.ID, 'react-select-2-option-0').click()
# получается добавить в поле только один предмет, с последующими выедает ошибку
# driver.find_element(By.ID, 'subjectsInput').send_keys('Commerce')
# driver.find_element(By.ID, 'react-select-2-option-0').click()

# hobbies
driver.find_element(By.CSS_SELECTOR, 'label[for="hobbies-checkbox-1"]').click()
driver.find_element(By.CSS_SELECTOR, 'label[for="hobbies-checkbox-2"]').click()

driver.find_element(By.ID, 'uploadPicture').send_keys('/home/victoria/Загрузки/bee.jpg')  # picture
driver.find_element(By.ID, 'currentAddress').send_keys('Here')  # current address

# state
driver.find_element(By.ID, 'state').click()
driver.find_element(By.ID, 'react-select-3-option-0').click()

# city
driver.find_element(By.ID, 'city').click()
driver.find_element(By.ID, 'react-select-4-option-0').click()

driver.find_element(By.ID, 'submit').submit()  # submit

print(driver.find_element(By.TAG_NAME, 'table').text)
