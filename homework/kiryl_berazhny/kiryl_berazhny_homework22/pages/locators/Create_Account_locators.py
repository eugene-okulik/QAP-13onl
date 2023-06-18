from selenium.webdriver.common.by import By


first_name = (By.ID, 'firstname')
last_name = (By.ID, 'lastname')
email_address = (By.ID, 'email_address')
password = (By.ID, 'password')
password_confirmation = (By.ID, 'password-confirmation')
submit = (By.XPATH, '//*[@id="form-validate"]/div/div[1]/button')
check_pass = (By.ID, 'password-strength-meter')
error_text = (By.CLASS_NAME, 'error')
