import socket
import struct

MULTICAST_GROUP = '224.1.1.1'
PORT = 5007

# Create the UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind to the port
sock.bind(('', PORT))

# Join multicast group
group = socket.inet_aton(MULTICAST_GROUP)
mreq = struct.pack('4s4s', group, socket.inet_aton('0.0.0.0'))
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

print(f"Listening for multicast messages on {MULTICAST_GROUP}:{PORT}...")

while True:
    data, addr = sock.recvfrom(1024)
    print(f"Received from {addr}: {data.decode()}")

