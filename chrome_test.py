import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import random
import logging

chromedriver = "C:/Users/User_/webdrivers/chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option('prefs', {
    'credentials_enable_service': False,
    'profile': {
        'password_manager_enabled': False
    }
})

LOG_FILENAME = "test_results.log"
logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)


class BasicTestCases:
    def driver_ini(self):
        driver = webdriver.Chrome(chrome_options=options)
        self.driver = driver
        self.driver.get("https://ihdev3.imperialhero.org/ihv2/public/")

    def chat_test(self):
        for i in range(0, 3):
            usernames = ["marinski.tester", "mtest1", "mtest2"]
            username_input = self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[3]/div/div[2]/div[2]/form/input[1]")
            username_input.send_keys(random.choice(usernames))
            pass_input = self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[2]/div[2]/form/input[2]")
            pass_input.send_keys("testtest123")
            login_submit = self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[2]/div[2]/form/button")
            login_submit.click()
            sleep(8)
            for x in range(0, 3):
                input_selector = self.driver.find_element_by_css_selector("#chat-message-input")
                input_selector.send_keys("test_script_chrome")
                chat_message_submit = self.driver.find_element_by_css_selector("#chat-message-input")
                chat_message_submit.send_keys(Keys.ENTER)
            driver = webdriver.Chrome(chrome_options=options)
            self.driver = driver
            self.driver.get("https://ihdev3.imperialhero.org/ihv2/public/")
            sleep(4)

    def teardown(self):
        self.driver.quit()

web = BasicTestCases
web.driver_ini(web)
web.chat_test(web)
web.teardown(web)
