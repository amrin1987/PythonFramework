import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:
    pass

    def loggingTest(self):
        testName = inspect.stack()[1][3]
        logger = logging.getLogger(testName)
        fileHandler = logging.FileHandler("logs.log")
        fileformatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s    ")

        fileHandler.setFormatter(fileformatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger
    def explicitWait(self,driver,locatorValue):
        wait = WebDriverWait(driver, 10)
        wait.until(presence_of_element_located([By.CSS_SELECTOR, locatorValue]))

    def chooseFromDropdownWithValue(self,mywebElement,value):
        select = Select(mywebElement)
        select.select_by_visible_text(value)