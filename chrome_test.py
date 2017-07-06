import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import random
import logging

chromedriver = "C:/Users/Mechan1x/web_drivers/chromedriver.exe"
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
        self.driver.get("https://www128.imperiaonline.org")

    def registration_test(self):
        register_button = self.driver.find_element_by_css_selector(
            "#content > div > div.register-wraper.fleft > div.centered > a")
        register_button.click()
        sleep(1)
        username_input = self.driver.find_element_by_css_selector("#reg-user")
        username_input.send_keys("test_user13")
        pass_input = self.driver.find_element_by_css_selector("#reg-pass")
        pass_input.send_keys("testtest")
        email_input = self.driver.find_element_by_css_selector("#reg-email")
        email_input.send_keys("marin.ivanov@imperiaonline.org")
        registration_submit = self.driver.find_element_by_css_selector("#register")
        registration_submit.click()
        if self.driver.current_url == "https://www141.imperiaonline.org/imperia/game_v6/game/village.php":
            logging.info("Registration test is passed!")
        else:
            logging.error("Registration test failed!")

    def login_test(self):
        username_input = self.driver.find_element_by_css_selector("#login-user")
        username_input.send_keys("test_user13")
        pass_input = self.driver.find_element_by_css_selector("#login-pass")
        pass_input.send_keys("testtest")
        login_submit = self.driver.find_element_by_css_selector("#login-button-wrapper > input")
        login_submit.click()
        sleep(2)
        ftl_url = self.driver.current_url
        correct_url = ".imperiaonline.org/imperia/game_v6/game/village.php"
        if correct_url in ftl_url:
            logging.info("Login test is passed!")
        else:
            logging.error("Login test failed!")
        sleep(3)

    '''def tutorial_1(self):
        # screen_1 = self.driver.find_element_by_css_selector
        # ("#begin-tutorial-wrapper > div.tutorial-order.centered > div > button")
        # screen_1.click()
        t_quest_1_accept = self.driver.find_element_by_css_selector(
            "#messageboxtutorialWindow > div > div.tutorial-content > div.tutorial-order.centered > div > button")
        t_quest_1_accept.click()
        sleep(1)
        welcome_back_m = self.driver.find_element_by_css_selector(
            "# messageboxemail_promo_notification > div > div > div.centered-block.fnone > button")
        welcome_back_m.click()
        t_building_1 = self.driver.find_element_by_css_selector("//*[@id="
        tutorialWindow
        "]")
        t_building_1.click()'''


web = BasicTestCases
web.driver_ini(web)
# web.registration_test(web)
web.login_test(web)
# web.tutorial_1(web)
