import logging
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService


class BrowserConfig:
    def __init__(self):
        self.ENVIRONMENT = os.getenv("env")
        self.BROWSER = os.getenv("browser")

    def select_browser(self):
        browser = self.BROWSER
        environment = self.ENVIRONMENT
        driver = None
        if environment == 'local':
            if browser == 'firefox':
                driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
            elif browser == 'chrome':
                driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            else:
                raise ValueError(
                    f'--browser="{browser}" is not defined')
        elif environment == "remote":
            pass
            options = Options()
            selenoid_capabilities = {
                "browserName": "chrome",
                "browserVersion": "latest",
                "selenoid:options": {
                    "enableVNC": True,
                    "enableVideo": False
                }
            }
            options.capabilities.update(selenoid_capabilities)
            driver = webdriver.Remote(
                command_executor="http://localhost:4444/wd/hub",
                options=options)

        logging.info(f"Setting {environment} driver with {browser}...")

        return driver
