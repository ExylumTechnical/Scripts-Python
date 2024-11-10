import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import cgi

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Create upload folder if it doesn't exist

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Serve the upload form and list uploaded files
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            files = os.listdir(UPLOAD_FOLDER)
            file_links = "\n".join([f'<li><a href="/{UPLOAD_FOLDER}/{file}">{file}</a></li>' for file in files])

            html = f"""
            <html>
            <body>
                <h1>Upload File</h1>
                <form method="post" enctype="multipart/form-data">
                    <input type="file" name="file">
                    <input type="submit" value="Upload">
                </form>
                <h2>Uploaded Files</h2>
                <ul>{file_links}</ul>
            </body>
            </html>
            """
            self.wfile.write(html.encode())
        else:
            # Serve uploaded files
            filepath = self.path.lstrip('/')
            if os.path.isfile(filepath):
                self.send_response(200)
                self.send_header("Content-type", "application/octet-stream")
                self.send_header("Content-Disposition", f'attachment; filename="{os.path.basename(filepath)}"')
                self.end_headers()
                with open(filepath, 'rb') as f:
                    self.wfile.write(f.read())
            else:
                self.send_error(404, "File Not Found")

    def do_POST(self):
        # Handle file upload
        content_type, pdict = cgi.parse_header(self.headers['Content-Type'])
        if content_type == 'multipart/form-data':
            form = cgi.FieldStorage(fp=self.rfile, headers=self.headers, environ={'REQUEST_METHOD': 'POST'})
            if 'file' in form:
                file_field = form['file']
                filename = os.path.basename(file_field.filename)
                filepath = os.path.join(UPLOAD_FOLDER, filename)

                with open(filepath, 'wb') as f:
                    f.write(file_field.file.read())

                self.send_response(303)
                self.send_header("Location", "/")
                self.end_headers()
            else:
                self.send_error(400, "No file uploaded")
        else:
            self.send_error(400, "Content-Type must be multipart/form-data")

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()