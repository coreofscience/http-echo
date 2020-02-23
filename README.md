# Echo

An http echo service in python for the greatest infrastructure debug
information.

## Usage

Expose port `8000` on the container to the port of your choice:

```console
docker run -e SERVICE_NAME=auth -p 8000:8000 coreofscience/echo
```

Then you can see your requests echoed away with [httpie]:

```console
http get localhost:8000/some/random/path q==search payload=john
```

You should see all the info about the request like so:

```json
{
    "headers": {
        "ACCEPT": "application/json, */*",
        "ACCEPT-ENCODING": "gzip, deflate",
        "CONNECTION": "keep-alive",
        "CONTENT-LENGTH": "19",
        "CONTENT-TYPE": "application/json",
        "HOST": "localhost:8000",
        "USER-AGENT": "HTTPie/2.0.0"
    },
    "method": "GET",
    "params": {
        "q": "search"
    },
    "path": "/some/random/path",
    "payload": {
        "payload": "john"
    },
    "query": "q=search",
    "tags": {
        "SERVICE_NAME": "auth"
    }
}
```

### Use cases

Use this whenever you don't know where  request is going in your
infrastructure. If you, for instance, are not sure if a request path is going
to be trimmed by a load balancer or something like that.

[httpie]: https://httpie.org/doc
