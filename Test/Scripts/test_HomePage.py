import sys
sys.path.append(sys.path[0] + "/...")

from Src.TestBase.WebDriverSetup import WebDriverSetup
from Src.PageObject.Pages.HomePage import Home
import unittest

class PHPT_HomePage(WebDriverSetup):

    def test_HomePage(self):
        driver = self.driver
        self.driver.get("https://phptravels.net/")
        self.driver.set_page_load_timeout(30)

        web_page_title = "PHPTRAVELS | Travel Technology Partner - PHPTRAVELS"

        try:
            if driver.title == web_page_title:
                print("WebPage loaded successfully")
                self.assertEqual(driver.title, web_page_title)
        except Exception as error:
            print(error + "Webpage failed to load")

        home_page = Home(driver)

if __name__ == '__main__':
    unittest.main()