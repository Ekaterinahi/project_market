from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base

"""Выбираем понравившийся товар и отправляем в избранное"""
class Product_page(Base):

    url = "https://market.yandex.ru/search?text=%D0%96%D0%B5%D0%BD%D1%81%D0%BA%D0%B8%D0%B9%20%D1%85%D1%83%D0%B4%D0%B8%20%D0%B8%20%D1%81%D0%B2%D0%B8%D1%82%D0%B5%D1%80&rs=eJxNUD1LA0EU3EtivASElJpYnIVol7u9ZJOokcXGIBYaFBvRJF4OC0utRAhprP0BSnqxE8SP6FnYWNlaeT_BSlERvBlEbIZh5u28eSu78SXjwRDBZT_CRmw2wvB4BvxkOsJeHIr4rEbY8YFBjZOrmAlccNGFrvPEBOaDjRvkHAEbB9BFDmkiwYQxvAqr1A_B9Txz9qH0RoEhudZI6CSBwQf543WE1sodJheZU0MTsQ1uNdnTZPNXXsG7xBvdb25vIUHzIj0wBWUZkzrFS1-wRddvkTzBJpKZ50zbuoJ7wZx18MY4f-MZGJxiJvyCa4Vsdca9Her3vMLusyGbv_MHnvpza-lc2jSNjDU8ZCUyyWzKa_vNvZ3dTWmJSfFnGpbx33RojtA0aMayg78mrIyxYPqq6PjllluXTslRsiIdKUvKzldUwa24rq1czyu2fOVJzy20lfKLTtlWtp138s4PbrOl8g%2C%2C&glfilter=26417130%3A27014351%2C27014370&glfilter=21194330%3A28575564%2C28575555&qrfrom=4&offer-shipping=pickup"


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.action = ActionChains(self.driver)



    # Locators
    product_1 = "(//button[@title='Добавить в избранное'])[1]"
    product_2 = "(//button[@title='Добавить в избранное'])[2]"
    product_3 = "(//button[@title='Добавить в избранное'])[3]"
    product_4 = "(//button[@title='Добавить в избранное'])[6]"
    product_5 = "(//button[@title='Добавить в избранное'])[7]"
    product_6 = "(//button[@title='Добавить в избранное'])[8]"
    product_7 = "(//button[@title='Добавить в избранное'])[9]"
    product_8 = "(//button[@title='Добавить в избранное'])[12]"
    like_button = "(//*[name()='svg'][@title='Избранное'])[1]"


    # Getters

    def get_product_1(self):
        try:
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1)))
        except TimeoutException:
            print("TimeoutException: Element not found within the specified time.")

    def get_product_2(self):
        try:
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_2)))
        except TimeoutException:
            print("TimeoutException: Element not found within the specified time.")

    def get_product_3(self):
        try:
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_3)))
        except TimeoutException:
            print("TimeoutException: Element not found within the specified time.")

    def get_product_4(self):
        try:
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_4)))
        except TimeoutException:
            print("TimeoutException: Element not found within the specified time.")

    def get_product_5(self):
        try:
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_5)))
        except TimeoutException:
            print("TimeoutException: Element not found within the specified time.")

    def get_product_6(self):
        try:
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_6)))
        except TimeoutException:
            print("TimeoutException: Element not found within the specified time.")

    def get_product_7(self):
        try:
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_7)))
        except TimeoutException:
            print("TimeoutException: Element not found within the specified time.")

    def get_product_8(self):
        try:
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_8)))
        except TimeoutException:
            print("TimeoutException: Element not found within the specified time.")

    def get_like_button(self):
        try:
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.like_button)))
        except TimeoutException:
            print("TimeoutException: Element not found within the specified time.")


    # Actions

    def click_product_1(self):
        self.get_product_1().click()
        print("Click product 1")

    def click_product_2(self):
        self.get_product_2().click()
        print("Click product 2")

    def click_product_3(self):
        self.get_product_3().click()
        print("Click product 3")

    def click_product_4(self):
        self.get_product_4().click()
        print("Click product 4")

    def click_product_5(self):
        self.get_product_5().click()
        print("Click  product 5")

    def click_product_6(self):
        self.get_product_6().click()
        print("Click product 6")

    def click_product_7(self):
        self.get_product_7().click()
        print("Click product 7")

    def click_product_8(self):
        self.get_product_8().click()
        print("Click product 8")

    def click_like_button(self):
        self.get_like_button().click()
        print("Click like_button")



    # Methods

    def button_product_1(self):
        self.driver.get(self.url)
        self.get_current_url()
        product_1 = self.get_product_1()
        self.move_to_element(product_1)
        self.click_product_1()
        like_button = self.get_like_button()
        self.move_to_element(like_button)
        self.click_like_button()

    def button_products_2(self):
        self.driver.get(self.url)
        self.get_current_url()
        product_2 = self.get_product_2()
        self.move_to_element(product_2)
        self.click_product_2()
        like_button = self.get_like_button()
        self.move_to_element(like_button)
        self.click_like_button()

    def button_products_3(self):
        self.driver.get(self.url)
        self.get_current_url()
        product_3 = self.get_product_3()
        self.move_to_element(product_3)
        self.click_product_3()
        like_button = self.get_like_button()
        self.move_to_element(like_button)
        self.click_like_button()

    def button_products_4(self):
        self.driver.get(self.url)
        self.get_current_url()
        product_4 = self.get_product_4()
        self.move_to_element(product_4)
        self.click_product_4()
        like_button = self.get_like_button()
        self.move_to_element(like_button)
        self.click_like_button()

    def button_products_5(self):
        self.driver.get(self.url)
        self.get_current_url()
        product_5 = self.get_product_5()
        self.move_to_element(product_5)
        self.click_product_5()
        like_button = self.get_like_button()
        self.move_to_element(like_button)
        self.click_like_button()

    def button_products_6(self):
        self.driver.get(self.url)
        self.get_current_url()
        product_6 = self.get_product_6()
        self.move_to_element(product_6)
        self.click_product_6()
        like_button = self.get_like_button()
        self.move_to_element(like_button)
        self.click_like_button()

    def button_products_7(self):
        self.driver.get(self.url)
        self.get_current_url()
        product_7 = self.get_product_7()
        self.move_to_element(product_7)
        self.click_product_7()
        like_button = self.get_like_button()
        self.move_to_element(like_button)
        self.click_like_button()

    def button_products_8(self):
        self.driver.get(self.url)
        self.get_current_url()
        product_8 = self.get_product_8()
        self.move_to_element(product_8)
        self.click_product_8()
        like_button = self.get_like_button()
        self.move_to_element(like_button)
        self.click_like_button()


















