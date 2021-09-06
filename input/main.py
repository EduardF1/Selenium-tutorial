from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = 'D:/SeleniumDrivers/chromedriver.exe'
driver = webdriver.Chrome(PATH)

# make the driver access the given URL
driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
driver.implicitly_wait(5)

# disable pop-up
try:
    no_button = driver.find_element_by_class_name('at-cm-no-button')
    no_button.click()
except:
    print('Element not found by given class name. Skipping...')

# access form input fields
input1 = driver.find_element_by_id('sum1')
input2 = driver.find_element_by_id('sum2')

# insert data into input fields
input1.send_keys(Keys.NUMPAD1, Keys.NUMPAD0)  # input1.send_keys(10)
input2.send_keys(Keys.NUMPAD2, Keys.NUMPAD0)  # input2.send_keys(20)

# Get the 'Get Total' button (by xpath)
# get_total_button = driver.find_element_by_xpath("//button[contains(text(), 'Get Total')]")
# Get the 'Get Total' button (by css selector)
get_total_button = driver.find_element_by_css_selector('button[onclick="return total()"]')
get_total_button.click()
