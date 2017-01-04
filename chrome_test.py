import os
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from time import sleep
import random

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
        address_field = self.driver.find_element_by_css_selector(
            '#main-search > div > div.input-hold.neighbourhood > input')
        streets = ['жк Гоце Делчев 15', 'жк Белите Брези 1', 'бул. Джеймс Баучър 3', 'жк Надежда 3', 'ул. Ралевица 84',
                   'жк Младост 2 2', 'Бокар 12', 'жк Банишора 1', 'Централна ЖП гара 6', 'ул.Яна Язова 3',
                   'ул.Чорлу 55', 'ул.Боженци 8', 'ул.Буная 18', 'ул.Бигла 21', 'жк Банишора 2',
                   'ул.Проф.Петър Джидров 2',
                   'ул.Хайдушка гора 21', 'бул.Симеоновско шосе 48', 'ул.Княз Борис 1', 'ул.Добротица Деспот',
                   'бул.Петко Каравелов 20', 'жк Обеля - 2 264', 'ул.Академик Петър Динеков 23',
                   'бул.Черни Връх 27', 'ул.Перун 2', 'бул.Свети Наум 23', 'ул.Резньовете 22', 'ул.Аксаков 9',
                   'ул.Беломорски Проход', 'жк Дианабад 2', '7 - ми 11 - ти километър', 'кв. Челопечене 4',
                   'Родопски извор № 30', 'ул.Света Гора № 2', 'Русалка 4', 'бул. Васил Левски 61',
                   'Добри Христов 144', 'Овча купел 1 558', 'Сан Стефано 11-13', 'Атанас Москов 324а',
                   'Сребърна 15', 'Мелник 356', 'ул. Васил Петлешков 80', 'Люлин 6 655',
                   '8-мин Декември 21',
                   'Осогово 30', 'Зона б-5 христо белчев 16', 'ул. Меча поляна 2', 'Цариградско шосе 83',
                   'Петър Протич 6',
                   'Буная 18',
                   '''('Хиподрума 104')''', 'Ами буе 17-23', 'Младост-3 309', 'Преки път 13', 'Съзнание 36',
                   'Красно село 211', 'ГМ Димитров 32', 'бул. България 49а', 'Jerusalem building 7',
                   'бул. Александър Малинов 91', 'ул. Хан Омуртаг 24', 'Казбек 10', 'Николай Лилиев 34',
                   'бул. Никола Вапцаров 53', 'ул. Бесарабия 15', 'ул. Блага Димитрова 1', 'Западна блок 106',
                   'Жеко Войвода 5',
                   'Яна 1', 'бул. Александър Малинов 51', 'Балканджи Йово 9', 'Захари Зограф 32А',
                   'бул. Янко Сакъзов 34',
                   'Деян Белишки 30', 'бул. Възкресение 87', 'Ген. Стоян Стоянов 68', 'ул. Перник 97',
                   'ул. Ресенска Поляна 98']

        address_field.send_keys(random.choice(streets))
        sleep(5)
        address_field.send_keys(Keys.ARROW_DOWN)
        sleep(2)
        address_field.send_keys(Keys.ENTER)
        search_submit = self.driver.find_element_by_css_selector('#search-submit')
        search_submit.click()


x = WebDriverTestCase()
x.setUp()
# x.register()
x.addressSearch()
