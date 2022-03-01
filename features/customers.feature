Feature: Customers
""" 
Confirm that we can browse the customer related pages on our site
"""

Scenario: success for visiting customer and customer details pages
    Given I navigate to the customer pages
    When I click on the link to customer details
    Then I should see the order for that customer
