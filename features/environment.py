from behave import fixture, use_fixture
from falcon.testing import TestClient

from echo import app


@fixture
def app_client(context):
    context.app = app()
    context.client = TestClient(context.app)


def before_all(context):
    use_fixture(app_client, context)
