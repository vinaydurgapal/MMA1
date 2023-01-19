from selenium.webdriver.common.by import By


class ClubPage():


    lnk_avatar_linktext ='//div/div[7]/div[1]/img'
    lnk_logout_lnktext = "Sign Out"
    def __init__(self, driver):
        self.driver = driver

    def clickavatar(self):
        self.driver.find_element(By.XPATH, self.lnk_avatar_linktext).click()

    def clicklogout(self):
        self.driver.find_element(By.LINK_TEXT, self.lnk_logout_lnktext).click()


    def getconfirmationmsgs(self):
        try:
          return self.driver.find_element(By.XPATH,"/html/body/div/div/div/div/div/div/div/h1").text
        except:
          None

