import sys
from time import sleep

from selenium.webdriver.common.by import By

sys.path.append(sys.path[0] + "/...")

from Src.TestBase.WebDriverSetup import WebDriverSetup
from Test.Scripts.test_LoginPage import PHPT_Login, login_user
from Src.PageObject.Pages.ManageHotelsPage import ManageHotel
import unittest

username = 'supplier@phptravels.com'
password = 'demosupplier'


class PHPT_Hotel(WebDriverSetup):
    def test_AddHotel(self):
        driver = self.driver
        self.driver.get("https://phptravels.net/api/supplier/hotels/add")
        self.driver.set_page_load_timeout(30)

        login_user(driver, username, password)

        manage = ManageHotel(driver)

        manage.hotel_name.send_keys('The Central Park North')
        manage.hotel_address.send_keys('137 W 111th St, New York, NY 10026, United States')
        manage.hotel_status.click()
        manage.hotel_location.click()

        elem = driver.find_element(By.XPATH, '//*[@id="select2-drop"]/div/input')
        elem.send_keys('New York')
        sleep(1)
        driver.find_element(By.XPATH, '//*[@id="select2-drop"]/ul/li/div').click()

        iframe = manage.description_iframe
        driver.switch_to.frame(iframe)
        driver.find_element(By.XPATH, '/html/body/p').send_keys('opis')

        driver.switch_to.default_content()

if __name__ == '__main__':
    unittest.main()