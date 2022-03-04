# Created by nutcracker22 at 04.03.22
Feature: Movie details
  """
  Confirm that we can browse the movie_details pages on our site
  """

  Scenario: Success for visiting movie_details pages
    Given I navigate to the movies page
    When I click on the link to a movie
    Then I should see the details of the movie
