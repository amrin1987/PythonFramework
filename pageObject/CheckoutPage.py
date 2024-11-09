from selenium.webdriver.common.by import By

from pageObject.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self,driver):
        self.driver = driver

    productsAvailable = (By.XPATH,"//app-card[@class='col-lg-3 col-md-6 mb-3']")
    checkoutButton = (By.XPATH, "//*[contains(text(),'Checkout')]")

    def productavailability(self):
        return self.driver.find_elements(*CheckOutPage.productsAvailable)
    def findcCheckoutButton (self):
         self.driver.find_element(*CheckOutPage.checkoutButton).click()
         confirmPage = ConfirmPage(self.driver)
         return confirmPage