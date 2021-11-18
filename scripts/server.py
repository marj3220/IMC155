import http.server
import socketserver

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/scripts/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

def web_server():
    handler_object = MyHttpRequestHandler
    PORT = 8080
    with socketserver.TCPServer(("", PORT), handler_object) as httpd:
        httpd.serve_forever()