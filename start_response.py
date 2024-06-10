def start_response(status, response_headers):
    """
    A simple implementation of start_response.
    
    Args:
        status (str): The HTTP status code and message (e.g., "200 OK").
        response_headers (list): A list of tuples containing HTTP headers.

    Returns:
        function: A function to send data to the client.
    """
    # Format the status line
    status_line = f"HTTP/1.1 {status}\r\n"
    
    # Format the headers
    headers = ''
    for header_name, header_value in response_headers:
        headers += f"{header_name}: {header_value}\r\n"
    
    # Concatenate the status line and headers
    response = status_line + headers + '\r\n'
    
    # Return a function to send data to the client
    def send_response_data(data):
        """
        A function to send data to the client.

        Args:
            data (bytes): The data to be sent to the client.
        """
        # Encode the data as bytes if it's not already
        if isinstance(data, str):
            data = data.encode()
        
        # Send the response to the client
        client_socket.sendall(response.encode() + data)
    
    return send_response_data

