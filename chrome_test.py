import os
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys

chromedriver = "/Users/marin/AppData/Local/web_drivers/chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)


class WebDriverTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = driver

    '''def register(self):
        self.driver.get("http://integration.bgmenu.com")
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
    '''
    def addressSearch(self):
        self.driver.get('http://integration.bgmenu.com')
        address_field = self.driver.find_element_by_css_selector('#main-search > div > div.input-hold.neighbourhood > input')
        address_field.send_keys('Подуево 10')
        for:
            se
            selection_homepage = self.driver.find_element_by_xpath == ('//*[@id="ui-id-5"') or ('//*[@id="ui-id-4"')
        selection_homepage.send_keys(Keys.ARROW_DOWN)
        selection_homepage.send_keys(Keys.ENTER)


x = WebDriverTestCase()
x.setUp()
# x.register()
x.addressSearch()
