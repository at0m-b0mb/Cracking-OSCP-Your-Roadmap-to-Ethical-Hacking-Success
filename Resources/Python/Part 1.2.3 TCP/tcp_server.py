import socket

def start_server():
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the local address and port
    server_socket.bind(('0.0.0.0', 12345))  # Listening on all interfaces at port 12345
    
    # Enable the server to accept connections
    server_socket.listen(1)
    print("Server listening on port 12345...")

    # Wait for a connection from a client
    conn, addr = server_socket.accept()
    print(f"Connection from {addr}")

    # Receive and send messages in a loop
    while True:
        # Receive data from the client
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"Received from client: {data}")

        # Send a response back to the client
        response = f"Server received: {data}"
        conn.send(response.encode())
    
    # Close the connection
    conn.close()

if __name__ == "__main__":
    start_server()
