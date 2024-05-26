import datetime
from selenium.webdriver import ActionChains


class Base():
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)

    """Method get current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url: " + get_url)


    """Method assert word"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")


    """Method assert price"""
    def assert_price(self, price, result):
        value_price = price.text
        assert value_price == result
        print("Good value price")

    """Method screenshot"""
    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\katen\\PycharmProjects\\project_market\\screen\\' + name_screenshot)


    """Method double click"""
    def get_double_clicks(self):
        get_click = self.driver.action.double_clicks().perform()
        print(get_click)

    """Method move to element"""
    def move_to_element(self, element):
        self.action.move_to_element(element).perform()


    """Method go back"""
    def go_back(self):
        self.driver.back()

    """Method refresh"""
    def refresh(self):
        self.driver.refresh()

    """ Scroll the page down. """
    def scroll_down(self, offset=0):

        if offset:
            self.driver.execute_script('window.scrollTo(0, {0});'.format(offset))
        else:
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')


    """ Scroll the page up. """
    def scroll_up(self, offset=0):

        if offset:
            self.driver.execute_script('window.scrollTo(0, -{0});'.format(offset))
        else:
            self.driver.execute_script('window.scrollTo(0, -document.body.scrollHeight);')


    """ Switch to iframe by it's name. """
    def switch_to_iframe(self, iframe):
        self.driver.switch_to.frame(iframe)


    """ Cancel iframe focus. """
    def switch_out_iframe(self):
        self.driver.switch_to.default_content()













