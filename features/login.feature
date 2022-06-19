Feature: I can log in and out, and only valid credentials work

    Scenario Outline:
        Given I am on the login page
        When I enter <username> into the input field
        When I enter <password> into the password field
        When I click the submit button
        Then I should be on a page with the title <title>
        And I will log out


        Examples:
            | username      | password      | title         |
            | user_1        | pass_1        | Dashboard     |
            | manager_1     | password      | Dashboard     |
            | schnitzel     | pw            | Error         |