def application(environ, start_response):
    """WSGI application function."""
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)
    return [b"Hello, World!"]

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    # Create a simple WSGI server
    server = make_server('localhost', 8000, application)
    print("Serving on port 8000...")

    # Start the server
    server.serve_forever()

