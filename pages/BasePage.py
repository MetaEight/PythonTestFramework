import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.saucedemo.com/"

    def page_has_loaded(self):
        try:
            WebDriverWait(self.driver, 1000, poll_frequency=0.5).until(
                lambda driver: self.driver.execute_script('return document.readyState == "complete";'))
            WebDriverWait(self.driver, 1000, poll_frequency=0.5).until(
                lambda driver: self.driver.execute_script('return jQuery.active == 0'))
            WebDriverWait(self.driver, 1000, poll_frequency=0.5).until(
                lambda driver: self.driver.execute_script('return typeof jQuery != "undefined"'))
            WebDriverWait(self.driver, 1000, poll_frequency=0.5).until(lambda driver: self.driver.execute_script(
                'return angular.element(document).injector().get("$http").pendingRequests.length === 0'))
        except:
            return False

    def find_element(self, locator, time=10, element=None):
        if element is None:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                             message=f"Can't find element by locator {locator}")
        else:
            element = element.find_element(*locator)
        return element

    def find_elements(self, locator, element=None):
        try:
            if element is None:
                element = self.driver.find_elements(*locator)
            else:
                element = element.find_elements(*locator)
        except:
            element = False
        return element

    def go_to_page(self, path=None):
        url = self.base_url if path is None else f"{self.base_url}{path}"
        self.driver.get(url)

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
