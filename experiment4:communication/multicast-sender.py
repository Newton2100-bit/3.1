import socket
import struct
import time

MULTICAST_GROUP = '224.1.1.1'
PORT = 5007

# Create the UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set TTL for multicast packets
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

while True:
    message = b"Hello from multicast sender"
    sock.sendto(message, (MULTICAST_GROUP, PORT))
    print("Sent multicast message.")
    time.sleep(2)

