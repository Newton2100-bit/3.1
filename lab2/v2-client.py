# Client.py (Python):
import socket, time

start = time.perf_counter()
# Client setup with context manager
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect(('localhost', 12345))
    
    # Receiving data from server
    data = client_socket.recv(1024)
    print(f"Received message: {data.decode()}")
    
    # Socket automatically closes when exiting the with block
    end = time.perf_counter()
    final = end - start
    print(f'This took {final:.4f}s')
