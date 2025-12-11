import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

"""Фикстура для инициализации и закрытия драйвера"""
@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    yield driver
    driver.quit()