import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))
client_socket.send(b'Hello server')
response = client_socket.recv(1024)
print(f"Received from server: {response.decode()}")
client_socket.close()
# server.py
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("Server is listening on port 12345...")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")
data = conn.recv(1024)
print(f"Received: {data.decode()}")
conn.send(b'Hello client')
conn.close()
server_socket.close()

