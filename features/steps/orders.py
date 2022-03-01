from behave import given, when, then
import time

@given(u'I navigate to the orders page')
def nav(context):
    """ Read the table """
    for row in context.table:
        model.add_user(id=row['id'], name=row['name'])
    """
    Navigate to the orders page
    """
    context.browser.get('http://localhost:5000/orders')

@when(u'I click on the link to order details')
def click(context):
    """
    Find the desired link
    """
    context.browser.find_element_by_partial_link_text('3').click()
    time.sleep(3)

@then(u'I should see the order details including items for that order')
def details(context):
    """
    if successful, then we should be directed to the order details page
    """
    # use print(context.browser.page_source) to aid debugging
    print(context.browser.page_source)
    time.sleep(5)
    assert context.browser.current_url == 'http://localhost:5000/order_details/3'
    assert 'Lori Wilson' in context.browser.page_source