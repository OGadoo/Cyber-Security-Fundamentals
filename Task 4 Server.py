from http.server import SimpleHTTPRequestHandler, HTTPServer

class FileUploadHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        # Handle file uploads
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # Save the uploaded file
        with open('received_file', 'wb') as f:
            f.write(post_data)

        # Respond to the client
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"File received successfully!")

if __name__ == "__main__":
    host = "localhost"
    port = 8000
    server = HTTPServer((host, port), FileUploadHandler)
    print(f"Server running at http://{host}:{port}")
    server.serve_forever()