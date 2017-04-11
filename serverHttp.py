import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

class S(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self._set_headers()
        self.wfile.write("hello")
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

def run(serve_class=http.server.HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = serve_class(server_address, handler_class)
    print("starting httpd...")
    httpd.serve_forever()

#with socketserver.TCPServer(("", PORT), Handler=S) as httpd:
#    print("serving at port", PORT)
#    httpd.serve_forever()

run()
