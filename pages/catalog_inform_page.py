from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base

"""Выставляем фильтр для последующего выбора товара"""
class Catalog_inform_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    main_word_4 = "//h1[@class='_3lpeU _6tyDq _1ea6I _2Imo_']"
    check_box_size_1 = "//div[@data-filter-value-id='27014351']"
    check_box_size_2 = "//div[@data-filter-value-id='27014370']"
    down_arrow = "//span[@class='_1ygQQ _2-d8S'][contains(text(),'Ещё 7')]"
    check_box_type_sweaters = "//span[contains(text(),'свитер')]"
    check_box_type_turtleneck = "//span[contains(text(),'водолазка')]"
    radio_button_high_rating = "(//span[contains(text(),'От')])[2]"
    button_shopping_method = "//span[contains(text(),'В пункт выдачи')]"


    # Getters
    def get_main_word_4(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word_4)))

    def get_check_box_size_1(self):
        try:
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_box_size_1)))
        except TimeoutException:
            print("TimeoutException: Element not found within the specified time.")

    def get_check_box_size_2(self):
        try:
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_box_size_2)))
        except TimeoutException:
            print("TimeoutException: Element not found within the specified time.")

    def get_down_arrow(self):
        try:
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.down_arrow)))
        except TimeoutException:
            print("TimeoutException: Element not found within the specified time.")
            return None

    def get_check_box_type_sweaters(self):
        try:
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_box_type_sweaters)))
        except TimeoutException:
            print("TimeoutException: Element not found within the specified time.")

    def get_check_box_type_turtleneck(self):
        try:
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_box_type_turtleneck)))
        except TimeoutException:
            print("TimeoutException: Element not found within the specified time.")

    def get_button_shopping_method(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_shopping_method)))

    def get_radio_button_high_rating(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.radio_button_high_rating)))


    # Actions

    def click_check_box_size_1(self):
        self.get_check_box_size_1().click()
        print("Click check_box size N1")

    def click_check_box_size_2(self):
        self.get_check_box_size_2().click()
        print("Click check_box size N2")

    def click_down_arrow(self):
        self.get_down_arrow().click()
        print("Click check_box down arrow")

    def click_check_box_type_sweaters(self):
        self.get_check_box_type_sweaters().click()
        print("Click check_box type sweaters")

    def click_check_box_type_turtleneck(self):
        self.get_check_box_type_turtleneck().click()
        print("Click check_box type turtleneck")

    def click_button_shopping_method(self):
        self.get_button_shopping_method().click()
        print("Click radio_button shopping method")

    def click_radio_button_high_rating(self):
        self.get_radio_button_high_rating().click()
        print("Click radio_button high rating")




    # Methods
    def edit_inform(self):
       self.get_current_url()
       self.assert_word(self.get_main_word_4(), 'Женский худи и свитер в Санкт-Петербурге')
       self.click_check_box_size_1()
       self.click_check_box_size_2()
       down_arrow = self.get_down_arrow()
       self.move_to_element(down_arrow)
       self.click_down_arrow()
       self.click_check_box_type_sweaters()
       self.click_check_box_type_turtleneck()
       self.click_button_shopping_method()
       self.click_radio_button_high_rating()
