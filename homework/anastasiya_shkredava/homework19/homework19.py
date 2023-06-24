from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


options = Options()
options.add_argument('--window-size=700,1280')
chrome_driver = webdriver.Chrome(options=options)

chrome_driver.get('https://demoqa.com/automation-practice-form')

# Name filling
chrome_driver.find_element(By.ID, 'firstName').send_keys('Kung Fu')
chrome_driver.find_element(By.ID, 'lastName').send_keys('Panda')

# Email filling
chrome_driver.find_element(By.ID, 'userEmail').send_keys('kungfupanda@gmail.com')

# Gender filling
chrome_driver.find_element(By.CSS_SELECTOR, 'label[for="gender-radio-1"]').click()

# Mobile number filling
chrome_driver.find_element(By.ID, 'userNumber').send_keys('0123456789')
chrome_driver.execute_script("window.scrollTo(0, 1280)")

# Date of Birth filling
chrome_driver.find_element(By.ID, 'dateOfBirthInput').click()
chrome_driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Choose Friday, June 23rd, 2023"]').click()

# Subjects filling
chrome_driver.implicitly_wait(1)
subjects_field = chrome_driver.find_element(By.ID, 'subjectsInput')
subjects_field.send_keys('English')
chrome_driver.find_element(By.ID, 'react-select-2-option-0').click()
subjects_field.send_keys('Chemistry')
chrome_driver.find_element(By.ID, 'react-select-2-option-0').click()

# Hobbies filling
chrome_driver.find_element(By.CSS_SELECTOR, 'label[for="hobbies-checkbox-1"]').click()
chrome_driver.find_element(By.CSS_SELECTOR, 'label[for="hobbies-checkbox-3"]').click()

# Picture uploading
path = os.path.dirname(__file__)
sys_path = os.path.join(path, 'symbol.PNG')
chrome_driver.find_element(By.ID, 'uploadPicture').send_keys(sys_path)
chrome_driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

# Current Address filling
chrome_driver.find_element(By.ID, 'currentAddress').send_keys('China, st. Hangzhou-105')

# State and City filling
chrome_driver.find_element(By.ID, 'state').click()
chrome_driver.find_element(By.ID, 'react-select-3-option-1').click()
chrome_driver.find_element(By.ID, 'city').click()
chrome_driver.find_element(By.ID, 'react-select-4-option-0').click()
chrome_driver.find_element(By.ID, 'submit').submit()

# Printing result
wait = WebDriverWait(chrome_driver, 10)
table = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='table-responsive']")))
print(table.text)
