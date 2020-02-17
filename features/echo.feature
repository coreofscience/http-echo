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
    And response "tags" includes "SERVICE_NAME": "sample"

    Examples:
    | method |
    | get    |
    | post   |
    | put    |
    | patch  |

  Scenario:
    Given our server is running with env "SERVICE_NAME": "sample"
    When we post to a sample endpoint with payload
      """
      {
        "key": "value",
        "foo": "bar"
      }
      """
    Then response "payload" includes "key": "value"
    Then response "payload" includes "foo": "bar"
