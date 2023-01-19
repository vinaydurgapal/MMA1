import time

import pytest

from pageObjects.ClubPage import ClubPage
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

import os
@pytest.mark.regression
class Test_Login():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # Logger

    user = ReadConfig.getUseremail()
    password = ReadConfig.getPassword() #this time time we do not need data from common file to login because we are using Excel file / for data driver test

   # path = os.path.abspath((os.curdir)+"\\testdata\\Opencart_LoginDta.xlsx")

    def test_login(self,setup):
        self.logger.info("******* Starting test_002_login **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)

        self.hp.clickLogin()

        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.user)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(10)

        self.targetpage=self.lp.isMyAccountPageExists()
        #print("ededdddddddddddddddddddd",self.targetpage)
        #
        if self.targetpage=="Vinay durgapal":

            print("pass")
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_login.png")
            print("fail")


        self.cp = ClubPage(self.driver)
        self.cp.clickavatar()
        self.cp.clicklogout()

        self.gettext=self.cp.getconfirmationmsgs()
        if self.gettext=='Login':
            print("logout successfully done")
        else:
            print('logout fail')
        #
        # self.driver.close()
        # self.logger.info("******* End of test_002_login **********")

