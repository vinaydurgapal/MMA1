from selenium.webdriver.common.by import By


class HomePage():

    lnk_signup_linktext = "Sign Up"
    lnk_login_linktext ="Log In"

    def __init__(self, driver):
        self.driver = driver

    def clickSignUp(self):
        self.driver.find_element(By.LINK_TEXT, self.lnk_signup_linktext).click()

    # def clickRegister(self):
    #     self.driver.find_element(By.LINK_TEXT,self.lnk_register_linktext).click()
    #
    def clickLogin(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_login_linktext).click()
