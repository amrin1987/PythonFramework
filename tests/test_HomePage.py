
import pytest

from TestData.HomePageData import HomePageData
from Utility.BaseClass import BaseClass
from pageObject.HomePage import HomePage
from selenium import webdriver


class Test_HomePage(BaseClass):
     def test_fillupForm(self,getdata):
            driver = self.driver
            logger = self.loggingTest()
            homepage = HomePage(driver)
            #logger.info("first name is " + getdata[0])
            homepage.setName().send_keys(getdata["firstname"])
            #confirmPage.select_country().send_keys("United S")
            homepage.setEmail().send_keys(getdata["lastname"])
            homepage.setPassword().send_keys("y")
            homepage.setIceCream().click()
            self.chooseFromDropdownWithValue(homepage.setGender(),getdata["gender"])
            try:
                homepage.setEmployementStatus("Employed")
            except:
                logger.warn("Employe is not available ")
            homepage.setBirthday().send_keys("05/11/1987")
           # homepage.setEmail().send_keys( "y")
            homepage.clickSubmit()
            homepage.verifySucessMessage()
            self.driver.refresh()
     @pytest.fixture(params=HomePageData.fileRead_Panda())
     def getdata(self,request):
            return request.param

