from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com/'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Open page')
    def open_page(self):
        self.driver.get(f'{self.base_url}{self.page_url}')

    def find(self, locator):
        WebDriverWait(self.driver, 5).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), 'welcome')
        )
        return self.driver.find_element(*locator)

    def finds(self, locator):
        WebDriverWait(self.driver, 5).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), 'Default welcome msg!')
        )
        return self.driver.find_elements(*locator)

    def find_log_in(self, locator):
        WebDriverWait(self.driver, 5).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), 'Welcome')
        )
        return self.driver.find_element(*locator)

    def find_window_alert(self, locator):
        WebDriverWait(self.driver, 5).until(
            EC.text_to_be_present_in_element(
                (By.ID, 'modal-content-15'),
                'Are you sure you want to remove all items from your Compare Products list?')
        )
        return self.driver.find_element(*locator)

    def find_message_compare(self, locator):
        WebDriverWait(self.driver, 5).until(
            EC.text_to_be_present_in_element(
                (By.XPATH, '//*[@id="maincontent"]/div[4]/div[3]/div[1]/div[1]/span'), '1 item')
        )
        return self.driver.find_element(*locator)

    @allure.step('Scroll page down')
    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
