Feature: User should be able to login and create a new reimbursement request

  Scenario Outline:
    Given I am on the login page
    When I enter <username> into the input field
    And I enter <password> into the password field
    And I click the submit button
    When I click the create request button
    And I enter <description> into the input field
    And I enter <price> into the input field
    And I enter <urgency> into the input field
    And I enter <date> into the input field
    And I click the submit button
    Then I should be on a page with the title <title>
    And I will log out


    Examples:
            | username      | password      | title         | description        | price  | urgency | date        |
            | user_1        | pass_1        | Dashboard     | yo its user 1      | 123.43 | 0       | 06/19/2022  |
            | manager_1     | password      | Dashboard     | its the manager_1  | 420.69 | 1       | 06/19/2022  |
            | schnitzel     | pw            | Error         | error              | 222.22 | 1       | 06/19/2022  |