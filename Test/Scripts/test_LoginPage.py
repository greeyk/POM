import sys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

sys.path.append(sys.path[0] + "/...")

from Src.TestBase.WebDriverSetup import WebDriverSetup
from Src.PageObject.Pages.LoginPage import LoginUser, LoginIframe
import unittest
from time import sleep

username = 'hcokury6725@kenvanharen.com'
password = 'testing1234'

title = 'Client Area - PHPTRAVELS'

class PHPT_Login(WebDriverSetup):
    def test_Login(self):
        driver = self.driver
        self.driver.get("https://phptravels.org/login")
        self.driver.set_page_load_timeout(30)

        login = LoginUser(driver)

        login.login_user_name.send_keys(username)
        sleep(1)
        login.login_password.send_keys(password)
        sleep(1)

        driver.switch_to.frame(login.login_captcha_iframe)

        iframe = LoginIframe(driver)
        iframe.login_captcha.click()

        driver.switch_to.default_content()
        sleep(1)

        login.login_button.click()


        try:
            if title == driver.title:
                print("User logged successfully")
        except Exception as error:
            print(error + "Login failed")

if __name__ == '__main__':
    unittest.main()