import sys
sys.path.append(sys.path[0] + "/...")

from Src.TestBase.WebDriverSetup import WebDriverSetup
from Src.Support.login import login_user
import unittest
from time import sleep

title = 'Dashboard'
username = 'supplier@phptravels.com'
password = 'demosupplier'


class PHPT_Login(WebDriverSetup):
    def test_Login(self):
        driver = self.driver
        self.driver.get("https://phptravels.net/api/supplier")
        self.driver.set_page_load_timeout(30)

        login_user(driver, username, password)

        try:
            if title == driver.title:
                print("User logged successfully")
        except Exception as error:
            print(error + "Login failed")

if __name__ == '__main__':
    unittest.main()