from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class createRequest:
    def __init__(self, driver: WebDriver):
        """This class is injected with a driver on intialization"""
        self.driver = driver

    def description_input_field(self):
        return self.driver.find_element(By.ID, "description")

    def price_input_field(self):
        return self.driver.find_element(By.ID, "price")

    def is_urgent_input_field(self):
        return self.driver.find_element(By.ID, "isUrgent")

    def not_urgent_input_field(self):
        return self.driver.find_element(By.ID, "isNotUrgent")

    def date_input_field(self):
        return self.driver.find_element(By.ID, "date")

    def submit_button(self):
        return self.driver.find_element(By.ID, "submitButton")

    def user_input_field(self):
        return self.driver.find_element(By.ID, "usernameInput")

    def password_input_field(self):
        return self.driver.find_element(By.ID, "passwordInput")

    def login_button(self):
        return self.driver.find_element(By.ID, "loginButton")

    def logout_button(self):
        return self.driver.find_element(By.ID, "logoutButton")

    def create_request_button(self):
        return self.driver.find_element(By.ID, "requestButton")

    def home_button(self):
        return self.driver.find_element(By.ID, "homeButton")

