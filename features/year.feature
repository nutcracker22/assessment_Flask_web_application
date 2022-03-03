Feature: Customers
""" 
Confirm that we can browse the year-related pages on our site
"""

Scenario: success for visiting customer and customer details pages
    Given I navigate to the main page
    When I click on the link to a year
    Then I should see the movies released in that year
    And I should not see any other year
