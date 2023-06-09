from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


chrome_options = Options()
chrome_options.add_argument('start-maximized')
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://demoqa.com/automation-practice-form')


driver.find_element(By.ID, 'firstName').send_keys('Vlad')
driver.find_element(By.ID, 'lastName').send_keys('Zavistovich')
driver.find_element(By.ID, 'userEmail').send_keys('vladzevar@gmail.com')
driver.find_element(By.CSS_SELECTOR, 'label[for="gender-radio-1"]').click()
driver.find_element(By.ID, 'userNumber').send_keys('48777028777')
driver.find_element(By.ID, 'dateOfBirthInput').click()
driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Choose Friday, June 23rd, 2023"]').click()
driver.find_element(By.ID, 'subjectsInput').send_keys('Polish')
driver.find_element(By.CSS_SELECTOR, 'label[for="hobbies-checkbox-3"]').click()
driver.find_element(By.CSS_SELECTOR, 'label[for="hobbies-checkbox-2"]').click()
driver.find_element(By.CSS_SELECTOR, 'label[for="hobbies-checkbox-1"]').click()
driver.find_element(By.ID, 'currentAddress').send_keys('3-я улица строителей, дом 25')
driver.find_element(By.ID, 'state').click()
driver.find_element(By.ID, 'react-select-3-option-0').click()
driver.find_element(By.ID, 'city').click()
driver.find_element(By.ID, 'react-select-4-option-0').click()
driver.find_element(By.ID, 'submit').submit()
