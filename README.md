# Echo

An http echo service in python for the greatest infrastructure debug
information.

## Usage

Expose port `8000` on the container to the port of your choice:

```console
docker run -p 8000:8000 coreofscience/echo
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
        "USER-AGENT": "HTTPie/1.0.3"
    },
    "method": "GET",
    "params": {
        "q": "search"
    },
    "path": "/some/random/path",
    "payload": {
        "payload": "john"
    },
    "query": "q=search"
}
```


[httpie]: https://httpie.org/doc
