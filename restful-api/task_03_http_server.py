#!/usr/bin/python3
import http.server
import socketserver
import json
import logging

undefined_endpoints_errors = {
    "/invalid_endpoint": {"error": "Endpoint not found"},
}

logging.basicConfig(level=logging.INFO)

def handle_root(self):
    response = {"message": "Hello, world!"}
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()
    self.wfile.write(json.dumps(response).encode('utf-8'))

def handle_data(self):
    response = {"data": "This is some data"}
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()
    self.wfile.write(json.dumps(response).encode('utf-8'))

def handle_status(self):
    response = {"status": "The server is running"}
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()
    self.wfile.write(json.dumps(response).encode('utf-8'))

def handle_info(self):
    try:
        response = {"version": "1.0", "description": "A simple API built with http.server"}
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))
    except Exception as e:
        logging.error(f"Error handling info endpoint: {str(e)}")
        self.send_response(500)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))

class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        logging.info(f"GET request: {self.path}")
        if self.path == '/':
            handle_root(self)
        elif self.path == '/data':
            handle_data(self)
        elif self.path == '/status':
            handle_status(self)
        elif self.path == '/info':
            handle_info(self)
        else:
            if self.path in undefined_endpoints_errors:
                error_message = undefined_endpoints_errors[self.path]
            else:
                error_message = {"error": "Endpoint not found"}
            self.send_response(404)  # Ensure 404 for undefined endpoints
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(error_message).encode('utf-8'))

    def do_POST(self):
        logging.info(f"POST request: {self.path}")
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        try:
            data = json.loads(post_data.decode('utf-8'))
            #... logic to store or use the data
            self.send_response(201)  # Created
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"message": "Data received"}).encode('utf-8'))
        except Exception as e:
            logging.error(f"Error handling POST request: {str(e)}")
            self.send_response(400)  # Bad Request
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))

PORT = 8000

# Use threading to avoid blocking the main thread
with socketserver.ThreadingTCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    logging.info(f"Serving at port {PORT}")
    httpd.serve_forever()
