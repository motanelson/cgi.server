from http.server import CGIHTTPRequestHandler, HTTPServer
print("\033c\033[43;30m\n")
PORT = 5000
handler = CGIHTTPRequestHandler

with HTTPServer(("", PORT), handler) as httpd:
    print('Servidor a correr em http://localhost:'+str(PORT))
    httpd.serve_forever()