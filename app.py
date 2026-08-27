from http.server import BaseHTTPRequestHandler, HTTPServer
import os

PORT = int(os.environ.get("PORT", "8085"))

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        content = b"""
        <html>
        <head><title>Teacher Deployment Demo</title></head>
        <body style="font-family:Arial; text-align:center; padding:80px;">
            <h1>Deployment Successful</h1>
            <h2>Deployed from GitHub</h2>
            <p>This application was deployed through my Proxmox IaC Portal.</p>
            <p>GitHub -> Docker -> VM -> Web Application</p>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
