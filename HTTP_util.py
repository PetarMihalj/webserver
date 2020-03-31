import http.server
import main
import globfile


def GET(path):
    """
    A decorator factory. Returns a decorator (GET_concrete), which captures the path variable.
    This means that the path variable is part of the returned function`s CLOSURE.

    Every handler method is then decorated with the returned function, in order to capture the reference to it in globfile.
    The same function is then overwritten with "None" in order to prevent accidents and abuse, such as calling such functions explicitly.
    """
    def GET_concrete(func):
        globfile.requests_GET[path] = func
        return None
    return GET_concrete


class Request:
    """
    A request wrapper exposes only the parts of BaseHTTPRequestHandler which website designer should have access to.
    Note: this is just a proof of concept, it needs some rework to be practical.
    """

    def __init__(self, req: http.server.BaseHTTPRequestHandler):
        self.client_address = req.client_address
        self.request_line = req.requestline
        self.headers = req.headers
        self.query_dict = dict()
        spl = req.path.split("?")
        if len(spl) > 1:
            query = spl[1]
            for keyval in query.split("&"):
                key, val = keyval.split("=")
                self.query_dict[key] = val


class Response:
    """
    Wraps the response parameters (which should be edited before returning from the handler function)
    """

    def __init__(self, req: http.server.BaseHTTPRequestHandler):
        self.status_code = 200
        self.headers = {}
        self.message = "Dummy message"
