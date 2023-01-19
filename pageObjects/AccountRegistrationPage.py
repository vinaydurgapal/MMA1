import time

from selenium.webdriver.common.by import By


class AccountRegistrationPage():
    txt_email_name = "email"
    validation_text = "//span[normalize-space()='Invalid Email']"
    txt_firstname_name = "firstName"
    txt_last_name = "lastName"
    txt_screenName = "screenName"
    txt_password_name = "password"
    id_checkbox ="//input[@id='agree']"
    txt_continue='//*[@id="kt_sign_up_form"]/div[8]'

    # txt_confpassword_name = "confirm"
    # chk_policy_name = "agree"
    # btn_cont_xpath="//input[@value='Continue']"
    # text_msg_conf_xpath="//h1[normalize-space()='Your Account Has Been Created!']"

    def __init__(self, driver):
        self.driver = driver
        #self.implicitly_wait(10)

    def setEmail(self, email):
        self.driver.find_element(By.NAME, self.txt_email_name).send_keys(email)
        #text = self.driver.find_element(By.XPATH,self.validation_text).text
        #print(text)

    def setFirstName(self, fname):
        self.driver.find_element(By.NAME, self.txt_firstname_name).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.NAME, self.txt_last_name).send_keys(lname)

    def ScreenName(self, Sname):
        self.driver.find_element(By.NAME, self.txt_screenName).send_keys(Sname)

    def Setpassword(self, password):
        self.driver.find_element(By.NAME, self.txt_password_name).send_keys(password)

    def clickCheckbox(self):
        self.driver.find_element(By.XPATH, self.id_checkbox).click()
        # self.time.sleep(10)

    def clickContinue(self):
        self.driver.find_element(By.XPATH,self.txt_continue).click()
        time.sleep(10)

    #
    def getconfirmationmsg(self):
        try:
          return self.driver.find_element(By.XPATH,"//h3[normalize-space()='Personal Details']").text
        except:
          None