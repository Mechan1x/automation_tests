from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from urllib.request import urlopen
import unittest
import time
import re

firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("general.useragent.override", "Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0")

firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
firefox_capabilities['binary'] = r'C:\Program Files (x86)\Mozilla Firefox\Firefox.exe'

binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\Firefox.exe')

driver = webdriver.Firefox(firefox_binary=binary, firefox_profile=firefox_profile, capabilities=firefox_capabilities)


class WebDriverTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox


class HomePageSearch(WebDriverTestCase):

    def test_homepage_search(self):
        self.driver.get("http://integration.bgmenu.com")


if __name__ == '__main__':
    unittest.main()
