from selenium import webdriver
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    yield chrome_driver
