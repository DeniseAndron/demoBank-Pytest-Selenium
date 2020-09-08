import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_LoginPage:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("***** Test_001_LoginPage *****")
        self.logger.info("***** Verifying Home Page Title *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        bnk_title = self.driver.title
        if bnk_title == 'GTPL Bank Home Page':
            assert True
            self.driver.close()
            self.logger.info("***** Home page title is passed *****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.info("***** Home page title is failed *****")
            assert False

    def test_login(self, setup):
        self.logger.info("***** Verify the login *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.Username(self.username)
        self.lp.Password(self.password)
        self.lp.LoginButton()

        #verify that the login was successful
        self.logger.info("***** Verify that the login was successful *****")
        bnk_title = self.driver.title
        if bnk_title == 'GTPL Bank Manager HomePage':
            assert True
            self.driver.close()
            self.logger.info("***** Login successfully *****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.info("***** Login failed *****")
            assert False
