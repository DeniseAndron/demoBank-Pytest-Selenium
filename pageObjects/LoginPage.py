from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.MainPageObjects import MainPage

class LoginPage(MainPage):
    #locators
    username = (By.NAME, 'uid')
    password = (By.NAME, 'password')
    login_button = (By.NAME, 'btnLogin')

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def Username(self, usernameId):
        self.enter_text(self.username, usernameId)

    def Password(self, passwordId):
        self.enter_text(self.password, passwordId)

    def LoginButton(self):
        self.click(self.login_button)
