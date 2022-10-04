import sys
sys.path.append(sys.path[0] + "/...")

from Src.TestBase.WebDriverSetup import WebDriverSetup
from Src.PageObject.Pages.HomePage import Home
import unittest
from selenium import webdriver

class Booking_HomePage(WebDriverSetup):

    def test_HomePage(self):
        driver = self.driver
        self.driver.get("https://www.booking.com/")
        self.driver.set_page_load_timeout(30)

        web_page_title = "Booking.com | Oficjalna strona | Najlepsze hotele, loty, samochody na wynajem i zakwaterowanie"

        try:
            if driver.title == web_page_title:
                print("WebPage loaded successfully")
                self.assertEqual(driver.title, web_page_title)
        except Exception as error:
            print(error + "Webpage failed to load")

        home_page = Home(driver)

if __name__ == '__main__':
    unittest.main()