from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://demoqa.com/automation-practice-form')

input_name = driver.find_element(By.ID, "firstName")
input_name.send_keys("Pavel")
input_lastname = driver.find_element(By.ID, "lastName")
input_lastname.send_keys("Petochenko")

input_email = driver.find_element(By.ID, 'userEmail')
input_email.send_keys('ppppasha@gmail.ru')

driver.find_element(By.CSS_SELECTOR, 'label[for=gender-radio-1]').click()

mobile = driver.find_element(By.ID, 'userNumber')
mobile.send_keys('6666666666')

driver.find_element(By.ID, 'dateOfBirthInput').click()
driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Choose Friday, June 16th, 2023"]').click()

driver.find_element(By.ID, 'subjectsInput').send_keys('Commerce')
driver.implicitly_wait(2)
driver.find_element(By.ID, 'react-select-2-option-0').click()

driver.find_element(By.CSS_SELECTOR, 'label[for="hobbies-checkbox-2"]').click()
driver.find_element(By.CSS_SELECTOR, 'label[for="hobbies-checkbox-3"]').click()

driver.find_element(By.ID, 'uploadPicture').send_keys('/home/palamnis/Загрузки/meme.jpg')
driver.find_element(By.ID, 'currentAddress').send_keys('1600 Pennsylvania Avenue NW, Washington, DC 20500, USA ')

driver.set_window_size(800, 1000)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

driver.find_element(By.ID, 'state').click()
driver.find_element(By.ID, 'react-select-3-option-2').click()
driver.find_element(By.ID, 'city').click()
driver.find_element(By.ID, 'react-select-4-option-0').click()
sleep(2)

driver.find_element(By.ID, 'submit').click()
sleep(2)
table = driver.find_element(By.TAG_NAME, 'table').text
print(table)
