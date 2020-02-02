import json
import logging

from falcon import API, Request, Response


class PingResource(object):
    """
    Small resource for health checking.
    """

    def on_get(self, req: Request, res: Response):
        res.media = {"pong": True}


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
    }


def app():
    """
    Create our echo falcon app.
    """
    logging.basicConfig()
    logging.getLogger("falcon").setLevel(logging.DEBUG)
    api = API()
    api.add_route("/ping", PingResource())
    api.add_sink(and_the_kitchen_sink)
    return api
