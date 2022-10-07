import sys

from Src.PageObject.Pages.LoginPage import LoginUser

sys.path.append(sys.path[0] + "/...")

from selenium.webdriver.common.by import By
from Src.PageObject.Locators import Locator

class ManageHotel(object):
    def __init__(self, driver):
        self.driver = driver

        self.add_hotel = driver.find_element(By.CLASS_NAME, Locator.add_hotel)
        # self.hotels1 = driver.find_element(By.XPATH, Locator.login_password)
        # self.manage_hotels = driver.find_element(By.XPATH, Locator.manage_hotels)
        # self.login_captcha_iframe = driver.find_element(By.XPATH, Locator.login_captcha_iframe)

    def get_AddHotel(self):
        return self.add_hotel

    # def get_HotelElement1(self):
    #     return self.hotels1
    #
    # def get_ManageHotels(self):
    #     return self.manage_hotels