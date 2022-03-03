from behave import *

use_step_matcher("re")


@given("I navigate to the movies page")
def nav(context):
    """
    Navigate to the movies page
    """
    context.browser.get('http://localhost:5000/movies')


@when("I click on the link to a movie")
def click(context):
    """
    Find the desired link
    """
    context.browser.find_element_by_partial_link_text('Home Team').click()


@then("I should see the details of the movie")
def details(context):
    """
    if successful, then we should be directed to the movie_details page
    """
    # use print(context.browser.page_source) to aid debugging
#    print(context.browser.page_source)
    assert context.browser.current_url == 'http://localhost:5000/movie_details/6'
    assert 'Home Team' in context.browser.page_source