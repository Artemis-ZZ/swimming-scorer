#!/usr/bin/env python3
"""Simple HTTP server for the swimming scorer PWA."""
import http.server
import socket
import os

PORT = 8080
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()

print(f"""
🏊 游泳课成绩管理系统

  电脑访问: http://localhost:{PORT}
  手机访问: http://{socket.gethostbyname(socket.gethostname())}:{PORT}

  按 Ctrl+C 停止服务器
""")
http.server.HTTPServer(('0.0.0.0', PORT), Handler).serve_forever()
