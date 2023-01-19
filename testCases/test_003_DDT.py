import time
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.ClubPage import ClubPage
from utilities import XLUtils
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import os

class Test_Login_DDT():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # Logger

    path = os.path.abspath(os.curdir)+"\\testdata\\Opencart_LoginData.xlsx"

    def test_login_ddt(self,setup):
        self.logger.info("**** Starting test_003_login_Datadriven *******")
        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        lst_status=[]

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)  # HomePage Page Object Class
        self.lp = LoginPage(self.driver)  # LoginPage Page Object Class
        self.cp = ClubPage(self.driver)  # MyAccount Page Object class

        for r in range(2,self.rows+1):
            self.hp.clickLogin()
            self.lp.clickLogin()

            self.email=XLUtils.readData(self.path,"Sheet1",r,1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)
            self.lp.setEmail(self.email)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()

            time.sleep(10)
            self.targetpage=self.lp.isMyAccountPageExists()

            if self.exp=='Valid':
                print(self.exp)
                if self.targetpage=="My Bio":
                    lst_status.append('Pass')
                    XLUtils.writeData(os.path.abspath(os.curdir)+"\\testdata\\Opencart_LoginData.xlsx", "Sheet1", r, 4, "passed")
                    self.cp.clickavatar()
                    self.cp.clicklogout()
                else:
                    lst_status.append('Fail')
            elif self.exp=='Invalid':
                #self.driver.refresh()
                if self.targetpage != "My Bio":
                    lst_status.append('Fail')
                    XLUtils.writeData(os.path.abspath(os.curdir) + "\\testdata\\Opencart_LoginData.xlsx", "Sheet1",
                                           r, 4, "fail")
                    self.driver.refresh()
                    # self.cp.clickavatar()
                    # self.cp.clicklogout()
                else:
                    lst_status.append('Pass')
        self.driver.close()
        print(lst_status)
        #final validation
        # if "Fail" not in lst_status:
        #     assert True
        # else:
        #     assert False
        self.logger.info("******* End of test_003_login_Datadriven **********")
