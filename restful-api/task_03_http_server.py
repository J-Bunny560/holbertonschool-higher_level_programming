#!/usr/bin/python3
import http.server
import socketserver
import json
import logging

# Set up logging
logging.basicConfig(filename='api.log', level=logging.INFO)

# Define error messages for undefined endpoints
undefined_endpoints_errors = {
    "/undefined_endpoint_1": {"error": "Endpoint 1 not found"},
    "/undefined_endpoint_2": {"error": "Endpoint 2 not found"},
    # Add more undefined endpoints as needed
}

def handle_root(self):
    try:
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Hello, this is a simple API!")
    except Exception as e:
        logging.error(f"Error handling root endpoint: {str(e)}")
        self.send_response(500)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))

def handle_data(self):
    try:
        # Sample data instead of reading from a file
        data = {
            "message": "This is sample data from the API",
            "items": [
                {"name": "Item 1"},
                {"name": "Item 2"}
            ]
        }
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))
    except Exception as e:
        logging.error(f"Error handling data endpoint: {str(e)}")
        self.send_response(500)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))

def handle_status(self):
    try:
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"OK")
    except Exception as e:
        logging.error(f"Error handling status endpoint: {str(e)}")
        self.send_response(500)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))

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
            self.send_response(404)
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
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
