# Server.py (Python):
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Server is waiting for client connection...")
    
    client_socket, addr = server_socket.accept()
    with client_socket:
        print(f"Connection established with {addr}")
        # Sending data to client
        client_socket.send(b'Hello from server')
