from unittest.result import failfast

from pyexpat.errors import messages
from selenium.webdriver.common.by import *


from pageObject.CheckoutPage import CheckOutPage


class HomePage:
    def __init__(self,driver):
        self.driver = driver

    shop = (By.XPATH, "//a[contains(text(),'Shop')]")
    Name_textBox = (By.NAME,"name")
    Email_textbox = (By.NAME,"email")
    Password_textbox = (By.ID,"exampleInputPassword1")
    IceCream_Checkbox = (By.ID,"exampleCheck1")
    Gender_DropDown = (By.ID, "exampleFormControlSelect1")
    Radio_EmployementStatus = (By.XPATH, "//label[starts-with(@for,'inlineRadio')]")
    Birthday_textbox = (By.NAME,"bday")
    Submit_Button =(By.XPATH,"//*[@type='submit']")
    SucessMessage = (By.XPATH,"//*[@class='alert alert-success alert-dismissible']")
    message_expected  = "Success!"

    def shopItem(self):
         self.driver.find_element(*HomePage.shop).click()
         checkoutPage = CheckOutPage(self.driver)
         return checkoutPage

    def setName(self):
        return self.driver.find_element(*HomePage.Name_textBox)
    def setEmail(self):
        return self.driver.find_element(*HomePage.Email_textbox)
    def setPassword(self):
        return self.driver.find_element(*HomePage.Password_textbox)
    def setIceCream(self):
        return self.driver.find_element(*HomePage.IceCream_Checkbox)
    def setGender(self):
        return self.driver.find_element(*HomePage.Gender_DropDown)
    def getEmployementStatus(self):
        listOfElement= self.driver.find_elements(*HomePage.Radio_EmployementStatus)
        print (len(listOfElement))
        return listOfElement
    def setBirthday(self):
        return self.driver.find_element(*HomePage.Birthday_textbox)
    def clickSubmit(self):
        self.driver.find_element(*HomePage.Submit_Button).click()

    def setEmployementStatus(self,valueTesxt):
        orginalText=""
        for  element in self.getEmployementStatus() :
            orginalText=element.text
            if orginalText==valueTesxt:
                    element.click()
        else:
            assert failfast(method=self)
            self.driver.save_screenshot("TestCaseFailure.jpeg")
    def verifySucessMessage(self):
        assert (HomePage.message_expected in
                self.driver.find_element(*HomePage.SucessMessage).text)



