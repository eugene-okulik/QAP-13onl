from selenium.webdriver.common.by import By


login_loc = (By.ID, 'email')
passw_loc = (By.ID, 'pass')
button_loc = (By.ID, 'send2')
# email_error = (By.ID, 'email-error')
email_error = (By.CLASS_NAME, 'error')
pass_validation = (By.ID, 'pass-error')
logo = (By.CSS_SELECTOR, '.logo')
