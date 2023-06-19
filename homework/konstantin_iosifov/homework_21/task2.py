from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://demoqa.com/menu#")
driver.maximize_window()

main_item2 = driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/a')
sub_sub_list = driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/ul/li[3]/a')
sub_sub_item2 = driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/ul/li[3]/ul/li[2]/a')
ActionChains(driver).move_to_element(main_item2).move_to_element(sub_sub_list).click(sub_sub_item2).perform()

driver.quit()
