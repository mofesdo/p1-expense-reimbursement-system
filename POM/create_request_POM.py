from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class createRequest:
    def __init__(self, driver: WebDriver):
        """This class is injected with a driver on intialization"""
        self.driver = driver

