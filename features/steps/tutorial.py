from behave import given, when, then
from falcon.testing import TestClient


@given("our server is running")
def our_server_is_running(context):
    assert context.app is not None
    assert context.client is not None


@when('we request the endpoint "{endpoint}"')
def we_get_endpoing(context, endpoint):
    context.resp = context.client.simulate_get(endpoint)


@then("we get a success json response")
def we_get_a_success_json_response(context):
    assert context.resp.status_code == 200
    assert context.resp.json == {"pong": True}


@when('we "{method}" to the endpoint "{endpoint}"')
def we_hit_the_endpoint_with(context, method, endpoint):
    client: TestClient = context.client
    context.resp = client.simulate_request(method=method, path=endpoint)


@then("we get an echo response")
def we_get_an_echo_response(context):
    assert context.resp.json["method"] == context.resp.request.method
    # TODO: Continue this one


@then(u"we get an invalid http method response")
def we_get_an_invalid_http_method_response(context):
    assert context.resp.status_code == 400
    assert context.resp.json == {
        "title": "Bad request",
        "description": "Invalid HTTP method",
    }

