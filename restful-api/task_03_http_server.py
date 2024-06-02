#!/usr/bin/python3
import http.server
import socketserver
import json
import logging

logging.basicConfig(level=logging.INFO)

class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        logging.info(f"GET request, Path: {self.path}")
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = self.handle_request()
        self.wfile.write(json.dumps(response).encode('utf-8'))

    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            logging.info(f"POST request, Path: {self.path}, Data: {post_data}")
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = self.handle_request({"data": post_data})
            self.wfile.write(json.dumps(response).encode('utf-8'))
        except Exception as e:
            logging.error(f"Error handling POST request: {str(e)}")
            self.send_response(400)  # Bad Request
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))

    def handle_request(self, data=None):
        response = None
        if self.path == "/":
            response = self.handle_root()
        elif self.path == "/data":
            response = self.handle_data()
        elif self.path == "/status":
            response = self.handle_status()
        elif self.path == "/info":
            response = self.handle_info()
        else:
            response = {"error": "Endpoint not found"}
            self.send_response(404)
        return response

    def handle_root(self):
        response = {"message": "Hello, this is a simple API!"}
        return response

    def handle_data(self):
        response = {"data": {"name": "John", "age": 30, "city": "New York"}}
        return response

    def handle_status(self):
        response = {"status": "OK"}
        return response

    def handle_info(self):
        response = {"version": "1.0", "description": "A simple API built with http.server"}
        return response


PORT = 8000

# Use threading to avoid blocking the main thread
with socketserver.ThreadingTCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    logging.info(f"Serving at port {PORT}")
    httpd.serve_forever()
