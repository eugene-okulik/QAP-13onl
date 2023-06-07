import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import tabulate

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://demoqa.com/automation-practice-form")

# ФИО
driver.find_element(By.ID, value="firstName").send_keys("Constantine")
driver.find_element(By.ID, value="lastName").send_keys("Iosifov")

# Email
driver.find_element(By.ID, value="userEmail").send_keys("user@user.com")

# Gender
driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[3]/div[2]/div[1]/label")\
    .click()

# Phone number
driver.find_element(By.ID, value="userNumber").send_keys("3752912345")

# DOB
dob = driver.find_element(By.ID, value="dateOfBirthInput").click()

calendar_month = Select(driver.find_element(By.CLASS_NAME, value="react-datepicker__month-select"))
calendar_month.select_by_value("2")

calendar_year = Select(driver.find_element(By.CLASS_NAME, value="react-datepicker__year-select"))
calendar_year.select_by_value("1996")

calendar_day = driver.find_element(By.CLASS_NAME, value="react-datepicker__day--013").click()

# Subject //// Никак не получается хотя бы что-то ввести в Subject.
# Пробовал по классу, по xpath. И в ошибке все равно падает почему-то класс is not reachable by keyboard############
# find_sub = driver.find_element(By.XPATH, value="//*[@id='subjectsContainer']/div/div[1]")
# find_sub.click()
# enter_sub = driver.find_element(By.XPATH, value="//*[@id='subjectsContainer']/div")
# enter_sub.send_keys("English")
# selenium.common.exceptions.ElementNotInteractableException: Message:
# Element <div class="subjects-auto-complete__control subjects-auto-complete__control--is-focused subjects-auto-complete__control--menu-is-open css-1pahdxg-control"> is not reachable by keyboard

# Hobbies
driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[7]/div[2]/div[1]/label")\
    .click()

driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[7]/div[2]/div[3]/label")\
    .click()

# Attach
upload = driver.find_element(By.ID, value="uploadPicture")
upload.send_keys("E:\\wallpapers\\bb.jpg")

# Current address
driver.find_element(By.ID, value="currentAddress").send_keys("Belarus")

#State
state_drop = driver.find_element(By.ID, value="state").click()
time.sleep(1)
state_sel = driver.find_element(By.ID, value="react-select-3-option-0").click()

# City
city_drop = driver.find_element(By.ID, value="city").click()
time.sleep(1)
city_sel = driver.find_element(By.ID, value="react-select-4-option-0").click()

# Submit
btn = driver.find_element(By.ID, value="submit")
driver.execute_script("arguments[0].click();", btn)

# Student Name
stud_name_label = driver.find_element(By.XPATH, value="/html/body/div[5]/div/div/div[2]/div/table/tbody/tr[1]/td[1]")\
    .text
stud_name_value = driver.find_element(By.XPATH, value="/html/body/div[5]/div/div/div[2]/div/table/tbody/tr[1]/td[2]")\
    .text

# Student Email
stud_email_label = driver.find_element(By.XPATH, value="/html/body/div[5]/div/div/div[2]/div/table/tbody/tr[2]/td[1]")\
    .text
stud_email_value = driver.find_element(By.XPATH, value="/html/body/div[5]/div/div/div[2]/div/table/tbody/tr[2]/td[2]")\
    .text

# Gender
stud_gender_label = driver.find_element(By.XPATH, value="/html/body/div[5]/div/div/div[2]/div/table/tbody/tr[3]/td[1]")\
    .text
stud_gender_value = driver.find_element(By.XPATH, value="/html/body/div[5]/div/div/div[2]/div/table/tbody/tr[3]/td[2]")\
    .text

# Mobile phone
stud_mobile_label = driver.find_element(By.XPATH, value="/html/body/div[5]/div/div/div[2]/div/table/tbody/tr[4]/td[1]")\
    .text
stud_mobile_value = driver.find_element(By.XPATH, value="/html/body/div[5]/div/div/div[2]/div/table/tbody/tr[4]/td[2]")\
    .text

# DOB
stud_dob_label = driver.find_element(By.XPATH, value="/html/body/div[5]/div/div/div[2]/div/table/tbody/tr[5]/td[1]")\
    .text
stud_dob_value = driver.find_element(By.XPATH, value="/html/body/div[5]/div/div/div[2]/div/table/tbody/tr[5]/td[2]")\
    .text

# Subjects
stud_subj_label = driver.find_element(By.XPATH, value="/html/body/div[5]/div/div/div[2]/div/table/tbody/tr[6]/td[1]")\
    .text
# stud_subj_value = driver.find_element(By.XPATH, value="/html/body/div[5]/div/div/div[2]/div/table/tbody/tr[5]/td[2]")\
    #.text

# Hobbies
stud_hobb_label = driver.find_element(By.XPATH, value="/html/body/div[5]/div/div/div[2]/div/table/tbody/tr[7]/td[1]")\
    .text
stud_hobb_value = driver.find_element(By.XPATH, value="/html/body/div[5]/div/div/div[2]/div/table/tbody/tr[7]/td[2]")\
    .text

# Picture
stud_pic_label = driver.find_element(By.XPATH, value="/html/body/div[5]/div/div/div[2]/div/table/tbody/tr[8]/td[1]")\
    .text
stud_pic_value = driver.find_element(By.XPATH, value="/html/body/div[5]/div/div/div[2]/div/table/tbody/tr[8]/td[2]")\
    .text

# Address
stud_addr_label = driver.find_element(By.XPATH, value="/html/body/div[5]/div/div/div[2]/div/table/tbody/tr[9]/td[1]")\
    .text
stud_addr_value = driver.find_element(By.XPATH, value="/html/body/div[5]/div/div/div[2]/div/table/tbody/tr[9]/td[2]")\
    .text

# State and City
stud_sc_label = driver.find_element(By.XPATH, value="/html/body/div[5]/div/div/div[2]/div/table/tbody/tr[10]/td[1]")\
    .text
stud_sc_value = driver.find_element(By.XPATH, value="/html/body/div[5]/div/div/div[2]/div/table/tbody/tr[10]/td[2]")\
    .text

# Close
time.sleep(1)
driver.find_element(By.ID, value="closeLargeModal").click()
data = [
    ['Label', 'Values'],
    [stud_name_label, stud_name_value],
    [stud_email_label, stud_email_value],
    [stud_gender_label, stud_gender_value],
    [stud_mobile_label, stud_mobile_value],
    [stud_dob_label, stud_dob_value],
    [stud_subj_label, 'None'],
    [stud_hobb_label, stud_hobb_value],
    [stud_pic_label, stud_pic_value],
    [stud_addr_label, stud_addr_value],
    [stud_sc_label, stud_sc_value]
]
results = tabulate.tabulate(data)
print(results)
