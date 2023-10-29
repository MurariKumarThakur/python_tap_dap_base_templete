import logging
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service

service = Service()


class DriverFactory:
    driver = None
    logger = logging.getLogger(__name__)

    @classmethod
    def initialize_browser(cls, browser_name):
        driver = None
        if browser_name == "chrome":
            options = webdriver.ChromeOptions()
            driver = webdriver.Chrome(service=service, options=options)

        elif browser_name == "firefox":
            options = webdriver.FirefoxOptions()
            driver = webdriver.Firefox(service=service, options=options)

        elif browser_name == "edge":
            options = webdriver.EdgeOptions()
            driver = webdriver.Edge(service=service, options=options)

        if driver is not None:
            driver.delete_all_cookies()
            driver.maximize_window()
            time.sleep(10)
            driver.implicitly_wait(10)  # Adjust as needed
            driver.set_page_load_timeout(30)
        else:
            # Handle the case when 'browser_name' does not match any of the conditions
            print(f"Unsupported browser: {browser_name}")
        # Add more browser options as needed

    # Adjust as needed

    @classmethod
    def get_driver(cls):
        return cls.driver
