import sys


sys.path.append(sys.path[0] + "/...")

from Src.TestBase.WebDriverSetup import WebDriverSetup
from Test.Scripts.test_LoginPage import PHPT_Login, login_user
from Src.PageObject.Pages.ManageHotelsPage import ManageHotel
import unittest
from time import sleep

class PHPT_Hotel(WebDriverSetup):
    def test_Hotel(self):
        driver = self.driver
        self.driver.get("https://phptravels.net/api/supplier/hotels")
        self.driver.set_page_load_timeout(30)

        login_user(driver)

        manage = ManageHotel(driver)

        manage.add_hotel.click()

if __name__ == '__main__':
    unittest.main()