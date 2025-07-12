import socket
import threading
import time
import json
from datetime import datetime

class Node:
    def __init__(self, id, port):
        self.id = id
        self.port = port
        self.host = 'localhost'
        self.request_queue = []
        self.socket = None
        self.peers = {}  # Dictionary to store peer connections
        self.running = False
        
    def start_server(self):
        """Start the server socket to listen for incoming connections"""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        self.running = True
        
        print(f"Node {self.id} started server on {self.host}:{self.port}")
        
        # Start listening for connections in a separate thread
        server_thread = threading.Thread(target=self._accept_connections)
        server_thread.daemon = True
        server_thread.start()
        
    def _accept_connections(self):
        """Accept incoming connections from other nodes"""
        while self.running:
            try:
                client_socket, addr = self.socket.accept()
                print(f"Node {self.id} accepted connection from {addr}")
                
                # Handle each client in a separate thread
                client_thread = threading.Thread(
                    target=self._handle_client, 
                    args=(client_socket,)
                )
                client_thread.daemon = True
                client_thread.start()
                
            except Exception as e:
                if self.running:
                    print(f"Node {self.id} error accepting connections: {e}")
                break
    
    def _handle_client(self, client_socket):
        """Handle messages from a connected client"""
        try:
            while self.running:
                data = client_socket.recv(1024)
                if not data:
                    break
                    
                message = json.loads(data.decode())
                self._process_message(message)
                
        except Exception as e:
            print(f"Node {self.id} error handling client: {e}")
        finally:
            client_socket.close()
    
    def _process_message(self, message):
        """Process received messages"""
        msg_type = message.get('type')
        from_id = message.get('from_id')
        
        if msg_type == 'REQUEST':
            timestamp = message.get('timestamp')
            print(f"Node {self.id} received REQUEST from Node {from_id} at time {timestamp}")
            
            # Send reply back
            self.send_reply(from_id)
            
        elif msg_type == 'REPLY':
            print(f"Node {self.id} received REPLY from Node {from_id}")
    
    def connect_to_peer(self, peer_id, peer_port):
        """Connect to another node"""
        try:
            peer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            peer_socket.connect((self.host, peer_port))
            self.peers[peer_id] = peer_socket
            print(f"Node {self.id} connected to Node {peer_id}")
            return True
        except Exception as e:
            print(f"Node {self.id} failed to connect to Node {peer_id}: {e}")
            return False
    
    def send_message(self, peer_id, message):
        """Send a message to a specific peer"""
        if peer_id in self.peers:
            try:
                message_json = json.dumps(message)
                self.peers[peer_id].send(message_json.encode())
                return True
            except Exception as e:
                print(f"Node {self.id} failed to send message to Node {peer_id}: {e}")
                return False
        else:
            print(f"Node {self.id} not connected to Node {peer_id}")
            return False
    
    def request_cs(self, timestamp):
        """Request critical section access"""
        print(f"Node {self.id} requests CS at time {timestamp}")
        
        # Send request to all connected peers
        request_message = {
            'type': 'REQUEST',
            'from_id': self.id,
            'timestamp': timestamp
        }
        
        for peer_id in self.peers:
            self.send_message(peer_id, request_message)
        
        return f"REQ from {self.id} at {timestamp}"
    
    def send_reply(self, to_id):
        """Send reply to a node"""
        reply_message = {
            'type': 'REPLY',
            'from_id': self.id
        }
        
        if self.send_message(to_id, reply_message):
            print(f"Node {self.id} sent REPLY to Node {to_id}")
    
    def shutdown(self):
        """Shutdown the node"""
        self.running = False
        
        # Close peer connections
        for peer_socket in self.peers.values():
            peer_socket.close()
        
        # Close server socket
        if self.socket:
            self.socket.close()
        
        print(f"Node {self.id} shutdown complete")

def main():
    # Create two nodes with different ports
    node1 = Node(1, 8001)
    node2 = Node(2, 8002)
    
    # Start both nodes
    node1.start_server()
    node2.start_server()
    
    # Give servers time to start
    time.sleep(1)
    
    # Connect nodes to each other
    node1.connect_to_peer(2, 8002)
    node2.connect_to_peer(1, 8001)
    
    # Give connections time to establish
    time.sleep(1)
    
    print("\n--- Simulation Starts Here ---")
    
    # Both nodes request to enter the critical section with different timestamps
    req1 = node1.request_cs(5)
    req2 = node2.request_cs(4)
    
    # Give time for message exchange
    time.sleep(2)
    
    # Decide which node gets access based on timestamp
    print(f"\nDecision: Comparing timestamps...")
    if 5 > 4:  # Node 1's timestamp (5) vs Node 2's timestamp (4)
        print("Node 2 gets CS (lower timestamp)")
    else:
        print("Node 1 gets CS (lower timestamp)")
    
    # Keep the simulation running for a bit to see all messages
    time.sleep(2)
    
    # Cleanup
    node1.shutdown()
    node2.shutdown()

if __name__ == "__main__":
    main()
