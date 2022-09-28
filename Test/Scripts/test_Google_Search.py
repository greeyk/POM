import sys
sys.path.append(sys.path[0] + "/...")

from Src.TestBase.WebDriverSetup import WebDriverSetup
from Src.PageObject.Pages.HomePage import Home
import unittest
from time import sleep

class Google_Search(WebDriverSetup):
    def test_GoogleSearch(self):
        driver = self.driver
        self.driver.get("https://www.google.com/")
        self.driver.set_page_load_timeout(30)

        home = Home(driver)

        home.decline_cookies.click()
        home.search_text.send_keys("LambdaTest")
        sleep(5)
        home.search_text.submit()
        sleep(5)

if __name__ == '__main__':
    unittest.main()