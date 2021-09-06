import os

from selenium import webdriver

from bot.booking.constants import BASE_URL

PATH = 'D:/SeleniumDrivers'


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=PATH, teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ["PATH"] += os.pathsep + driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    # tear down
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_on_first_page(self):
        self.get(BASE_URL)

    def change_currency(self, currency=None):
        currency_button = self.find_element_by_css_selector(
            'button[data-tooltip-text="Choose your currency"]'
        )
        currency_button.click()
        selected_currency_element = self.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )
        selected_currency_element.click()

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element_by_id('ss')
        search_field.clear()  # clear input field
        search_field.send_keys(place_to_go)

        first_dropdown_item = self.find_element_by_css_selector(
            'li[data-i="0"]'
        )
        first_dropdown_item.click()

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element_by_css_selector(
            f'td[data-date="{check_in_date}"]'
        )
        check_in_element.click()

        check_out_element = self.find_element_by_css_selector(
            f'td[data-date="{check_out_date}"]'
        )
        check_out_element.click()
