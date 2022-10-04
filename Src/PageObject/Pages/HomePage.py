import sys

sys.path.append(sys.path[0] + "/...")

from selenium.webdriver.common.by import By
from Src.PageObject.Locators import Locator

class Home(object):
    def __init__(self, driver):
        self.driver = driver
        self.book_decline_cookies = driver.find_element(By.XPATH, Locator.book_decline_cookies)
        self.book_login = driver.find_element(By.XPATH, Locator.book_login)
        self.book_signup = driver.find_element(By.XPATH, Locator.book_signup)

    def getLogin(self):
        return self.book_login

    def getSignup(self):
        return self.book_signup

    def declineCookies(self):
        return self.book_decline_cookies