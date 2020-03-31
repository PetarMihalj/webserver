
import http.server as server
import HTTP_util
import globfile


class Handler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split("?")[0]
        if path in globfile.requests_GET:
            request = HTTP_util.Request(self)
            response = HTTP_util.Response(self)
            globfile.requests_GET[path](request, response)

            self.send_response(response.status_code)
            for h in response.headers:
                self.send_header(h, response.headers[h])
            self.end_headers()
            self.wfile.write(response.message)
        else:
            self.send_error(404, "No cats here")


if __name__ == "__main__":
    import sys
    import importlib
    for module_name in sys.argv[1:]:
        importlib.import_module(module_name)
    httpd = server.ThreadingHTTPServer(('', 8080), Handler)
    httpd.serve_forever()
