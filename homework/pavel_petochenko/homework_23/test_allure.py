import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure


@allure.feature("Page Title")
class TestPageTitle:
    @pytest.fixture
    def driver(self):
        driver_chrome = webdriver.Chrome()
        driver_chrome.maximize_window()
        return driver_chrome

    @allure.story("Verify page title")
    def test_page_title(self, driver):
        driver.get("https://magento.softwaretestingboard.com/customer/account/create/")
        actual_title = driver.title
        expected_title = "Create New Customer Account"
        with allure.step("Verify page title"):
            assert actual_title == expected_title

    @allure.story("Verify required fields")
    def test_required_fields(self, driver):
        driver.get("https://magento.softwaretestingboard.com/customer/account/create/")
        required_fields = driver.find_elements(By.CSS_SELECTOR, '.required')
        with allure.step("Verify required fields"):
            assert len(required_fields) > 0

    @allure.story("Verify firstname and lastname fields")
    def test_firstname_lastname(self, driver):
        driver.get("https://magento.softwaretestingboard.com/customer/account/create/")
        firstname_elements = driver.find_elements(By.ID, "firstname")
        with allure.step("Verify firstname fields"):
            assert len(firstname_elements) > 0
        lastname_elements = driver.find_elements(By.ID, "lastname")
        with allure.step("Verify lastname fields"):
            assert len(lastname_elements) > 0


@allure.feature("Product Page")
class TestProductPage:
    @pytest.fixture
    def driver(self):
        driver_chrome = webdriver.Chrome()
        driver_chrome.maximize_window()
        return driver_chrome

    @allure.story("Verify page title")
    def test_page_title_2(self, driver):
        driver.get("https://magento.softwaretestingboard.com/collections/eco-friendly.html")
        expected_title = "Eco Friendly"
        with allure.step("Verify page title"):
            assert driver.title == expected_title

    @allure.story("Verify product count")
    def test_product_count(self, driver):
        driver.get("https://magento.softwaretestingboard.com/collections/eco-friendly.html")
        product_elements = driver.find_elements(By.CSS_SELECTOR, ".product-item")
        expected_product_count = 14
        with allure.step("Verify product count"):
            assert len(product_elements) == expected_product_count

    @allure.story("Verify opening product page")
    def test_open_product_page(self, driver):
        driver.get("https://magento.softwaretestingboard.com/collections/eco-friendly.html")
        product_link = driver.find_element(By.LINK_TEXT, "Ana Running Short")
        with allure.step("Click on product link"):
            product_link.click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.url_to_be("https://magento.softwaretestingboard.com/ana-running-short.html"))
        with allure.step("Verify product page URL"):
            assert driver.current_url == "https://magento.softwaretestingboard.com/ana-running-short.html"


@allure.feature("Element Presence")
class TestElementPresence:
    @pytest.fixture
    def driver(self):
        driver_chrome = webdriver.Chrome()
        driver_chrome.maximize_window()
        return driver_chrome

    @allure.story("Verify element presence")
    def test_element_presence(self, driver):
        driver.get("https://magento.softwaretestingboard.com/sale.html")
        element = driver.find_element(By.XPATH, '//*[@id="maincontent"]/div[4]/div[1]/div[1]/div/a/span/span[2]')
        with allure.step("Verify element presence"):
            assert element.is_displayed()

    @allure.story("Verify navigation to women deals")
    def test_navigation_to_women_deals(self, driver):
        driver.get("https://magento.softwaretestingboard.com/sale.html")
        women_deals_link_locator = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[1]/div[1]/div/a/span/span[2]')
        women_deals_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(women_deals_link_locator))
        with allure.step("Click on women deals link"):
            women_deals_link.click()
        expected_url = "https://magento.softwaretestingboard.com/promotions/women-sale.html"
        with allure.step("Verify current URL"):
            assert driver.current_url == expected_url
