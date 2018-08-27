import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException, StaleElementReferenceException
from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.remote.webelement import WebElement, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expect
from framework.driver_core.element import Element


class Driver:
    def __init__(self, browser: str):
        self.browser = browser
        self.current = self._select_driver(browser)

    @property
    def current_window_handle(self):
        return self.current.current_window_handle

    @property
    def page_source(self):
        return self.current.page_source

    @property
    def switch_to(self):
        return self.current.switch_to

    @property
    def title(self):
        return self.current.title

    @property
    def url(self):
        return self.current.current_url

    @property
    def window_handles(self):
        return self.current.window_handles

    def back(self):
        self.current.back()

    def close(self):
        self.current.close()

    def execute_script(self, js, *args):
        self.current.execute_script(js, args)

    def execute_async_script(self, js, *args):
        self.current.execute_async_script(js, args)

    def find_element(self, by, locator):
        webelement = WebDriverWait(self.current, 30).until(
            lambda drvr: drvr.find_element(by, locator))
        element = Element(webelement)
        element.by = by
        element.locator_str = locator
        return element

    def find_elements(self, by, locator):
        return self.current.find_elements(by, locator)

    def forward(self):
        self.current.forward()

    def goto(self, url):
        self.current.get(url)

    def maximize_window(self):
        self.current.maximize_window()

    def quit(self):
        self.current.quit()

    def refresh(self):
        self.current.refresh()

    def save_screenshot(self, filename) -> bool:
        return self.current.save_screenshot(filename)

    def _select_driver(self, browser):
        driver = None

        if browser == "chrome":
            driver = Chrome(
                "c:/dev/python-automation/_drivers/chromedriver.exe")
        elif browser == "firefox":
            driver = Firefox(
                "c:/dev/python-automation/_drivers/chromedriver.exe")

        if driver == None:
            raise WebDriverException(f"invalid browser specified: {browser}")

        driver.maximize_window()
        return driver
