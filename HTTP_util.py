import http.server
import main
import globfile


def GET(path):
    def GET_concrete(func):
        globfile.requests_GET[path] = func
        return None
    return GET_concrete


class Request:
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
    def __init__(self, req: http.server.BaseHTTPRequestHandler):
        self.status_code = 200
        self.headers = {}
        self.message = "Dummy message"
