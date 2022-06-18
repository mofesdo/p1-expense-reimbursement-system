from behave import when, then
from selenium.webdriver.support.select import Select

@when(u'I enter {username} into the input field')
def step_impl(context, username):
    context.wiki_home.search_bar().send_keys(username)


@when(u'I enter {password} into the input field')
def step_impl(context, language):
    context.wiki_home.language_selector().select_by_value(language)


@when(u'I click the submit button')
def step_impl(context):
    context.wiki_home.search_button().click()


@then(u'I should be on a page with the title {title}')
def step_impl(context, title):
    assert context.driver.title == title

