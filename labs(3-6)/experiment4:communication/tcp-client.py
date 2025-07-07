import socket

HOST = 'localhost'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((HOST, PORT))
    client_socket.send(b'Hello server')
    response = client_socket.recv(1024)
    print(f"Received from server: {response.decode()}")
finally:
    client_socket.close()

