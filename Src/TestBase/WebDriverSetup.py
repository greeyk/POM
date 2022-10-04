import unittest
from selenium import webdriver
import time
from time import sleep
import warnings
import urllib3
from selenium.webdriver.chrome.service import Service



class WebDriverSetup(unittest.TestCase):
    def setUp(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        ser = Service('C:\SeleniumDrivers\chromedriver.exe')
        op = webdriver.ChromeOptions()
        op.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=ser, options=op)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        if (self.driver != None):
            print("Cleanup of test environment")
            self.driver.close()
            self.driver.quit()