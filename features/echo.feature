Feature: Echo

  Scenario Outline:
    Given our server is running
    When we "<method>" to a sample endpoint
    Then we get an echo sample "<method>" response

    Examples:
    | method |
    | get    |
    | post   |
    | put    |
    | patch  |