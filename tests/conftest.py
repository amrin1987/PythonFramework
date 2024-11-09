import pytest
from selenium import webdriver
from selenium.webdriver.common.by import *


def pytest_addoption(parser):
    """Custom Pytest command line options"""
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    driver.maximize_window()

    driver.get("https://rahulshettyacademy.com/angularpractice/")

    request.cls.driver= driver
    yield
    driver.quit()
    #return driver