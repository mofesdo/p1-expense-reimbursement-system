import selenium.common
from behave import when, then, given
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from utils.constants import site_url
from utils.constants import wait_time, wait_time_long
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given(u'I am on the login page')
def first_step(context):
    context.driver.maximize_window()
    context.driver.get(site_url)
    context.driver.implicitly_wait(wait_time)


@when(u'I enter {username} into the input field')
def step_impl(context, username):
    context.driver.implicitly_wait(wait_time)
    context.login_POM.username_input_field().send_keys(username)


@when(u'I enter {password} into the password field')
def step_impl(context, password):
    context.driver.implicitly_wait(wait_time)
    context.login_POM.password_input_field().send_keys(password)


@when(u'I click the submit button')
def step_impl(context):
    context.driver.implicitly_wait(wait_time)
    context.login_POM.submit_button().click()


@when(u'I click the create request button')
def step_impl(context):
    pass


@when(u'I enter {description} into the input field')
def step_impl(context):
    pass


@when(u'I enter {price} into the input field')
def step_impl(context):
    pass


@when(u'I enter {urgency} into the input field')
def step_impl(context):
    pass


@when(u'I enter {date} into the input field')
def step_impl(context):
    pass


@when(u'I click the submit button')
def step_impl(context):
    pass


@then(u'I should be on a page with the title {title}')
def step_impl(context, title):
    context.driver.implicitly_wait(wait_time)
    assert context.driver.title == title


@then(u'I will log out')
def final_step(context):
    if context.driver.title == "Dashboard":
        context.login_POM.logout_button().click()
    context.driver.implicitly_wait(wait_time)

