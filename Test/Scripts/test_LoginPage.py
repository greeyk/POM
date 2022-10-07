import sys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

sys.path.append(sys.path[0] + "/...")

from Src.TestBase.WebDriverSetup import WebDriverSetup
from Src.PageObject.Pages.LoginPage import LoginUser
import unittest
from time import sleep

username = 'supplier@phptravels.com'
password = 'demosupplier'

title = 'Dashboard'


class PHPT_Login(WebDriverSetup):
    def test_Login(self):
        driver = self.driver
        self.driver.get("https://phptravels.net/api/supplier")
        self.driver.set_page_load_timeout(30)

        login_user(driver)

        try:
            if title == driver.title:
                print("User logged successfully")
        except Exception as error:
            print(error + "Login failed")

def login_user(driver):
    login = LoginUser(driver)

    login.login_user_name.send_keys(username)
    sleep(1)
    login.login_password.send_keys(password)
    sleep(1)
    login.login_button.click()
    sleep(5)

if __name__ == '__main__':
    unittest.main()