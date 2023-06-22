from selenium import webdriver
from selenium.webdriver.common.by import By
import os


ch_driver = webdriver.Chrome()
ch_driver.maximize_window()
ch_driver.get('https://demoqa.com/automation-practice-form')


ch_driver.find_element(By.ID, 'firstName').send_keys('Irina')
ch_driver.find_element(By.ID, 'lastName').send_keys('Ivanova')
ch_driver.find_element(By.ID, 'userEmail').send_keys('ivanova@mail.ru')
ch_driver.find_element(By.CSS_SELECTOR, 'label[for="gender-radio-2"]').click()
ch_driver.find_element(By.ID, 'userNumber').send_keys('8005553535')
ch_driver.find_element(By.ID, 'dateOfBirthInput').click()
ch_driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Choose Sunday, July 2nd, 2023"]').click()
ch_driver.find_element(By.CSS_SELECTOR, 'label[for="hobbies-checkbox-1"]').click()
ch_driver.find_element(By.CSS_SELECTOR, 'label[for="hobbies-checkbox-3"]').click()
ch_driver.find_element(By.ID, 'subjectsInput').send_keys('m')
ch_driver.find_element(By.ID, 'react-select-2-option-2').click()
ch_driver.find_element(By.ID, 'subjectsInput').send_keys('b')
ch_driver.find_element(By.ID, 'react-select-2-option-0').click()
path = os.path.dirname(__file__)
sys_path = os.path.join(path, 'img_1.png')
ch_driver.find_element(By.XPATH, '//*[@id="uploadPicture"]').send_keys(sys_path)
ch_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
ch_driver.find_element(By.XPATH, '//*[@id="currentAddress"]').send_keys(
    'Russia, Khabarovsk Territory, Khabarovsk, Pacific street, 217'
)
ch_driver.find_element(By.XPATH, '//*[@id="state"]').click()
ch_driver.find_element(By.XPATH, '//*[@id="react-select-3-option-1"]').click()
ch_driver.find_element(By.XPATH, '//*[@id="city"]').click()
ch_driver.find_element(By.XPATH, '//*[@id="react-select-4-option-0"]').click()
ch_driver.find_element(By.ID, 'submit').submit()
conclusion = ch_driver.find_element(By.CLASS_NAME, 'modal-content')
print(conclusion.text)
