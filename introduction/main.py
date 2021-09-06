from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1)    Each different browser uses a different webdriver object (i.e. Chrome() for the Chrome browser, alternatively, Mozilla or Edge could have been used)
# 2)    By default, when running the below line of code, an error will be outputted to the terminal 'chromedriver' executable needs to be in PATH.
#       In order to solve the error/issue, the open a new tab in chrome and type 'chrome://version', this will provide the version of the currently installed
#       version of chrome (local version). The chromedriver executable (required) can be found at https://chromedriver.storage.googleapis.com/index.html.
#       !!! The version (Major) needs to match (local version and executable). !!!
PATH = 'D:/SeleniumDrivers/chromedriver.exe'
driver = webdriver.Chrome(PATH)

# make the driver access the given URL
driver.get("https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html")
# ensure the browser does the action only after 30 seconds
driver.implicitly_wait(30)
button_element = driver.find_element_by_id('downloadButton')
button_element.click()

# wait for element to load

WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label'),       # Element
        'Complete!'                              # Expected text
    )
)