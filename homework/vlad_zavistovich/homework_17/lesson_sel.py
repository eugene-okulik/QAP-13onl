from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = Options()
chrome_options.add_argument('start-maximized')
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.amazon.com/')
# driver.maximize_window() Это он сам растягивает на весь экран
print(driver.current_url)
print(driver.title)
country = driver.find_element(By.ID, 'glow-ingress-line2')
print(country.text)
sleep(1)
