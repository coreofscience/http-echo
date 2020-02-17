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

  Scenario Outline:
    Given our server is running with env "SERVICE_NAME": "sample"
    When we "<method>" to a sample endpoint
    Then we get an echo sample "<method>" response
    And the response tags include "SERVICE_NAME": "sample"

    Examples:
    | method |
    | get    |
    | post   |
    | put    |
    | patch  |