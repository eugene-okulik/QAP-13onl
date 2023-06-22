from selenium.webdriver.common.by import By


first_name_loc = (By.ID, "firstname")
last_name_loc = By.ID, "lastname"
e_mail_loc = (By.ID, "email_address")
passw_loc = (By.ID, "password")
confirm_passw_loc = (By.ID, "password-confirmation")
create_button_loc = (By.CLASS_NAME, "submit")
confirmation_error_loc = (By.ID, "password-confirmation-error")
password_error_loc = (By.ID, "password-error")
last_name_error = (By.ID, "lastname-error")
