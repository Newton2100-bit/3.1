import socket
import threading
import time
import json
import random
from datetime import datetime
from enum import Enum

class NodeState(Enum):
    IDLE = "IDLE"
    REQUESTING = "REQUESTING"
    IN_CS = "IN_CS"

class Node:
    def __init__(self, id, port):
        self.id = id
        self.port = port
        self.host = 'localhost'
        self.socket = None
        self.peers = {}  # Dictionary to store peer connections
        self.running = False
        
        # Mutual exclusion state
        self.state = NodeState.IDLE
        self.logical_clock = 0
        self.request_timestamp = None
        self.replies_received = 0
        self.total_peers = 0
        
        # Deferred reply queue - stores requests that need to be replied to later
        self.deferred_replies = []  # List of (node_id, timestamp) tuples
        self.lock = threading.Lock()  # Thread safety for shared state
        
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
                
                # Simulate network delays
                time.sleep(random.uniform(0.1, 0.5))
                
                # Simulate message loss (5% chance)
                if random.random() < 0.05:
                    print(f"Node {self.id} - Message lost due to network failure")
                    continue
                    
                message = json.loads(data.decode())
                self._process_message(message)
                
        except Exception as e:
            print(f"Node {self.id} error handling client: {e}")
        finally:
            client_socket.close()
    
    def _process_message(self, message):
        """Process received messages"""
        with self.lock:
            msg_type = message.get('type')
            from_id = message.get('from_id')
            timestamp = message.get('timestamp', 0)
            
            # Update logical clock
            self.logical_clock = max(self.logical_clock, timestamp) + 1
            
            if msg_type == 'REQUEST':
                print(f"Node {self.id} received REQUEST from Node {from_id} at time {timestamp}")
                self._handle_request(from_id, timestamp)
                
            elif msg_type == 'REPLY':
                print(f"Node {self.id} received REPLY from Node {from_id}")
                self._handle_reply(from_id)
    
    def _handle_request(self, from_id, timestamp):
        """Handle CS request from another node"""
        should_reply_now = True
        
        if self.state == NodeState.IN_CS:
            # Currently in CS - defer the reply
            should_reply_now = False
            print(f"Node {self.id} is in CS - deferring reply to Node {from_id}")
            
        elif self.state == NodeState.REQUESTING:
            # Both nodes are requesting - use timestamp ordering
            if (timestamp < self.request_timestamp or 
                (timestamp == self.request_timestamp and from_id < self.id)):
                # Other node has priority - defer our request and reply now
                should_reply_now = True
                print(f"Node {self.id} - Node {from_id} has priority (timestamp: {timestamp} vs {self.request_timestamp})")
            else:
                # We have priority - defer the reply
                should_reply_now = False
                print(f"Node {self.id} has priority - deferring reply to Node {from_id}")
        
        if should_reply_now:
            self.send_reply(from_id)
        else:
            # Add to deferred replies queue
            self.deferred_replies.append((from_id, timestamp))
            print(f"Node {self.id} - Added Node {from_id} to deferred replies queue")
    
    def _handle_reply(self, from_id):
        """Handle reply from another node"""
        if self.state == NodeState.REQUESTING:
            self.replies_received += 1
            print(f"Node {self.id} - Received {self.replies_received}/{self.total_peers} replies")
            
            if self.replies_received == self.total_peers:
                # All replies received - can enter CS
                self._enter_critical_section()
    
    def _enter_critical_section(self):
        """Enter the critical section"""
        self.state = NodeState.IN_CS
        print(f"\n🔒 Node {self.id} ENTERED CRITICAL SECTION at logical time {self.logical_clock}")
        
        # Simulate work in CS
        time.sleep(2)
        
        self._exit_critical_section()
    
    def _exit_critical_section(self):
        """Exit the critical section and process deferred replies"""
        print(f"🔓 Node {self.id} EXITED CRITICAL SECTION")
        
        self.state = NodeState.IDLE
        
        # Process all deferred replies
        print(f"Node {self.id} - Processing {len(self.deferred_replies)} deferred replies")
        for node_id, timestamp in self.deferred_replies:
            print(f"Node {self.id} - Sending deferred reply to Node {node_id}")
            self.send_reply(node_id)
        
        # Clear the deferred replies queue
        self.deferred_replies.clear()
    
    def connect_to_peer(self, peer_id, peer_port):
        """Connect to another node"""
        try:
            peer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            peer_socket.connect((self.host, peer_port))
            self.peers[peer_id] = peer_socket
            self.total_peers += 1
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
    
    def request_cs(self):
        """Request critical section access"""
        with self.lock:
            if self.state != NodeState.IDLE:
                print(f"Node {self.id} - Already requesting or in CS")
                return
            
            self.state = NodeState.REQUESTING
            self.logical_clock += 1
            self.request_timestamp = self.logical_clock
            self.replies_received = 0
            
            print(f"Node {self.id} requests CS at logical time {self.request_timestamp}")
            
            # Send request to all connected peers
            request_message = {
                'type': 'REQUEST',
                'from_id': self.id,
                'timestamp': self.request_timestamp
            }
            
            for peer_id in self.peers:
                self.send_message(peer_id, request_message)
    
    def send_reply(self, to_id):
        """Send reply to a node"""
        reply_message = {
            'type': 'REPLY',
            'from_id': self.id,
            'timestamp': self.logical_clock
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
    # Create three nodes for better demonstration
    node1 = Node(1, 8001)
    node2 = Node(2, 8002)
    node3 = Node(3, 8003)
    
    nodes = [node1, node2, node3]
    
    # Start all nodes
    for node in nodes:
        node.start_server()
    
    # Give servers time to start
    time.sleep(1)
    
    # Connect nodes to each other (full mesh)
    node1.connect_to_peer(2, 8002)
    node1.connect_to_peer(3, 8003)
    node2.connect_to_peer(1, 8001)
    node2.connect_to_peer(3, 8003)
    node3.connect_to_peer(1, 8001)
    node3.connect_to_peer(2, 8002)
    
    # Give connections time to establish
    time.sleep(1)
    
    print("\n" + "="*50)
    print("DISTRIBUTED MUTUAL EXCLUSION SIMULATION")
    print("="*50)
    
    # Simulate concurrent CS requests
    def request_after_delay(node, delay):
        time.sleep(delay)
        node.request_cs()
    
    # Start requests with small delays to create conflicts
    threading.Thread(target=request_after_delay, args=(node1, 0.1)).start()
    threading.Thread(target=request_after_delay, args=(node2, 0.2)).start()
    threading.Thread(target=request_after_delay, args=(node3, 0.3)).start()
    
    # Let simulation run
    time.sleep(15)
    
    # Another round of requests
    print("\n" + "="*30)
    print("SECOND ROUND OF REQUESTS")
    print("="*30)
    
    threading.Thread(target=request_after_delay, args=(node3, 0.1)).start()
    threading.Thread(target=request_after_delay, args=(node1, 0.2)).start()
    
    # Let simulation run
    time.sleep(10)
    
    # Cleanup
    for node in nodes:
        node.shutdown()

if __name__ == "__main__":
    main()
