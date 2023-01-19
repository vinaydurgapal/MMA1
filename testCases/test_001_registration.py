import os
import time

import pytest
from selenium.webdriver.common.by import By

from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilities import randomeString
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig

@pytest.mark.sanity
class Test_001_AccountReg:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    def test_account_reg(self, setup):
        self.logger.info("**************************************************Test Case 001  STarted ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("open web page----------------------------------------------------")
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickSignUp()

        self.regpage = AccountRegistrationPage(self.driver)
        self.logger.info("register=======================================================")
        self.email = randomeString.random_string_generator() + '@gmail.com'
        self.regpage.setEmail(self.email)

        self.regpage.setFirstName(ReadConfig.getFirstName())



        self.regpage.setLastName(ReadConfig.getLastName())
        self.screename = randomeString.screenname_genrator()
        self.regpage.ScreenName(self.screename)
        self.regpage.Setpassword(ReadConfig.getPassword())
        self.regpage.clickCheckbox()
        self.regpage.clickContinue()
        time.sleep(5)

        # self.regpage.setConfirmPassword("abcxyz")
        # self.regpage.setPrivacyPolicy()
        # self.regpage.clickContinue()
        self.confmsg=self.regpage.getconfirmationmsg()
        # self.driver.close()
        if self.confmsg=="Personal Details":
            print("hogya")
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "//screenshots//" + "test_account_reg.png")

        else:
            print("fail")
            # Flag = self.driver.find_element(By.NAME,'email')
            # self.driver.execute_script("arguments[0].scrollIntoView();",Flag)
            self.driver.save_screenshot(os.path.abspath(os.curdir)+ "//screenshots//" + "test_page.png")
        self.logger.info("**************************************************Test Case 001  STarted ")



