from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os


driver = webdriver.Chrome()
driver.get('https://demoqa.com/automation-practice-form')

driver.find_element(By.ID, 'firstName').send_keys('Kiryl')
driver.find_element(By.ID, 'lastName').send_keys('Berazhny')
driver.find_element(By.ID, 'userEmail').send_keys('kirylberag@gmail.com')
driver.find_element(By.CSS_SELECTOR, 'label[for="gender-radio-1"]').click()
driver.find_element(By.ID, 'userNumber').send_keys('0298148761')

driver.execute_script("window.scrollTo(0, 1000)")

driver.find_element(By.ID, 'dateOfBirthInput').send_keys(Keys.COMMAND + 'a')
driver.find_element(By.ID, 'dateOfBirthInput').send_keys('05.09.1993' + Keys.ENTER)
driver.find_element(By.ID, 'subjectsInput').send_keys('Physics')
driver.find_element(By.ID, 'subjectsInput').send_keys(Keys.ENTER)
driver.find_element(By.CSS_SELECTOR, 'label[for="hobbies-checkbox-3"]').click()
os_path = os.path.join(os.path.dirname(__file__), 'płyta szalunkowa.png')
driver.find_element(By.ID, 'uploadPicture').send_keys(os_path)
driver.find_element(By.ID, 'currentAddress').send_keys('87-720, Ciechocinek, ul. Aleja 700-lecia 3C')

driver.set_window_size(565, 525)
driver.execute_script("window.scrollTo(0, 1850)")

driver.find_element(By.ID, 'state').click()
driver.find_element(By.ID, 'react-select-3-option-2').click()
driver.find_element(By.ID, 'city').click()
driver.find_element(By.ID, 'react-select-4-option-1').click()
driver.find_element(By.ID, 'submit').send_keys(Keys.ENTER)

print(driver.find_element(By.CLASS_NAME, 'table-responsive').text)
