Feature: User should be able to login and create a new reimbursement request

  Scenario Outline:
    Given I am on the login page for request
    When I enter <username> into the username field for request
    And I enter <password> into the password field for request
    And I click the login button for request
    When I click the create request button for request
    And I enter <description> into the description field for request
    And I enter <price> into the price field for request
    And I enter <urgency> into the urgency field for request
    And I enter <date> into the date field for request
    And I click the submit button for request
    Then I should be on a page with the title <title> for request
    And I will log out for request


    Examples:
            | username      | password      | title         | description        | price  | urgency | date        |
            | user_1        | pass_1        | Dashboard     | yo its user 1      | 123.43 | 0       | 06/19/2022  |
            | manager_1     | password      | Dashboard     | its the manager_1  | 420.69 | 1       | 06/19/2022  |
            | schnitzel     | pw            | Error         | error              | 222.22 | 1       | 06/19/2022  |
            | manager_1     | password      | Error         | ``                 | 222.22 | 1       | 06/19/2022  |
            | manager_1     | password      | Error         | error price        | 1222.22| 1       | 06/19/2022  |
            | manager_1     | password      | Dashboard     | make urgency = 0   | 222.22 | 3       | 06/19/2022  |