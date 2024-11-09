from selenium.webdriver.common.by import By


class ConfirmPage:

    Price_text = (By.CSS_SELECTOR,".text-right>h3>strong")
    Checkout_Button = (By.XPATH, "//*[contains(text(),'Checkout')]")
    Select_Country_dropdown = (By.ID,"country")
    selections = (By.CLASS_NAME,"suggestions")
    CheckBox =(By.XPATH, "//div[@class='checkbox checkbox-primary']")
    Submit_Button = (By.XPATH, "//*[@type='submit']")
    Alert_Message = (By.CLASS_NAME, "alert-success")

    def __init__(self,driver):
        self.driver = driver
    def priceCheck(self):
        return self.driver.find_element(*ConfirmPage.Price_text)
    def checkoutButton(self):
        return self.driver.find_element(*ConfirmPage.Checkout_Button)
    def select_country(self):
        return self.driver.find_element(*ConfirmPage.Select_Country_dropdown)
    def selection_from_dropdown(self):
        return self.driver.find_elements(*ConfirmPage.selections)
    def checkbox(self):
        return self.driver.find_element(*ConfirmPage.CheckBox)
    def submitButton(self):
        return self.driver.find_element(*ConfirmPage.Submit_Button)
    def alert_message(self):
        return self.driver.find_element(*ConfirmPage.Alert_Message)