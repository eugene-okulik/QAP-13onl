from selenium.webdriver.common.by import By


firstname_error_loc = (By.ID, 'firstname-error')
lastname_error_loc = (By.ID, 'lastname-error')
passw_error_loc = (By.XPATH, '//div[@id="password-error"]')
email_error_loc = (By.XPATH, '//div[@id="email_address-error"]')
passw_confirm_error_loc = (By.ID, 'password-confirmation-error')
button_loc = (By.CSS_SELECTOR, "[title='Create an Account']")
