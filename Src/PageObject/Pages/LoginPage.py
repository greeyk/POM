import sys

sys.path.append(sys.path[0] + "/...")

from selenium.webdriver.common.by import By
from Src.PageObject.Locators import Locator

class LoginUser(object):
    def __init__(self, driver):
        self.driver = driver

        self.book_login_user_name = driver.find_element(By.XPATH, Locator.book_login_user_name)
        self.book_login_user_button = driver.find_element(By.XPATH, Locator.book_login_user_button)


    def get_Username(self):
        return self.book_login_user_name

    def get_UsernameButton(self):
        return self.book_login_user_button


class LoginPassword(object):
    def __init__(self, driver):
        self.driver = driver

        self.book_login_password = driver.find_element(By.XPATH, Locator.book_login_password)
        self.book_login_password_button = driver.find_element(By.XPATH, Locator.book_login_password_button)

    def get_Password(self):
            return self.book_login_password

    def get_PasswordButton(self):
            return self.book_login_password_button
