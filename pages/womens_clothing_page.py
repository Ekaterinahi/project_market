from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base

"""Открываем каталог"""
class Womens_clothing_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    women_clothing_1 = "//a[@href='/search--zhenskaia-odezhda?glfilter=14805991%3A14805993&hid=53543855&nid=54252047']"
    main_word_3 = "//a[@data-auto='logoMarketLink']"
    search_field = "//input[@id='header-search']"
    button_search = "//button[@data-auto='search-button']"

    # Getters    # arrow_to_the_right = "//*[@id='/content/page/fancyPage/cms/2/SearchClarify-SearchClarify/controls']/div[2]/button"
    def get_women_clothing_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.women_clothing_1)))

    # def get_arrow_to_the_right(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.arrow_to_the_right)))

    def get_main_word_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word_3)))

    def get_search_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_field)))

    def get_button_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_search)))



    # Actions
    def click_women_clothing_1(self):
        self.get_women_clothing_1().click()
        print("Click women clothing N1")

    # def click_arrow_to_the_right(self):
    #     self.get_arrow_to_the_right().click()
    #     print("Click arrow to the right")

    def input_search_field(self, search_field):
        self.get_search_field().send_keys(search_field)
        print("Input search field")

    def click_button_search(self):
        self.get_button_search().click()
        print("Click button_search")


    # Methods
    def classify(self):
       self.get_current_url()
       self.assert_word(self.get_main_word_3(), 'Яндекс')
       self.click_women_clothing_1()
       # self.click_arrow_to_the_right()
       self.input_search_field('Женский худи и свитер')
       self.click_button_search()
