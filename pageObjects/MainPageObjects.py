from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class MainPage:
    def __init__(self, driver):
        self.driver = driver

        #performs a click after looking for the locator
    def click(self, by_locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(by_locator)).click()

    #press the enter button
    def enter_button(self, by_locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.RETURN)

# this function asserts comparison of a web element's text with passed in text.
    def assert_element_text(self, by_locator, element_text):
        web_element = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(by_locator))
        assert web_element.text == element_text

# this function performs text entry of the passed in text, in a web element whose locator is passed to it.
    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    # this function checks if the web element whose locator has been passed to it, is enabled or not and returns
    # web element if it is enabled.
    def is_enabled(self, by_locator):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(by_locator))

    # this function checks if the web element whose locator has been passed to it, is visible or not and returns
    # true or false depending upon its visibility.
    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    # this function moves the mouse pointer over a web element whose locator has been passed to it.
    def hover_to(self, by_locator):
        element = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()

    # check if web element is selected
    def is_element_selected(self, by_locator):
        element = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(by_locator)).is_selected()
        if element is True:
            print("The element is selected")
        else:
            print("The element is not selected")

    # check if web element is selected, then clicks on it

    def is_element_selected_Click(self, by_locator):
        element = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(by_locator))
        element_selected = element.is_selected()
        if element_selected is not True:
            element.click()
        else:
            print("The element is not selected")

    def selectItem(self, by_locator, value):
        element = Select(WebDriverWait(self.driver,3).until(EC.visibility_of_element_located(by_locator)))
        element.select_by_value(value)



    def presence_located(self, by_locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
            print ("Element is ready")
        except TimeoutError:
            print("Loading took to long")