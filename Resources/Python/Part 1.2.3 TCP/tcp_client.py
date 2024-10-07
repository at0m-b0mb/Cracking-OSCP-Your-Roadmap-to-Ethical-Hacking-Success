import socket

def start_client():
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server at localhost on port 12345
    client_socket.connect(('127.0.0.1', 12345))
    print("Connected to server...")

    # Send and receive messages
    while True:
        message = input("Enter message to send to the server (or type 'exit' to quit): ")
        if message.lower() == 'exit':
            break

        # Send the message to the server
        client_socket.send(message.encode())
        
        # Receive the response from the server
        response = client_socket.recv(1024).decode()
        print(f"Response from server: {response}")
    
    # Close the socket
    client_socket.close()

if __name__ == "__main__":
    start_client()
