import socket

HOST = 'localhost'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"TCP Server listening on {HOST}:{PORT}...")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")
data = conn.recv(1024)
print(f"Received from client: {data.decode()}")
conn.send(b'Hello client')
conn.close()
server_socket.close()

