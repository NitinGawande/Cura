from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import pytest


@pytest.fixture()
def setup():
    driver=webdriver.Chrome()
    wait = WebDriverWait(driver, 5)
    return driver,wait



