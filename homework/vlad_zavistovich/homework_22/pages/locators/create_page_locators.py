from selenium.webdriver.common.by import By

name_loc = (By.ID, 'firstname')
surname_loc = (By.ID, 'lastname')
email_loc = (By.ID, 'email_address')
password_loc = (By.ID, 'password')
password_2_loc = (By.ID, 'password-confirmation')
button_loc = (By.CSS_SELECTOR, '.action.submit.primary')
email_message_error_loc = (By.ID, 'email_address-error')
password_message_error_loc = (By.ID, 'password-error')
surname_message_error_loc = (By.ID, 'lastname-error')
