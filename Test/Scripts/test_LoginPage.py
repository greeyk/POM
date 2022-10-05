import sys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

sys.path.append(sys.path[0] + "/...")

from Src.TestBase.WebDriverSetup import WebDriverSetup
from Src.PageObject.Pages.HomePage import Home
from Src.PageObject.Pages.LoginPage import LoginUser, LoginPassword
import unittest
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

username = 'hcokury6725@kenvanharen.com'
password = 'Testing1234'

check_list = ['Twoje konto', 'Your account']

class Booking_Login(WebDriverSetup):
    def test_Login(self):
        driver = self.driver
        self.driver.get("https://www.booking.com/")
        self.driver.set_page_load_timeout(30)

        home = Home(driver)

        home.book_decline_cookies.click()
        home.book_login.click()

        login = LoginUser(driver)

        login.book_login_user_name.send_keys(username)
        sleep(2)
        login.book_login_user_button.click()
        sleep(2)

        login = LoginPassword(driver)

        login.book_login_password.send_keys(password)
        sleep(2)
        login.book_login_password_button.click()
        sleep(2)


        try:
            # check_status = driver.find_element(By.XPATH, '//*[@id="profile-menu-trigger--title"]').getText()
            if driver.find_element(By.XPATH, '//*[@id="profile-menu-trigger--title"]').getText() in check_list:
                print("User logged successfully")
        except Exception as error:
            print(error + "Login failed")



if __name__ == '__main__':
    unittest.main()
