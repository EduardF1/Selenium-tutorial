#   Utility class for applying filtration
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BookingFilter:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def sort_price_lowest_first(self):
        price_element = self.driver.find_element_by_css_selector('li[data-id="price"]')
        price_element.click()