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


class WebDriverTestCase:
    def registrationtest(self):
        driver = webdriver.Chrome(chrome_options=options)
        self.driver = driver
        self.driver.get("http://integration.bgmenu.com")
        register_button = driver.find_element_by_css_selector("ul.user-nav.no-login>li>a")
        register_button.click()
        name_input = driver.find_element_by_css_selector("#fullname")
        name_input.send_keys("test user")
        email_input = driver.find_element_by_css_selector("#email")
        email_input.send_keys("random_email@gmail.com")
        pass_input = driver.find_element_by_css_selector("#password")
        pass_input.send_keys("password1")
        registration_submit = driver.find_element_by_css_selector("#submit-btn")
        registration_submit.click()

    def logintest(self):
        driver = webdriver.Chrome(chrome_options=options)
        self.driver = driver
        self.driver.get("http://integration.bgmenu.com")
        login_button = driver.find_element_by_css_selector("#user-nav > ul > li:nth-child(2) > a")
        login_button.click()
        email_input = driver.find_element_by_css_selector("#email")
        email_input.send_keys("m.ivanov@oliviera.ro")
        pass_input = driver.find_element_by_css_selector("#password")
        pass_input.send_keys("testtest")
        login_submit = driver.find_element_by_css_selector("#submit-btn")
        login_submit.click()

    def makeanordertest(self):
        driver = webdriver.Chrome(chrome_options=options)
        self.driver = driver
        self.driver.get("http://integration.bgmenu.com")
        login_button = driver.find_element_by_css_selector("#user-nav > ul > li:nth-child(2) > a")
        login_button.click()
        email_input = driver.find_element_by_css_selector("#email")
        email_input.send_keys("m.ivanov@oliviera.ro")
        pass_input = driver.find_element_by_css_selector("#password")
        pass_input.send_keys("testtest")
        login_submit = driver.find_element_by_css_selector("#submit-btn")
        login_submit.click()
        address_field = driver.find_element_by_css_selector(
            "#main-search > div > div.input-hold.neighbourhood > input")
        streets = "жк Гоце Делчев 15"
        address_field.send_keys(streets)
        sleep(2)
        address_field.send_keys(Keys.ARROW_DOWN)
        sleep(2)
        address_field.send_keys(Keys.ENTER)
        sleep(1)
        address_field.send_keys(Keys.ENTER)
        sleep(2)
        restaurant_choice = self.driver.find_element_by_css_selector(
            "#result-list > li:nth-child(1) > div.place-info > div.place-header-wrapper > a > h2")
        restaurant_choice.click()
        sleep(5)
        meal_add = self.driver.find_element_by_css_selector(
            "#meal-84564 > form > div.item-details > div.item-add-to-car > a")
        meal_add.click()
        sleep(3)
        order_input = driver.find_element_by_css_selector(
            "#container > section.page_content.clearfix > div:nth-child(4) > aside > div > section > a")
        order_input.click()
        sleep(3)
        address_selector = driver.find_element_by_css_selector("#address_id")
        order_submit = driver.find_element_by_css_selector(
            "#cart-detiles-cont > div.main-content-ordered > div.row > div.col-md-3 > a")
        driver.implicitly_wait(2)
        try:
            driver.find_element_by_css_selector(
                "#cart-detiles-cont > div:nth-child(2) > div > div > div.address-not-supported > span")
            address_selector.click()
            address_selector.send_keys(Keys.ARROW_DOWN)
            address_selector.send_keys(Keys.ENTER)
        except NoSuchElementException:
            order_submit.click()

            # Add try method for increased time error message
            # try:
            # self.driver.find_element_by_css_selector

    def addaddresstest(self):
        driver = webdriver.Chrome(chrome_options=options)
        self.driver = driver
        self.driver.get("http://integration.bgmenu.com")
        login_button = driver.find_element_by_css_selector("#user-nav > ul > li:nth-child(2) > a")
        login_button.click()
        email_input = driver.find_element_by_css_selector("#email")
        email_input.send_keys("m.ivanov@oliviera.ro")
        pass_input = driver.find_element_by_css_selector("#password")
        pass_input.send_keys("testtest")
        login_submit = driver.find_element_by_css_selector("#submit-btn")
        login_submit.click()
        sleep(3)
        side_bar = driver.find_element_by_css_selector("#user-menu > div.pull-left.user-name")
        side_bar.click()
        delivery_address = driver.find_element_by_css_selector("#user-menu-dd > ul > li:nth-child(3) > a")
        delivery_address.click()
        add_address = driver.find_element_by_css_selector(
            "#user-profil > div > div.col-md-8 > div > div.btn-submit.text-center > button")
        add_address.click()
        city_select = driver.find_element_by_css_selector("#city_id")
        city_select.click()
        city_select.send_keys(Keys.ARROW_DOWN)
        city_select.send_keys(Keys.ENTER)
        street_select = driver.find_element_by_css_selector("#street")
        street_select.send_keys("Бул България")
        num_select = driver.find_element_by_css_selector("#street_number")
        num_select.send_keys("111")
        save_address = driver.find_element_by_css_selector("#toggle-add-address > div > input")
        save_address.click()


x = WebDriverTestCase()
# x.registrationtest()
# x.logintest()
# x.makeanordertest()
x.addaddresstest()
