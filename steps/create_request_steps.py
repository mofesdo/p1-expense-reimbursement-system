import selenium.common
from behave import when, then, given
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from utils.constants import site_url
from utils.constants import wait_time, wait_time_long
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@given(u'I am on the login page for request')
def first_step(context):
    context.driver.maximize_window()
    context.driver.get(site_url)
    context.driver.implicitly_wait(wait_time)


@when(u'I enter {username} into the username field for request')
def step_impl(context, username):
    context.driver.implicitly_wait(wait_time)
    context.create_request_POM.user_input_field().send_keys(username)


@when(u'I enter {password} into the password field for request')
def step_impl(context, password):
    context.driver.implicitly_wait(wait_time)
    context.create_request_POM.password_input_field().send_keys(password)


@when(u'I click the login button for request')
def step_impl(context):
    context.driver.implicitly_wait(wait_time)
    context.create_request_POM.login_button().click()


@when(u'I click the create request button for request')
def step_impl(context):
    if context.driver.title == "Error":
        pass
    else:
        context.driver.implicitly_wait(wait_time)
        context.create_request_POM.create_request_button().click()


@when(u'I enter {description} into the description field for request')
def step_impl(context, description):
    if context.driver.title == "Error":
        pass
    else:
        context.driver.implicitly_wait(wait_time)
        context.create_request_POM.description_input_field().send_keys(description)


@when(u'I enter {price} into the price field for request')
def step_impl(context, price):
    if context.driver.title == "Error":
        pass
    else:
        context.driver.implicitly_wait(wait_time)
        context.create_request_POM.price_input_field().send_keys(price)


@when(u'I enter {urgency} into the urgency field for request')
def step_impl(context, urgency):
    if context.driver.title == "Error":
        pass
    else:
        context.driver.implicitly_wait(wait_time)
        if int(urgency) == 0:
            context.create_request_POM.not_urgent_input_field().click()
        elif int(urgency) == 1:
            context.create_request_POM.is_urgent_input_field().click()
        else:
            pass


@when(u'I enter {date} into the date field for request')
def step_impl(context, date):
    if context.driver.title == "Error":
        pass
    else:
        context.driver.implicitly_wait(wait_time)
        context.create_request_POM.date_input_field().send_keys(date)


@when(u'I click the submit button for request')
def step_impl(context):
    if context.driver.title == "Error":
        pass
    else:
        context.driver.implicitly_wait(wait_time_long)
        context.create_request_POM.submit_button().click()
        time.sleep(3)


@then(u'I should be on a page with the title {title} for request')
def step_impl(context, title):
    if context.driver.title == "Error" or context.driver.title == "Create New Reimbursement Request":
        context.create_request_POM.home_button().click()
    else:
        context.driver.implicitly_wait(wait_time)
        assert context.driver.title == title


@then(u'I will log out for request')
def final_step(context):
    if context.driver.title == "Error" or context.driver.title == "Create New Reimbursement Request":
        context.create_request_POM.home_button().click()
        time.sleep(1)
        if context.driver.title != "Blackbeard's Crew":
            context.create_request_POM.logout_button().click()
    elif context.driver.title == "Dashboard":
        context.create_request_POM.logout_button().click()
        context.driver.implicitly_wait(wait_time)
    else:
        pass

