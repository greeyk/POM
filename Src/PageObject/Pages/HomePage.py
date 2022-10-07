import sys

sys.path.append(sys.path[0] + "/...")

from selenium.webdriver.common.by import By
from Src.PageObject.Locators import Locator

class Home(object):
    def __init__(self, driver):
        self.driver = driver
        self.login = driver.find_element(By.XPATH, Locator.home_login)
        self.signup = driver.find_element(By.XPATH, Locator.home_signup)

    def getLogin(self):
        return self.login

    def getSignup(self):
        return self.signup
