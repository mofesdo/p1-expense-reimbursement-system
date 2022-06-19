Feature: I can search for content in different languages using the same search bar

    Scenario Outline:
        Given If I am logged in, I will log out
        Given I am on the site
        When I enter <username> into the input field
        When I enter <password> into the password field
        When I click the submit button
        Then I should be on a page with the title <title>


        Examples:
            | username      | password      | title         |
            | user_1        | pass_1        | Dashboard     |
            | manager_1     | password      | Dashboard     |
            | Schnitzel     | de            | Dashboard     |