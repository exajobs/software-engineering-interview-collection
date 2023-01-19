import os
from typing import Callable, Any
from wsgiref.simple_server import make_server


class DataStorageServer:

    def __init__(self) -> None:
        pass

    def __call__(self, environ: dict[str, Any], start_response: Callable[..., Any]) -> bytes:
        """
        The environ parameter is a dictionary containing some useful
        HTTP request information such as: REQUEST_METHOD, CONTENT_LENGTH,
        PATH_INFO, CONTENT_TYPE, etc.
        For the full list of attributes refer to wsgi definitions:
        https://wsgi.readthedocs.io/en/latest/definitions.html
        """

        # Download an object
        # GET /data/{repository}/{object_id}
        # Response
        # Status: 200 OK
        # {object data}
        if environ["REQUEST_METHOD"] == "GET":
            # This implementation of GET is incomplete at this time and won't
            # pass the tests, please improve it.
            body = b""
            status = "200 OK"
            response_headers = [("Content-Type", "text/plain")]

        start_response(status, response_headers)
        yield body


if __name__ == "__main__":
    app = DataStorageServer()
    port = os.environ.get('PORT', 8282)
    with make_server("", port, app) as httpd:
        print(f"Listening on port {port}...")
        httpd.serve_forever()
