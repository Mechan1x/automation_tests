import os
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from time import sleep
import random

edgedriver = "/Users/Mechan1x/AppData/Local/web_drivers/MicrosoftWebDriver.exe"
os.environ["webdriver.edgedriver.driver"] = edgedriver


class WebDriverTestCase(unittest.TestCase):
    def addressSearch(self):
            driver = webdriver.Edge()
            self.driver = driver
            self.driver.get("https://integration.bgmenu.com")
            sleep(4)
            address_field = driver.find_element_by_css_selector(
                '#main-search > div > div.input-hold.neighbourhood > input')
            # address_field.send_keys(Keys.LEFT_CONTROL + 'a')  # The type language should be EN for this to work
            # address_field.send_keys(Keys.BACKSPACE)
            streets = ['жк Гоце Делчев 15', 'жк Белите Брези 1', 'бул. Джеймс Баучър 3', 'жк Надежда 3',
                       'ул. Ралевица 84',
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
                       'Ами буе 17-23', 'Младост-3 309', 'Преки път 13', 'Съзнание 36',
                       'Красно село 211', 'ГМ Димитров 32', 'бул. България 49а', 'Jerusalim 7',
                       'бул. Александър Малинов 91', 'ул. Хан Омуртаг 24', 'Казбек 10', 'Николай Лилиев 34',
                       'бул. Никола Вапцаров 53', 'ул. Бесарабия 15', 'ул. Блага Димитрова 1', 'Западна блок 106',
                       'Жеко Войвода 5',
                       'Яна 1', 'бул. Александър Малинов 51', 'Балканджи Йово 9', 'Захари Зограф 32А',
                       'бул. Янко Сакъзов 34',
                       'Деян Белишки 30', 'бул. Възкресение 87', 'Стоян Стоянов 68', 'ул. Перник 97',
                       'ул. Ресенска Поляна 98']

            address_field.send_keys(random.choice(streets))
            sleep(2)
            address_field.send_keys(Keys.ARROW_DOWN)
            sleep(2)
            address_field.send_keys(Keys.ENTER)
            sleep(1)
            address_field.send_keys(Keys.ENTER)


x = WebDriverTestCase()
# x.register()
x.addressSearch()
