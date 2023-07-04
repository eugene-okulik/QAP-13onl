from selenium.webdriver.common.by import By


list_button = (By.ID, 'mode-list')
grid_button = (By.ID, 'modes-label')
quantity = (By.CLASS_NAME, 'price-wrapper')
sort_arrow = (By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[2]/div[4]/a')
sort_select = (By.ID, 'sorter')
sort_price = (By.XPATH, '//*[@id="sorter"]/option[3]')
search = (By.ID, 'search')
