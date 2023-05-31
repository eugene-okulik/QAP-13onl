from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep


chrome_options = Options()
# chrome_options.add_argument('start-maximized')
# chrome_options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.amazon.com/')
# driver.maximize_window()
# print(driver.current_url)
# print(driver.title)

country = driver.find_element(By.ID, 'glow-ingress-line2')
print(country.text)
deliver_to = driver.find_element(By.CLASS_NAME, 'a-popover-trigger')
print(deliver_to.get_attribute('class'))

sleep(1)
