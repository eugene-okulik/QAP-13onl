from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--window-size=615,641')
chrome_driver = webdriver.Chrome(options=options)
# chrome_driver.maximize_window()
chrome_driver.get('https://demoqa.com/automation-practice-form')
chrome_driver.find_element(By.ID, 'firstName').send_keys('Kung Fu')
chrome_driver.find_element(By.ID, 'lastName').send_keys('Panda')
chrome_driver.find_element(By.ID, 'userEmail').send_keys('kungfupanda@gmail.com')
chrome_driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
chrome_driver.find_element(By.CSS_SELECTOR, 'label[for="gender-radio-1"]').click()
chrome_driver.find_element(By.ID, 'userNumber').send_keys('0123456789')
chrome_driver.find_element(By.ID, 'dateOfBirthInput').click()
chrome_driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Choose Friday, June 23rd, 2023"]').click()
chrome_driver.find_element(By.CSS_SELECTOR, 'input[wfd-id="id8"]').send_keys('English')
chrome_driver.implicitly_wait(1)
chrome_driver.find_element(By.ID, 'react-select-2-option-0').click()
chrome_driver.find_element(By.CSS_SELECTOR, 'input[wfd-id="id8"]').send_keys('Chemistry')
chrome_driver.implicitly_wait(1)
chrome_driver.find_element(By.ID, 'react-select-2-option-0').click()
chrome_driver.find_element(By.CSS_SELECTOR, 'label[for="hobbies-checkbox-1"]').click()
chrome_driver.find_element(By.CSS_SELECTOR, 'label[for="hobbies-checkbox-3"]').click()
# chrome_driver.find_element(By.ID, 'uploadPicture').send_keys("C:\\Temp\\background.png")  # picture uploading
chrome_driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
chrome_driver.find_element(By.ID, 'currentAddress').send_keys('China, st. Hangzhou-105')
chrome_driver.find_element(By.ID, 'state').click()
chrome_driver.find_element(By.ID, 'react-select-3-option-1').click()
chrome_driver.find_element(By.ID, 'city').click()
chrome_driver.find_element(By.ID, 'react-select-4-option-0').click()
chrome_driver.find_element(By.ID, 'submit').submit()
print(chrome_driver.find_element(By.TAG_NAME, 'table').text)
