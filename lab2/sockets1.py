import socket

def create_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 8080))
    server.listen(1)
    
    print("Server listening on port 8080...")
    client, addr = server.accept()
    print(f"Connection from {addr}")
    
    # Send different types of messages
    client.send(b'Welcome to the server!\n')
    client.send('Current time: 2024-01-15\n'.encode())
    client.send(f'Your IP: {addr[0]}\n'.encode())
    
    # Receive data
    data = client.recv(1024)
    if data:
        message = data.decode()
        print(f"Client said: {message}")
        
        # Echo back
        response = f"Server received: {message}"
        client.send(response.encode())
    
    client.close()
    server.close()
