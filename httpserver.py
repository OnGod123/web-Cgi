import socket

class HTTPServer:
    def __init__(self, host='localhost', port=8051):
        self.host = host
        self.port = port

    def handle_request(self, client_socket, request_data):
        # Parse the HTTP request
        request_lines = request_data.split('\r\n')
        method, path, _ = request_lines[0].split(' ')

        # Respond to GET requests
        if method == 'GET':
            self.send_response(client_socket, 200, [('Content-Type', 'text/html')])
            self.write(client_socket, '<h1>Hello, world!</h1>')
        # Respond to POST requests
        elif method == 'POST':
            content_length = int([line.split(': ')[1] for line in request_lines if line.startswith('Content-Length')][0])
            post_data = request_lines[-1]
            form_data = {}
            for key_value_pair in post_data.split('&'):
                key, value = key_value_pair.split('=')
                form_data[key] = value
            self.send_response(client_socket, 200, [('Content-Type', 'text/plain')])
            self.write(client_socket, f"Received form data: {form_data}")
        else:
            self.send_response(client_socket, 405, [('Content-Type', 'text/plain')])
            self.write(client_socket, 'Method not allowed')

    def send_response(self, client_socket, status, response_headers):
        status_line = f"HTTP/1.1 {status}\r\n"
        headers = ''.join([f"{header_name}: {header_value}\r\n" for header_name, header_value in response_headers])
        self.send(client_socket, status_line + headers + '\r\n')

    def write(self, client_socket, data):
        self.send(client_socket, data)

    def send(self, client_socket, data):
        client_socket.sendall(data.encode())

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((self.host, self.port))
            server_socket.listen()

            print(f'Server listening on {self.host}:{self.port}...')

            while True:
                client_socket, addr = server_socket.accept()
                with client_socket:
                    request_data = client_socket.recv(1024).decode()
                    if request_data:
                        self.handle_request(client_socket, request_data)

if __name__ == '__main__':
    server = HTTPServer()
    server.start()

