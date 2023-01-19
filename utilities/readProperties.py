import configparser
import os


config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+'\\configurations\\config.ini')


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('commonInfo','baseURL')
        return url

    @staticmethod
    def getPassword():
        pwd = config.get('commonInfo','password')
        return pwd

    @staticmethod
    def getFirstName():
        fname = config.get('commonInfo','fname')
        return fname
    @staticmethod
    def getLastName():
        lname = config.get('commonInfo','lname')
        return lname

    @staticmethod
    def getUseremail():
        email = config.get('commonInfo', 'email')
        return email

    @staticmethod
    def getPassword():
        login_password = config.get('commonInfo', 'login_password')
        return login_password

