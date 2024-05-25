from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base

"""Выбираем избранный товар и отправляем в карзину"""
class Checking_registration_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    bat_jacket_word = "//a[contains(text(), 'Кофта Оверсайз Летучая Мышь Серый')]"
    sweater_elongated_word = "//a[contains(text(), 'Свитер удлиненный')]"
    sweater_white_word = "//a[contains(text(), 'Свитер удлиненный')]"
    sweater_black_word = "//a[contains(text(), 'Свитер удлиненный')]"
    love_republic_milk_word = "//a[contains(text(), 'Свитер Женский, модель s23180молочный, one size 42-48')]"
    white_oversize_sweater_word = "//a[contains(text(), 'Свитер женский белый оверсайз')]"
    beige_oversize_sweater_word = "//a[contains(text(), 'Свитер женский бежевый оверсайз')]"
    sweater_model_milk_word = "//a[contains(text(), 'Свитер Женский, модель k8613молочный, one size 42-48')]"
    price_1 = "//span[contains(text(),'1 254')]"
    price_2 = "//span[contains(text(),'1 100')]"
    price_3 = "//span[contains(text(),'1 100')]"
    price_4 = "//span[contains(text(),'1 100')]"
    price_5 = "(//span[contains(text(),'790')])[2]"
    price_6 = "//span[contains(text(),'2 564')]"
    price_7 = "//span[contains(text(),'2 990')]"
    price_8 = "(//span[contains(text(),'750')])[2]"
    decoration_button = "//button[@id='cartCheckoutButton']"

    # Getters

    def get_bat_jacket_word(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.bat_jacket_word)))

    def get_sweater_elongated_word(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.sweater_elongated_word)))

    def get_sweater_white_word(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.sweater_white_word)))

    def get_sweater_black_word(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.sweater_black_word)))

    def get_love_republic_milk_word(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.love_republic_milk_word)))

    def get_white_oversize_sweater_word(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.white_oversize_sweater_word)))

    def get_beige_oversize_sweater_word(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.beige_oversize_sweater_word)))

    def get_sweater_model_milk_word(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.sweater_model_milk_word)))

    def get_price_1(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price_1)))

    def get_price_2(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price_2)))

    def get_price_3(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price_3)))

    def get_price_4(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price_4)))

    def get_price_5(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price_5)))

    def get_price_6(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price_6)))

    def get_price_7(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price_7)))

    def get_price_8(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price_8)))

    def get_decoration_button(self):
        try:
            return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.decoration_button)))
        except TimeoutException:
            print("TimeoutException: Element not found within the specified time.")



    # Actions

    def click_decoration_button(self):
        self.get_decoration_button().click()
        print("Click decoration button")



    # Methods

    def bat_jacket_word_1(self):
       self.get_current_url()
       self.assert_word(self.get_bat_jacket_word(), 'Кофта Оверсайз Летучая Мышь Серый')
       self.assert_price(self.get_price_1(), '1 254')
       self.click_decoration_button()

    def sweater_elongated_word_1(self):
       self.get_current_url()
       self.assert_word(self.get_sweater_elongated_word(), 'Свитер удлиненный')
       self.assert_price(self.get_price_2(), '1 100')
       self.click_decoration_button()

    def sweater_white_word_1(self):
       self.get_current_url()
       self.assert_word(self.get_sweater_white_word(), 'Свитер удлиненный')
       self.assert_price(self.get_price_3(), '1 100')
       self.click_decoration_button()

    def sweater_black_word_1(self):
       self.get_current_url()
       self.assert_word(self.get_sweater_black_word(), 'Свитер удлиненный')
       self.assert_price(self.get_price_4(), '1 100')
       self.click_decoration_button()

    def love_republic_milk_word_1(self):
       self.get_current_url()
       self.assert_word(self.get_love_republic_milk_word(), 'Свитер Женский, модель s23180молочный, one size 42-48')
       self.assert_price(self.get_price_5(), '790')
       self.click_decoration_button()

    def white_oversize_sweater_word_1(self):
       self.get_current_url()
       self.assert_word(self.get_white_oversize_sweater_word(), 'Свитер женский белый оверсайз')
       self.assert_price(self.get_price_6(), '2 564')
       self.click_decoration_button()

    def beige_oversize_sweater_word_1(self):
       self.get_current_url()
       self.assert_word(self.get_beige_oversize_sweater_word(), 'Свитер женский бежевый оверсайз')
       self.assert_price(self.get_price_7(), '2 990')
       self.click_decoration_button()

    def sweater_model_milk_word_1(self):
       self.get_current_url()
       self.assert_word(self.get_sweater_model_milk_word(), 'Свитер Женский, модель k8613молочный, one size 42-48')
       self.assert_price(self.get_price_8(), '750')
       self.click_decoration_button()


















