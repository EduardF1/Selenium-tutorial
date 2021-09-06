#   Utility class for applying filtration
from selenium.webdriver.remote.webdriver import WebDriver


class BookingFilter:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def sort_price_lowest_first(self):
        price_element = self.driver.find_element_by_css_selector('li[data-id="price"]')
        price_element.click()