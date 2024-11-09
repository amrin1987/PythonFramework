from venv import logger

from selenium import webdriver
from selenium.webdriver.common.by import *
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from Utility.BaseClass import BaseClass
from pageObject.CheckoutPage import CheckOutPage
from pageObject.ConfirmPage import ConfirmPage
from pageObject.HomePage import HomePage


class Test_e2e(BaseClass):
    CountryName="United States of America"
    message = " Thank you! "

    def test_e2e(self):
            driver = self.driver

            driver.implicitly_wait(4)
            #driver.find_element(By.XPATH, "//a[contains(text(),'Shop')]").click()
            homepage = HomePage(driver)
            checkoutPage = homepage.shopItem()
            productsAvailable = CheckOutPage(driver).productavailability()
            assert len(productsAvailable) ==4
            #logger = BaseClass.loggingTest(self)
            log = self.loggingTest()
            log.info("4 products available")
            for product in productsAvailable:
                    title = product.find_element(By.CSS_SELECTOR,".card-title > a").text
                    if title == "Blackberry":
                            product.find_element(By.XPATH,"//*[contains(text(),'Add')]").click()
            log.info("Blackberry selected")
            confirmPage=checkoutPage.findcCheckoutButton()
            driver.implicitly_wait(40)
            #Confirm pages activity

            price =  confirmPage.priceCheck().text.replace("₹. ","")
            assert int(price) == 100000

            confirmPage.checkoutButton().click()
            confirmPage.select_country().send_keys("United S")

            for country in confirmPage.selection_from_dropdown():
                self.explicitWait(country, "ul>li")

                if country.find_element(By.CSS_SELECTOR,"ul>li").text == Test_e2e.CountryName:
                           country.click()
            driver.implicitly_wait(40)
            confirmPage.checkbox().click()
            confirmPage.submitButton().click()

            #alert alert-success alert-dismissible
            assert Test_e2e.message in confirmPage.alert_message().text
