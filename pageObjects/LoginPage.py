from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.common.by import By



class LoginPage():
    lnk_email = "email"
    lnk_password = "password"
    link_cont = '//*[@id="kt_sign_in_form"]/div[4]'
    account_exist= "//span[normalize-space()='Vinay durgapal']"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.NAME,self.lnk_email).send_keys(email)

    def setPassword(self, pwd):
        self.driver.find_element(By.NAME,self.lnk_password).send_keys(pwd)

    def clickLogin(self):
       self.double_click = self.driver.find_element(By.XPATH,self.link_cont)
       action = ActionChains(self.driver)
       # double click operation and perform
       action.double_click(self.double_click).perform()
    def isMyAccountPageExists(self):
        try:
            return self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div[1]/div[1]/div/h3').text
        except:
            None



