import socket
import struct

MULTICAST_GROUP = '224.1.1.1'
PORT = 5007

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client_socket.bind(('', PORT))

group = socket.inet_aton(MULTICAST_GROUP)
mreq = struct.pack('4s4s', group, socket.inet_aton('0.0.0.0'))
client_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

while True:
    data, addr = client_socket.recvfrom(1024)
    print(f"Received message from {addr}: {data.decode()}")

