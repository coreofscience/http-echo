from behave import given, then, when
from falcon.testing import TestClient
from grappa import should


from echo import app


@given('our server is running with env "{name}": "{value}"')
def step_impl(context, name, value):
    context.app = app({name: value})
    context.client = TestClient(context.app)


@given("our server is running")
def our_server_is_running(context):
    context.app = app()
    context.client = TestClient(context.app)


@when('we request the endpoint "{endpoint}"')
def we_get_endpoing(context, endpoint):
    context.resp = context.client.simulate_get(endpoint)


@then("we get a success json response")
def we_get_a_success_json_response(context):
    context.resp.status_code | should.be.equal.to(200)
    context.resp.json | should.be.equal.to({"pong": True})


@when('we "{method}" to the endpoint "{endpoint}"')
def we_hit_the_endpoint_with(context, method, endpoint):
    client: TestClient = context.client
    context.resp = client.simulate_request(method=method.upper(), path=endpoint)


@when('we "{method}" to a sample endpoint')
def we_hit_a_sample_endpoint_with(context, method):
    context.execute_steps(f'When we "{method}" to the endpoint "/sample"')


@then('we get an echo sample "{method}" response')
def we_get_an_echo_response(context, method):
    context.resp.json["method"] | should.be.equal.to(method.upper())
    context.resp.json["path"] | should.be.equal.to("/sample")
    with should(context.resp.json):
        should.be.a(dict)
        should.have.key("headers").to.be.a(dict)
        should.have.key("params").to.be.a(dict)
        should.have.key("payload").to.be.a(dict)
        should.have.key("query").to.be.a(str)


@then("we get an invalid http method response")
def we_get_an_invalid_http_method_response(context):
    context.resp.status_code | should.be.equal.to(405)
    context.resp.text | should.be.empty


@then('the response tags include "{name}": "{value}"')
def the_response_tags_include(context, name, value):
    with should(context.resp.json):
        should.have.key("tags").to.be.a(dict)
    with should(context.resp.json.get("tags")):
        should.have.key(name).that.should.be.equal.to(value)
