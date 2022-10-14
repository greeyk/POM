import sys

sys.path.append(sys.path[0] + "/...")

from selenium.webdriver.common.by import By
from Src.PageObject.Selectors import Locator

class ManageHotel(object):
    def __init__(self, driver):
        self.driver = driver

        # self.add_hotel = driver.find_element(By.CLASS_NAME, Locator.add_hotel)
        self.hotel_name = driver.find_element(By.XPATH, Locator.hotel_name)
        self.hotel_address = driver.find_element(By.XPATH, Locator.hotel_address)
        self.hotel_status = driver.find_element(By.XPATH, Locator.hotel_status)
        self.hotel_type = driver.find_element(By.XPATH, Locator.hotel_type)
        self.hotel_location = driver.find_element(By.XPATH, Locator.hotel_location)
        self.description_iframe = driver.find_element(By.XPATH, Locator.description_iframe)
        self.add_button = driver.find_element(By.XPATH, Locator.add_button)

    # def get_AddHotel(self):
    #     return self.add_hotel

    # def get_HotelElement1(self):
    #     return self.hotels1
    #
    # def get_ManageHotels(self):
    #     return self.manage_hotels