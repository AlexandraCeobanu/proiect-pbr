from http.server import BaseHTTPRequestHandler, HTTPServer
import clips_solver
import json
import validation

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def _set_cors_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')

    def do_OPTIONS(self):
        self.send_response(200)
        self._set_cors_headers()
        self.end_headers()

    def do_GET(self):
        if self.path.startswith("/syllogism-solver"):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'{"Message": "Welcome to Syllogism Solver!"}')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'{"Error": "The requested page was not found"}')

    def do_POST(self):
        if self.path == "/solve":
            content_type = self.headers.get('Content-Type')

            if content_type != 'application/json':
                self.response(415)
                self._set_cors_headers()
                self.end_headers()
                self.wfile.write(b'{"Error": "Data interchange format is JSON!"}')
            else:
                content_lenght = int(self.headers['Content-length'])
                post_data = self.rfile.read(content_lenght)
                premises = json.loads(post_data.decode('utf-8'))

                type1, subject1, predicate1, verb1 = validation.validate(premises[0]["type"], premises[0]["sentence"])
                type2, subject2, predicate2, verb2 = validation.validate(premises[1]["type"], premises[1]["sentence"])

                if type1 == -1 or type2 == -1:
                    self.send_response(422)
                    self._set_cors_headers()
                    self.end_headers()
                    self.wfile.write(b'{"Error": "One or both premises are invalid! You should have a sentence with a subject (one or two words), a verb (optional +not) and a predicate(one or two words)"}')
                else:
                    conclusion = clips_solver.solve(type1, type2, subject1, subject2, predicate1, predicate2)
                    print(conclusion)

                    if len(conclusion):
                        self.send_response(200)
                        self._set_cors_headers()
                        self.end_headers()
                        response = f'{{"Conclusion": "{conclusion}"}}'
                        self.wfile.write(response.encode('utf-8'))

                    else:
                        print(premises)
                        self.send_response(404)
                        self._set_cors_headers()
                        self.end_headers()
                        self.wfile.write(b'{"Error: We cannot solve the syllogism based on your premises."}')
        else:
            self.send_response(421)
            self._set_cors_headers()
            self.end_headers()
            self.wfile.write(b'{"Error: Misdirected Request"}')


host = 'localhost'
port = 8000

server = HTTPServer((host, port), MyHTTPRequestHandler)
print(f"Server started on {host}:{port}")
server.serve_forever()



