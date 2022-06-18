from behave.runner import Context
from selenium import webdriver
from POM.login_POM import loginPage

def before_all(context: Context):
    # We need to add a driver to the context
    context.driver = webdriver.Chrome("utils/Driver/chromedriver.exe")
    # We need to add all POMS to the context
    context.login_POM = loginPage(context.driver)
    # We add an implicit wait to work with latency issues
    context.driver.implicitly_wait(1)

def after_all(context: Context):
    # This will make sure at the end of a behave test all the drivers are closed
    context.driver.quit()
