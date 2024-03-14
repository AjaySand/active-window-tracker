from http.server import BaseHTTPRequestHandler, HTTPServer
from tracker import loadFromFile
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.end_headers()

    def _set_json_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_GET(self):
        if self.path == '/':
            self._set_headers()

            self.wfile.write(b"Python http server up and running")

        elif(self.path == '/todays-activities'):
            self._set_json_headers()

            activities = loadFromFile({})

            self.wfile.write(json.dumps(activities).encode())

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Page not found")


def run():
    port = 9876
    ip = '0.0.0.0'
    server_address = (ip, port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Server running on port {port}")
    httpd.serve_forever()
