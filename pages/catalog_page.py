from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base

"""Открываем каталог"""
class Catalog_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    catalog_button = "//button[@class='_30-fz button-focus-ring Hkr1q _1pHod _2rdh3 _3rbM-']"
    clothes_and_shoes = "//li[@class='_12HrO _3-xdb cia-cs']"
    main_word_2 = "//a[@href='//ya.ru/']"


    # Getters
    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_button)))

    def get_clothes_and_shoes(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.clothes_and_shoes)))

    def get_main_word_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word_2)))


    # Actions
    def click_catalog_button(self):
        self.get_catalog_button().click()
        print("Click catalog button")

    def click_clothes_and_shoes(self):
        self.get_clothes_and_shoes().click()
        print("Click clothes and shoes")



    # Methods
    def sort(self):
       self.get_current_url()
       self.click_catalog_button()
       self.click_clothes_and_shoes()
       self.assert_word(self.get_main_word_2(), 'Яндекс')

