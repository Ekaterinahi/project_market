from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base

"""Выбираем избранный товар и отправляем в карзину"""
class Product_like_page(Base):

    url = 'https://market.yandex.ru/my/wishlist?track=head'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    product_1_button = "//button[@aria-label='В корзину']"
    product_2_button = "//button[@aria-label='В корзину']"
    product_3_button = "//button[@aria-label='В корзину']"
    product_4_button = "//button[@aria-label='В корзину']"
    product_5_button = "//button[@aria-label='В корзину']"
    product_6_button = "//button[@aria-label='В корзину']"
    product_7_button = "//button[@aria-label='В корзину']"
    product_8_button = "//button[@aria-label='В корзину']"
    basket_button = "//a[@class='EQlfk _2h0Ng _1IKOp']"


    # Getters
    def get_product_1_button(self):
        try:
            return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_1_button)))
        except TimeoutException:
            print("TimeoutException: Element not found within the specified time.")

    def get_product_2_button(self):
        try:
            return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_2_button)))
        except TimeoutException:
            print("TimeoutException: Element not found within the specified time.")

    def get_product_3_button(self):
        try:
            return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_3_button)))
        except TimeoutException:
            print("TimeoutException: Element not found within the specified time.")

    def get_product_4_button(self):
        try:
            return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_4_button)))
        except TimeoutException:
            print("TimeoutException: Element not found within the specified time.")

    def get_product_5_button(self):
        try:
            return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_5_button)))
        except TimeoutException:
            print("TimeoutException: Element not found within the specified time.")

    def get_product_6_button(self):
        try:
            return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_6_button)))
        except TimeoutException:
            print("TimeoutException: Element not found within the specified time.")

    def get_product_7_button(self):
        try:
            return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_7_button)))
        except TimeoutException:
            print("TimeoutException: Element not found within the specified time.")

    def get_product_8_button(self):
        try:
            return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_8_button)))
        except TimeoutException:
            print("TimeoutException: Element not found within the specified time.")

    def get_basket_button(self):
        try:
            return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.basket_button)))
        except TimeoutException:
            print("TimeoutException: Element not found within the specified time.")


    # Actions

    def click_product_1_button(self):
        self.get_product_1_button().click()
        print("Click product 1 button")

    def click_product_2_button(self):
        self.get_product_2_button().click()
        print("Click product 2 button")

    def click_product_3_button(self):
        self.get_product_3_button().click()
        print("Click product 3 button")

    def click_product_4_button(self):
        self.get_product_4_button().click()
        print("Click product 4 button")

    def click_product_5_button(self):
        self.get_product_5_button().click()
        print("Click product 5 button")

    def click_product_6_button(self):
        self.get_product_6_button().click()
        print("Click product 6 button")

    def click_product_7_button(self):
        self.get_product_7_button().click()
        print("Click product 7 button")

    def click_product_8_button(self):
        self.get_product_8_button().click()
        print("Click product 8 button")

    def click_basket_button(self):
        self.get_basket_button().click()
        print("Click basket button")



    # Methods

    def products_1_button(self):
       self.driver.get(self.url)
       self.driver.maximize_window()
       self.get_current_url()
       self.click_product_1_button()
       basket_button = self.get_basket_button()
       self.move_to_element(basket_button)
       self.click_basket_button()

    def products_2_button(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_product_2_button()
        basket_button = self.get_basket_button()
        self.move_to_element(basket_button)
        self.click_basket_button()

    def products_3_button(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_product_3_button()
        basket_button = self.get_basket_button()
        self.move_to_element(basket_button)
        self.click_basket_button()

    def products_4_button(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_product_4_button()
        basket_button = self.get_basket_button()
        self.move_to_element(basket_button)
        self.click_basket_button()

    def products_5_button(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_product_5_button()
        basket_button = self.get_basket_button()
        self.move_to_element(basket_button)
        self.click_basket_button()

    def products_6_button(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_product_6_button()
        basket_button = self.get_basket_button()
        self.move_to_element(basket_button)
        self.click_basket_button()

    def products_7_button(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_product_7_button()
        basket_button = self.get_basket_button()
        self.move_to_element(basket_button)
        self.click_basket_button()

    def products_8_button(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_product_8_button()
        basket_button = self.get_basket_button()
        self.move_to_element(basket_button)
        self.click_basket_button()


















