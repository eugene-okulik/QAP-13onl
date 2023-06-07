import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime


class TestGuestFormPage(unittest.TestCase):
    driver = None

    def setUp(self) -> None:
        print('before test')
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self) -> None:
        print('after test')
        self.driver.quit()

    @unittest.skipIf(datetime.now().weekday() == 0, 'Not working on mondays')
    def test_dropdown(self):
        print('in test')
        self.driver.get('https://www.google.com/')
        search = self.driver.find_element(By.NAME, 'q')
        self.assertTrue(search.is_displayed())

    @unittest.skip('Bug #345')
    def test_cookies_test(self):
        print('in test')
        self.driver.get('https://magento.softwaretestingboard.com/sales/guest/form/')
        button = self.driver.find_element(By.NAME, 'btnI')
        self.assertTrue(button.is_displayed())

    def test_one(self):
        summ = 1 + 2
        self.assertEqual(summ, 3)

    def test_two(self):
        summ = 2 + 3
        self.assertEqual(summ, 4)
