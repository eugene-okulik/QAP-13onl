from selenium.webdriver.common.by import By

title_loc = (By.CLASS_NAME, 'page-title')
first_name_loc = (By.ID, 'firstname')
last_name_loc = (By.ID, 'lastname')
email_loc = (By.NAME, 'email')
password_loc = (By.ID, 'password')
confirm_password_loc = (By.NAME, 'password_confirmation')
button_loc = (By.CSS_SELECTOR, '.action.submit.primary')
email_error_mess = (By.ID, 'email_address-error')
short_passw_error_mess = (By.ID, 'password-error')
wait_loc = (By.CLASS_NAME, 'not-logged-in')
