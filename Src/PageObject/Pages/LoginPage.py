import sys

sys.path.append(sys.path[0] + "/...")

from selenium.webdriver.common.by import By
from Src.PageObject.Locators import Locator

class LoginUser(object):
    def __init__(self, driver):
        self.driver = driver

        self.login_user_name = driver.find_element(By.XPATH, Locator.login_user_name)
        self.login_password = driver.find_element(By.XPATH, Locator.login_password)
        self.login_button = driver.find_element(By.XPATH, Locator.login_button)

    def get_Username(self):
        return self.login_user_name

    def get_Password(self):
        return self.login_password

    def get_LoginButton(self):
        return self.login_button

