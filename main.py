
import http.server as server
import HTTP_util
import globfile


class Handler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split("?")[0]
        if path in globfile.requests_GET:
            request = HTTP_util.Request(self)
            response = HTTP_util.Response(self)

            # Calls the handler function
            globfile.requests_GET[path](request, response)

            # Unwraps the response, prepares it for sending back.
            self.send_response(response.status_code)
            for h in response.headers:
                self.send_header(h, response.headers[h])
            self.end_headers()

            # Send the response
            self.wfile.write(response.message)
        else:
            # Wrong request
            self.send_error(404, "No cats here")


if __name__ == "__main__":
    import sys
    import importlib

    # Importing modules given in arguments
    for module_name in sys.argv[1:]:
        importlib.import_module(module_name)

    # Feel free to bind it to other addresses/ports
    httpd = server.ThreadingHTTPServer(('', 8080), Handler)
    httpd.serve_forever()
