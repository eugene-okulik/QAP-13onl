from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import pytest


@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument('--window-size=640,1300')
    c_driver = webdriver.Chrome(options=chrome_options)
    return c_driver


def test_filling_form(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    firstname = driver.find_element(By.ID, 'firstName')
    firstname.send_keys('Вася')
    lastname = driver.find_element(By.ID, 'lastName')
    lastname.send_keys('Пупкин')
    usermail = driver.find_element(By.ID, 'userEmail')
    usermail.send_keys('pupkin@gmail.com')
    driver.find_element(By.CSS_SELECTOR, 'label[for="gender-radio-1"]').click()
    mobile_number = driver.find_element(By.ID, 'userNumber')
    mobile_number.send_keys('1234567890')
    driver.find_element(By.ID, 'dateOfBirthInput').click()
    year_of_birth = driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select')
    select = Select(year_of_birth)
    select.select_by_value('1995')
    day_of_birth = driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select')
    select = Select(day_of_birth)
    select.select_by_value('9')
    driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Choose Sunday, October 1st, 1995"]').click()
    subjects = driver.find_element(By.ID, 'subjectsInput')
    subjects.send_keys('English')
    driver.implicitly_wait(1)
    subjects.send_keys(Keys.ENTER)
    driver.find_element(By.XPATH, '//label[@for="hobbies-checkbox-1"]').click()
    driver.find_element(By.ID, 'currentAddress').send_keys('3-я улица строителей, дом 25')
    driver.find_element(By.ID, 'state').click()
    driver.find_element(By.ID, 'react-select-3-option-0').click()
    driver.find_element(By.ID, 'city').click()
    driver.find_element(By.ID, 'react-select-4-option-0').click()
    driver.find_element(By.ID, 'uploadPicture').send_keys("C:/PythonPrj/TutorProject/"
                                                          "QAP-13onl/homework/danil_antimonov/homeWork_19/pict.jpg")
    driver.find_element(By.ID, 'submit').submit()
