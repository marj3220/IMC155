import http.server
import socketserver

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/scripts/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Create an object of the above class
#handler_object = MyHttpRequestHandler
handler_object = http.server.SimpleHTTPRequestHandler

PORT = 8080
with socketserver.TCPServer(("", PORT), handler_object) as httpd:
    httpd.serve_forever()