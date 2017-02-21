from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import random

firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("general.useragent.override",
                               "Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0")

firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
firefox_capabilities['binary'] = r"C:\Program Files (x86)\Mozilla Firefox\Firefox.exe"

binary = FirefoxBinary(r"C:\Program Files (x86)\Mozilla Firefox\Firefox.exe")


class BasicTestCases:
    def driver_ini(self):
        driver = webdriver.Firefox()
        self.driver = driver
        driver.maximize_window()
        self.driver.get('https://bgmenu.com')

    def login_test(self):
        login_button = self.driver.find_element_by_css_selector("#user-nav > ul > li:nth-child(2) > a")
        login_button.click()
        sleep(2)
        email_input = self.driver.find_element_by_css_selector("#email")
        email_input.send_keys("m.ivanov@oliviera.ro")
        pass_input = self.driver.find_element_by_css_selector("#password")
        pass_input.send_keys("testtest")
        login_submit = self.driver.find_element_by_css_selector("#submit-btn")
        login_submit.click()

    def make_order_test(self):
        for i in range(3):
            address_field = self.driver.find_element_by_css_selector(
                "#main-search > div > div.input-hold.neighbourhood > input")
            address_field.clear()
            streets = "Бул България 111"
            address_field.send_keys(streets)
            sleep(2)
            address_field.send_keys(Keys.ARROW_DOWN)
            sleep(2)
            address_field.send_keys(Keys.ENTER)
            sleep(2)
            address_field.send_keys(Keys.ENTER)
            sleep(2)
            search_restaurant = self.driver.find_element_by_css_selector("#search")
            search_restaurant.send_keys("Annette")
            search_restaurant.send_keys(Keys.ENTER)
            selected_restaurant = self.driver.find_element_by_css_selector(
                "#result-list > li > div.place-info > div.place-header-wrapper > a > h2")
            selected_restaurant.click()
            meal_add = self.driver.find_element_by_css_selector(
                "#meal-2242 > form > div.item-details > div.item-add-to-car > a")
            meal_add.click()
            sleep(4)

            try:
                continue_order = self.driver.find_element_by_css_selector(
                    "#general_popup_content > div.text-center > a.green_btn.continue-add-to-cart")
                continue_order.click()
                sleep(3)
                meal_add.click()
                meal_add.click()
            except NoSuchElementException:
                sleep(2)
                meal_add.click()
                meal_add.click()

            sleep(3)
            order_input = self.driver.find_element_by_css_selector(
                "#container > section.page_content.clearfix > div:nth-child(4) > aside > div > section > a")
            order_input.click()
            sleep(3)
            address_selector = self.driver.find_element_by_css_selector("#address_id")
            sleep(3)

            try:
                self.driver.find_element_by_css_selector(
                    "#cart-detiles-cont > div:nth-child(2) > div > div > div.address-not-supported > span")
                address_selector.click()
                address_selector.send_keys(Keys.ARROW_DOWN)
                address_selector.send_keys(Keys.ENTER)
                sleep(3)
                add_comment = self.driver.find_element_by_css_selector(
                    "#cart-detiles-cont > div.main-content-ordered > div:nth-child(2) > div.leave-comment > label > span")
                add_comment.click()
                comment_field = self.driver.find_element_by_css_selector("#order-comment")
                comment_field.clear()
                comment_field.send_keys("BGMENU ТЕСТ! НЕ ПРИГОТВЯЙТЕ!")
                order_submit = self.driver.find_element_by_css_selector(
                    "#cart-detiles-cont > div.main-content-ordered > div.row > div.col-md-3 > a")
                order_submit.click()
            except NoSuchElementException:
                sleep(3)
                add_comment = self.driver.find_element_by_css_selector(
                    "#cart-detiles-cont > div.main-content-ordered > div:nth-child(2) > div.leave-comment > label > span")
                add_comment.click()
                comment_field = self.driver.find_element_by_css_selector("#order-comment")
                comment_field.clear()
                comment_field.send_keys("BGMENU ТЕСТ! НЕ ПРИГОТВЯЙТЕ!")
                order_submit = self.driver.find_element_by_css_selector(
                    "#cart-detiles-cont > div.main-content-ordered > div.row > div.col-md-3 > a")
                order_submit.click()

            sleep(2)

            '''try:
                self.driver.find_element_by_css_selector("#cart-detiles-cont > div:nth-child(3) > div > div > span > span")
                self.driver.find_element_by_css_selector("#cart-detiles-cont > div:nth-child(3) > div > div > div:nth-child(3) > label").click()
                sleep(2)
                self.driver.find_element_by_css_selector("#cart-detiles-cont > div:nth-child(3) > div > div > div:nth-child(1) > label").click()
                sleep(2)
                order_submit.click()
                sleep(3)
            except NoSuchElementException:
                order_submit.click()
                sleep(2)'''
            self.driver.find_element_by_css_selector("#logo").click()
            sleep(2)


web = BasicTestCases
web.driver_ini(web)
web.login_test(web)
web.make_order_test(web)
