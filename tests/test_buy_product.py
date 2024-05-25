import time

import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from pages.catalog_inform_page import Catalog_inform_page
from pages.catalog_page import Catalog_page
from pages.checking_before_registration_page import Checking_registration_page
from pages.final_page import Fanal_page
from pages.login_page import Login_page
from pages.product_like_page import Product_like_page
from pages.products_page import Product_page
from pages.womens_clothing_page import Womens_clothing_page


# @pytest.mark.order(3)
def test_buy_product_1(set_up, set_group):

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\katen\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)
    print("Start Test 1")

    login = Login_page(driver)
    login.authorization()
    cp = Catalog_page(driver)
    cp.sort()
    wcp = Womens_clothing_page(driver)
    wcp.classify()
    cip = Catalog_inform_page(driver)
    cip.edit_inform()
    pp = Product_page(driver)
    pp.button_product_1()
    pip = Product_like_page(driver)
    pip.products_1_button()
    crp_1 = Checking_registration_page(driver)
    crp_1.bat_jacket_word_1()
    fp = Fanal_page(driver)
    fp.bat_jackets_word()


    print("Finish Test 1")
    time.sleep(10)
    driver.quit()

# @pytest.mark.order(1)
def test_buy_product_2():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\katen\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)
    print("Start Test 2")

    login = Login_page(driver)
    login.authorization()
    cp = Catalog_page(driver)
    cp.sort()
    wcp = Womens_clothing_page(driver)
    wcp.classify()
    cip = Catalog_inform_page(driver)
    cip.edit_inform()
    pp = Product_page(driver)
    pp.button_products_2()
    pip = Product_like_page(driver)
    pip.products_2_button()
    crp_1 = Checking_registration_page(driver)
    crp_1.sweater_elongated_word_1()
    fp = Fanal_page(driver)
    fp.sweater_elongated_word()

    print("Finish Test 2")
    time.sleep(10)
    driver.quit()

# @pytest.mark.order(2)
def test_buy_product_3():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\katen\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)
    print("Start Test 3")

    login = Login_page(driver)
    login.authorization()
    cp = Catalog_page(driver)
    cp.sort()
    wcp = Womens_clothing_page(driver)
    wcp.classify()
    cip = Catalog_inform_page(driver)
    cip.edit_inform()
    pp = Product_page(driver)
    pp.button_products_3()
    pip = Product_like_page(driver)
    pip.products_3_button()
    crp_1 = Checking_registration_page(driver)
    crp_1.sweater_white_word_1()
    fp = Fanal_page(driver)
    fp.sweater_white_word()

    print("Finish Test 3")
    # time.sleep(10)
    driver.quit()

# @pytest.mark.order(4)
def test_buy_product_4():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\katen\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)
    print("Start Test 4")
#
    login = Login_page(driver)
    login.authorization()
    cp = Catalog_page(driver)
    cp.sort()
    wcp = Womens_clothing_page(driver)
    wcp.classify()
    cip = Catalog_inform_page(driver)
    cip.edit_inform()
    pp = Product_page(driver)
    pp.button_products_4()
    pip = Product_like_page(driver)
    pip.products_4_button()
    crp_1 = Checking_registration_page(driver)
    crp_1.sweater_black_word_1()
    fp = Fanal_page(driver)
    fp.sweater_black_word()

    print("Finish Test 4")
    time.sleep(10)
    driver.quit()

# @pytest.mark.order(6)
def test_buy_product_5():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\katen\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)
    print("Start Test 5")
#
    login = Login_page(driver)
    login.authorization()
    cp = Catalog_page(driver)
    cp.sort()
    wcp = Womens_clothing_page(driver)
    wcp.classify()
    cip = Catalog_inform_page(driver)
    cip.edit_inform()
    pp = Product_page(driver)
    pp.button_products_5()
    pip = Product_like_page(driver)
    pip.products_5_button()
    crp_1 = Checking_registration_page(driver)
    crp_1.love_republic_milk_word_1()
    fp = Fanal_page(driver)
    fp.love_republic_milk_word()

    print("Finish Test 5")
    time.sleep(10)
    driver.quit()

# @pytest.mark.order(7)
def test_buy_product_6():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\katen\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)
    print("Start Test 6")
#
    login = Login_page(driver)
    login.authorization()
    cp = Catalog_page(driver)
    cp.sort()
    wcp = Womens_clothing_page(driver)
    wcp.classify()
    cip = Catalog_inform_page(driver)
    cip.edit_inform()
    pp = Product_page(driver)
    pp.button_products_6()
    pip = Product_like_page(driver)
    pip.products_6_button()
    crp_1 = Checking_registration_page(driver)
    crp_1.white_oversize_sweater_word_1()
    fp = Fanal_page(driver)
    fp.white_oversize_sweater_word()

    print("Finish Test 6")
    time.sleep(10)
    driver.quit()

# @pytest.mark.order(5)
def test_buy_product_7():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\katen\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)
    print("Start Test 7")
#
    login = Login_page(driver)
    login.authorization()
    cp = Catalog_page(driver)
    cp.sort()
    wcp = Womens_clothing_page(driver)
    wcp.classify()
    cip = Catalog_inform_page(driver)
    cip.edit_inform()
    pp = Product_page(driver)
    pp.button_products_7()
    pip = Product_like_page(driver)
    pip.products_7_button()
    crp_1 = Checking_registration_page(driver)
    crp_1.beige_oversize_sweater_word_1()
    fp = Fanal_page(driver)
    fp.beige_oversize_sweater_word()

    print("Finish Test 7")
    time.sleep(10)
    driver.quit()


# @pytest.mark.order(8)
def test_buy_product_8():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\katen\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)
    print("Start Test 8")

    login = Login_page(driver)
    login.authorization()
    cp = Catalog_page(driver)
    cp.sort()
    wcp = Womens_clothing_page(driver)
    wcp.classify()
    cip = Catalog_inform_page(driver)
    cip.edit_inform()
    pp = Product_page(driver)
    pp.button_products_8()
    pip = Product_like_page(driver)
    pip.products_8_button()
    crp_1 = Checking_registration_page(driver)
    crp_1.sweater_model_milk_word_1()
    fp = Fanal_page(driver)
    fp.sweater_model_milk_word()

    print("Finish Test 8")
    time.sleep(10)
    driver.quit()






