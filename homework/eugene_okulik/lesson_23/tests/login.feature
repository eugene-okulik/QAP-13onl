Feature: login page

    Scenario: incorrect login alert
    Given I am on the login page
    When I enter non-existing user email into email field
    And I enter correct password
    And I click Sign In button
    Then I see alert message

    Scenario: password validation displayed
    Given I am on the login page
    When I enter correct email
    And I click Sign In button
    Then I see password validation
