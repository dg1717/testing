from behave import *
from selenium import webdriver
from pages.my_page import MyPage

@given('I navigate to "{url}"')
def step_impl(context, url):
    context.driver = webdriver.Chrome()
    context.page = MyPage(context.driver)
    context.page.driver.get(url)

@then('I see the title is "{title}"')
def step_impl(context, title):
    assert context.page.page_title == title
