from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Chrome()
driver.set_window_size(650, 1000)
driver.get('https://demoqa.com/automation-practice-form')

driver.find_element(By.XPATH, '//*[@placeholder="First Name"]').send_keys('Nik')
driver.find_element(By.XPATH, '//*[@placeholder="Last Name"]').send_keys('S')
driver.find_element(By.XPATH, '//*[@placeholder="name@example.com"]').send_keys('nikkk@mail.ru')

# не разобрался почему не работает driver.find_element(By.XPATH, '//input[@id="gender-radio-1"]').click()
driver.find_element(By.CSS_SELECTOR, 'label[for="gender-radio-1"]').click()
driver.find_element(By.XPATH, '//*[@placeholder="Mobile Number"]').send_keys('79991453014')
driver.find_element(By.XPATH, '//*[@id="dateOfBirthInput"]').click()
year = driver.find_element(By.XPATH, '//*[@class="react-datepicker__year-select"]')
select = Select(year)
select.select_by_value('1992')
driver.find_element(By.XPATH, '//*[@class="react-datepicker__month-select"]').click()
month = driver.find_element(By.XPATH, '//*[@class="react-datepicker__month-select"]')
select = Select(month)
select.select_by_value('7')
driver.find_element(By.XPATH, '//*[@class="react-datepicker__month-select"]').click()
day = driver.find_element(By.XPATH, '//*[@class="react-datepicker__day react-datepicker__day--028"]').click()

driver.execute_script("window.scrollTo(0, 1000)")

subjects = driver.find_element(By.ID, 'subjectsInput')
subjects.send_keys('hindi')
driver.implicitly_wait(1)
subjects.send_keys(Keys.ENTER)

driver.find_element(By.XPATH, '//*[@for="hobbies-checkbox-3"]').click()
driver.find_element(By.XPATH, '//*[@id="currentAddress"]').send_keys('Kollektornaya st. 32')

driver.execute_script("window.scrollTo(0, 1000)")

driver.find_element(By.XPATH, '//*[@class=" css-1wa3eu0-placeholder"]').click()
driver.find_element(By.XPATH, '//*[@id="react-select-3-option-0"]').click()

driver.find_element(By.XPATH, '//*[@class=" css-1wa3eu0-placeholder"]').click()
driver.find_element(By.XPATH, '//*[@id="react-select-4-option-0"]').click()

driver.find_element(By.ID, 'submit').click()

sleep(5)
