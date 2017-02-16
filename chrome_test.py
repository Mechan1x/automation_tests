import os
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from time import sleep
import random

chromedriver = "/Users/Marin/AppData/Local/web_drivers/chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")


class WebDriverTestCase(unittest.TestCase):
    def registrationTest(self):
        driver = webdriver.Chrome(chrome_options=options)
        self.driver = driver
        self.driver.get("https://integration.bgmenu.com")
        register_button = self.driver.find_element_by_css_selector('ul.user-nav.no-login>li>a')
        register_button.click()
        name_input = self.driver.find_element_by_css_selector('#fullname')
        name_input.send_keys('test user')
        email_input = self.driver.find_element_by_css_selector('#email')
        email_input.send_keys('random_email@gmail.com')
        pass_input = self.driver.find_element_by_css_selector('#password')
        pass_input.send_keys('password1')
        registration_submit = self.driver.find_element_by_css_selector('#submit-btn')
        registration_submit.click()

    def makeAnOrderTest(self):
        driver = webdriver.Chrome(chrome_options=options)
        self.driver = driver
        self.driver.get('http://integration.bgmenu.com')
        address_field = self.driver.find_element_by_css_selector(
            '#main-search > div > div.input-hold.neighbourhood > input')
        streets = ['жк Гоце Делчев 15', 'жк Белите Брези 1', 'Младост 104', 'жк Овча Купел 1']
        address_field.send_keys(random.choice(streets))
        sleep(2)
        address_field.send_keys(Keys.ARROW_DOWN)
        sleep(2)
        address_field.send_keys(Keys.ENTER)
        sleep(1)
        address_field.send_keys(Keys.ENTER)


x = WebDriverTestCase()
x.registrationTest()
x.makeAnOrderTest()
