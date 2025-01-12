from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base


"""Проходим авторизацию на яндекс маркете"""
class Login_page(Base):

    url = "https://market.yandex.ru/"


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    profile = "//a[@class='EQlfk _1GKjN button-focus-ring _3cvBZ _2CyyG _2zrh4']"
    email = "//input[@id='passp-field-login']"
    button_id = "//button[@id='passp:sign-in']"
    password = "//input[@id='passp-field-passwd']"
    continue_button = "//button[@id='passp:sign-in']"
    main_word_market = "//a[@data-auto='logoMarketLink']"

    # Getters
    # locator на кнопку Войти
    def get_profile(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.profile)))

    #locator email
    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    #locator продолжить в яндекс id
    def get_button_id(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_id)))

    #locator пароля
    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    # locator continue
    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    # locator word Market
    def get_main_word_market(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word_market)))



    # Actions
    def click_profile(self):
        self.get_profile().click()
        print("Click profile")
    def input_email(self, email):
        self.get_email().send_keys(email)
        print("Input email")
    def click_button_id(self):
        self.get_button_id().click()
        print("Click button_id")
    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")
    def click_continue_button(self):
        self.get_continue_button().click()
        print("Click continue button")



    # Methods
    def authorization(self):
       self.driver.get(self.url)
       self.driver.maximize_window()
       self.get_current_url()
       self.click_profile()
       self.input_email("ekt.hi@yandex.ru")
       self.click_button_id()
       self.input_password("112142")
       self.click_continue_button()
       self.assert_word(self.get_main_word_market(), 'Яндекс')
















