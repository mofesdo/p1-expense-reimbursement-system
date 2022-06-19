from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class loginPage:

    def __init__(self, driver: WebDriver):
        """This class is injected with a driver on intialization"""
        self.driver = driver

    def username_input_field(self):
        return self.driver.find_element(By.ID, "usernameInput")

    def password_input_field(self):
        return self.driver.find_element(By.ID, "passwordInput")

    def submit_button(self):
        return self.driver.find_element(By.ID, "loginButton")

    def logout_button(self):
        return self.driver.find_element(By.ID, "logoutButton")

