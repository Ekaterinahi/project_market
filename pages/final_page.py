from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base

"""Указываем информацию о получателе"""
class Fanal_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    main_word_7 = "//h1[@class='_3yx5w _3qD7N jb-qv _17lKQ fq7oS']"
    main_word_8 = "//h3[@class='_3qD7N _2obc7 _1nknV fq7oS']"
    bat_jacket_word_2 = "//div[contains(text(), 'Кофта Оверсайз Летучая Мышь Серый')]"
    sweater_elongated_word_2 = "//div[contains(text(), 'Свитер удлиненный')]"
    sweater_white_word_2 = "//div[contains(text(), 'Свитер удлиненный')]"
    sweater_black_word_2 = "//div[contains(text(), 'Свитер удлиненный')]"
    love_republic_milk_word_2 = "//div[contains(text(), 'Свитер Женский, модель s23180молочный, one size 42-48')]"
    white_oversize_sweater_word_2 = "//div[contains(text(), 'Свитер женский белый оверсайз')]"
    beige_oversize_sweater_word_2 = "//div[contains(text(), 'Свитер женский бежевый оверсайз')]"
    sweater_model_milk_word_2 = "//div[contains(text(), 'Свитер Женский, модель k8613молочный, one size 42-48')]"
    price_bat_jacket = "//span[contains(text(), '1 254')]"
    price_sweater_elongated = "//span[contains(text(), '1 100')]"
    price_sweater_white = "//span[contains(text(), '1 100')]"
    price_sweater_black = "//span[contains(text(), '1 100')]"
    price_love_republic_milk = "//span[contains(text(),'790')]"
    price_white_oversize_sweater = "//span[contains(text(), '2 564')]"
    price_beige_oversize_sweater = "//span[contains(text(), '2 990')]"
    price_sweater_model_milk = "//span[contains(text(), '750')]"
    proceed_payment = "//button[@class='_1YUN1 hJpwy _3HEj7 _1nVKJ _1-G63 _3vvUo _2wTrL']"



    # Getters

    def get_main_word_7(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.main_word_7)))

    def get_main_word_8(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.main_word_8)))

    def get_bat_jacket_word_2(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.bat_jacket_word_2)))

    def get_sweater_elongated_word_2(self):
        return WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.sweater_elongated_word_2)))

    def get_sweater_white_word_2(self):
        return WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.sweater_white_word_2)))

    def get_sweater_black_word_2(self):
        return WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.sweater_black_word_2)))

    def get_love_republic_milk_word_2(self):
        return WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.love_republic_milk_word_2)))

    def get_white_oversize_sweater_word_2(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.white_oversize_sweater_word_2)))

    def get_beige_oversize_sweater_word_2(self):
        return WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.beige_oversize_sweater_word_2)))

    def get_sweater_model_milk_word_2(self):
        return WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.sweater_model_milk_word_2)))

    def get_price_bat_jacket(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.price_bat_jacket)))

    def get_price_sweater_elongated(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.price_sweater_elongated)))

    def get_price_sweater_white(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.price_sweater_white)))

    def get_price_sweater_black(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.price_sweater_black)))

    def get_price_love_republic_milk(self):
        return WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.price_love_republic_milk)))

    def get_price_white_oversize_sweater(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.price_white_oversize_sweater)))

    def get_price_beige_oversize_sweater(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.price_beige_oversize_sweater)))

    def get_price_sweater_model_milk(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.price_sweater_model_milk)))

    def get_proceed_payment(self):
        try:
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.proceed_payment)))
        except TimeoutException:
            print("TimeoutException: Element not found within the specified time.")

    # Actions

    def click_proceed_payment(self):
        self.get_proceed_payment().click()
        print("Click proceed payment")


    # Methods

    def bat_jackets_word(self):
        self.get_current_url()
        self.assert_word(self.get_main_word_7(), 'Оформление')
        self.assert_word(self.get_main_word_8(), 'Онлайн')
        self.assert_word(self.get_bat_jacket_word_2(), 'Кофта Оверсайз Летучая Мышь Серый')
        self.assert_price(self.get_price_bat_jacket(), '1 254')
        self.click_proceed_payment()
        self.get_screenshot()

    def sweater_elongated_word(self):
        self.get_current_url()
        self.assert_word(self.get_main_word_7(), 'Оформление')
        self.assert_word(self.get_main_word_8(), 'Онлайн')
        self.assert_word(self.get_sweater_elongated_word_2(), 'Свитер удлиненный')
        self.assert_price(self.get_price_sweater_elongated(), '1 100')
        self.click_proceed_payment()
        self.get_screenshot()

    def sweater_white_word(self):
        self.get_current_url()
        self.assert_word(self.get_main_word_7(), 'Оформление')
        self.assert_word(self.get_main_word_8(), 'Онлайн')
        self.assert_word(self.get_sweater_white_word_2(), 'Свитер удлиненный')
        self.assert_price(self.get_price_sweater_white(), '1 100')
        self.click_proceed_payment()
        self.get_screenshot()

    def sweater_black_word(self):
        self.get_current_url()
        self.assert_word(self.get_main_word_7(), 'Оформление')
        self.assert_word(self.get_main_word_8(), 'Онлайн')
        self.assert_word(self.get_sweater_black_word_2(), 'Свитер удлиненный')
        self.assert_price(self.get_price_sweater_black(), '1 100')
        self.click_proceed_payment()
        self.get_screenshot()

    def love_republic_milk_word(self):
        self.get_current_url()
        self.assert_word(self.get_main_word_7(), 'Оформление')
        self.assert_word(self.get_main_word_8(), 'Онлайн')
        self.assert_word(self.get_love_republic_milk_word_2(),
                         'Свитер Женский, модель s23180молочный, one size 42-48')
        self.assert_price(self.get_price_love_republic_milk(), '790')
        self.click_proceed_payment()
        self.get_screenshot()

    def white_oversize_sweater_word(self):
        self.get_current_url()
        self.assert_word(self.get_main_word_7(), 'Оформление')
        self.assert_word(self.get_main_word_8(), 'Онлайн')
        self.assert_word(self.get_white_oversize_sweater_word_2(), 'Свитер женский белый оверсайз')
        self.assert_price(self.get_price_white_oversize_sweater(), '2 564')
        self.click_proceed_payment()
        self.get_screenshot()


    def beige_oversize_sweater_word(self):
        self.get_current_url()
        self.assert_word(self.get_main_word_7(), 'Оформление')
        self.assert_word(self.get_main_word_8(), 'Онлайн')
        self.assert_word(self.get_beige_oversize_sweater_word_2(), 'Свитер женский бежевый оверсайз')
        self.assert_price(self.get_price_beige_oversize_sweater(), '2 990')
        self.click_proceed_payment()
        self.get_screenshot()

    def sweater_model_milk_word(self):
        self.get_current_url()
        self.assert_word(self.get_main_word_7(), 'Оформление')
        self.assert_word(self.get_main_word_8(), 'Онлайн')
        self.assert_word(self.get_sweater_model_milk_word_2(),
                         'Свитер Женский, модель k8613молочный, one size 42-48')
        self.assert_price(self.get_price_sweater_model_milk(), '750')
        self.click_proceed_payment()
        self.get_screenshot()


