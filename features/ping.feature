Feature: ping endpoint

  Scenario: request the ping endpoint
    Given our server is running
    When we request the endpoint "/ping"
    Then we get a success json response

  Scenario Outline: other methods to the ping endpoint
    Given our server is running
    When we "<method>" to the endpoint "/ping"
    Then we get an invalid http method response

    Examples:
    | method |
    | post   |
    | put    |
    | patch  |