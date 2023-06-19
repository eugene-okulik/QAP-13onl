import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.demoblaze.com/index.html")

driver.execute_script("window.open('about:blank', 'new_tab');")

driver.switch_to.window(driver.window_handles[-1])

driver.get("https://www.demoblaze.com/prod.html?idp_=1")

# Без слипа валится сразу. Со слипом хотя бы доходит до алерта и уже там проблемы. Идей нет как пофиксить
time.sleep(3)

btn = driver.find_element(By.CLASS_NAME, 'btn-success')
driver.execute_script("arguments[0].click();", btn)
# driver.find_element(By.CLASS_NAME, 'btn-success').click()

alert = Alert(driver)
driver.implicitly_wait(10)
alert.accept()
driver.implicitly_wait(10)

# driver.close()

cart = driver.find_element(By.CLASS_NAME, value='nav-link')
cart.click()

title = driver.find_element(By.XPATH, '//*[@id="tbodyid"]/tr/td[2]')
assert title.text == 'Samsung galaxy s6'

driver.quit()
