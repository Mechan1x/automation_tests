import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import random

chromedriver = "/Users/Mechan1x/AppData/Local/web_drivers/chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")


class HhManagerAutomation:
    def driver_ini(self):
        driver = webdriver.Chrome(chrome_options=options)
        self.driver = driver
        self.driver.get("http://integration.bgmenu.com/hhmanager/")

    def log_in(self):
        email_front = self.driver.find_element_by_css_selector("#email")
        email_front.send_keys("m.ivanov@oliviera.ro")
        pass_front = self.driver.find_element_by_css_selector("#password")
        pass_front.send_keys("testtest")
        login = self.driver.find_element_by_css_selector(
            "body > div.container-fluid > div > div.fluid-row > div > form > div.form-actions > button")
        login.click()

    def sidebar_actions(self):
        open_sidebar = self.driver.find_element_by_css_selector("#toggle_button")
        open_sidebar.click()
        sidebar_mail = self.driver.find_element_by_css_selector("#email")
        sidebar_mail.send_keys("m.ivanov@oliviera.ro")
        make_search = self.driver.find_element_by_css_selector("#slide_cont > form > div.form-actions > button")
        make_search.click()

    def order_status_change(self):
        order_status_waiting = self.driver.find_element_by_css_selector("#status-141491")
        if order_status_waiting is True:

    # status-141472


web = HhManagerAutomation
web.driver_ini(web)
web.log_in(web)
