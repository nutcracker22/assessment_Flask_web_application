from behave import given, when, then

@given('I navigate to the main page')
def nav(context):
    """ 
    Navigate to the customers page
    """
    context.browser.get('http://localhost:5000/')

@when('I click on the link to a year')
def click(context):
    """ 
    Find the desired link
    """
    context.browser.find_element_by_partial_link_text('2021').click()

@then('I should see the movies released in that year')
def details(context):
    """ 
    if successful, then we should be directed to the year page
    """
    # use print(context.browser.page_source) to aid debugging
    print(context.browser.page_source)
    assert context.browser.current_url == 'http://localhost:5000/year/2'
    assert '2021' in context.browser.page_source

@then('I should not see any other year')
def details(context):
    """
    if successful, then we should not see any other year on the page
    """
    # use print(context.browser.page_source) to aid debugging
    print(context.browser.page_source)
    assert '2020' not in context.browser.page_source