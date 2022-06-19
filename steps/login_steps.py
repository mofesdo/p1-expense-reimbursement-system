import selenium.common
from behave import when, then, given
from selenium.webdriver.support.select import Select
from utils.constants import site_url


@given(u'I am on the site')
def first_step(context):
    context.driver.get(site_url)


@given(u'If I am logged in, I will log out')
def logout_step(context):
    context.driver.implicitly_wait(1)
    try:
        context.login_POM.logout_button().click()
    except selenium.common.NoSuchElementException:
        pass


@when(u'I enter {username} into the input field')
def step_impl(context, username):
    context.login_POM.username_input_field().send_keys(username)


@when(u'I enter {password} into the password field')
def step_impl(context, password):
    context.login_POM.password_input_field().send_keys(password)


@when(u'I click the submit button')
def step_impl(context):
    context.login_POM.submit_button().click()


@then(u'I should be on a page with the title {title}')
def step_impl(context, title):
    assert context.driver.title == title

