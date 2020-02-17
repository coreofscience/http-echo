import json
import logging
import os

from falcon import API, Request, Response


class PingResource(object):
    """
    Small resource for health checking.
    """

    def on_get(self, req: Request, res: Response):
        res.media = {"pong": True}


def sink(environment):
    def and_the_kitchen_sink(req: Request, res: Response):
        """
        Handle all request with their payload.
        """
        res.media = {
            "path": req.path,
            "params": req.params,
            "method": req.method,
            "headers": req.headers,
            "query": req.query_string,
            "payload": json.loads(req.bounded_stream.read() or "{}"),
            "tags": {
                name: value
                for name, value in environment.items()
                if name.startswith("SERVICE_")
            },
        }

    return and_the_kitchen_sink


def app(environment=None):
    """
    Create our echo falcon app.
    """
    if environment is None:
        environment = os.environ
    logging.basicConfig()
    logging.getLogger("falcon").setLevel(logging.DEBUG)
    api = API()
    api.add_route("/ping", PingResource())
    api.add_sink(sink(environment))
    return api
