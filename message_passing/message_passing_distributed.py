import socket
import threading
import json
import time
import queue
import uuid
from enum import Enum
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional, Any, Callable
import pickle

class MessageType(Enum):
    REQUEST = "request"
    RESPONSE = "response"
    HEARTBEAT = "heartbeat"
    ELECTION = "election"
    COORDINATE = "coordinate"
    ACKNOWLEDGE = "acknowledge"
    BROADCAST = "broadcast"

@dataclass
class Message:
    """Base message structure for distributed communication"""
    id: str
    type: MessageType
    sender: str
    recipient: str
    timestamp: float
    data: Any = None
    sequence_number: int = 0
    requires_ack: bool = False
    
    def to_bytes(self) -> bytes:
        """Serialize message to bytes"""
        return pickle.dumps(asdict(self))
    
    @classmethod
    def from_bytes(cls, data: bytes) -> 'Message':
        """Deserialize message from bytes"""
        msg_dict = pickle.loads(data)
        msg_dict['type'] = MessageType(msg_dict['type'])
        return cls(**msg_dict)

class MessageHandler:
    """Handles different types of messages"""
    
    def __init__(self):
        self.handlers: Dict[MessageType, Callable] = {}
    
    def register_handler(self, msg_type: MessageType, handler: Callable):
        """Register a handler for a specific message type"""
        self.handlers[msg_type] = handler
    
    def handle_message(self, message: Message, node: 'DistributedNode'):
        """Route message to appropriate handler"""
        handler = self.handlers.get(message.type)
        if handler:
            return handler(message, node)
        else:
            print(f"No handler for message type: {message.type}")

class DistributedNode:
    """Represents a node in a distributed system"""
    
    def __init__(self, node_id: str, host: str = "localhost", port: int = 0):
        self.node_id = node_id
        self.host = host
        self.port = port
        self.socket = None
        self.running = False
        
        # Message handling
        self.message_handler = MessageHandler()
        self.message_queue = queue.Queue()
        self.pending_acks = {}
        self.sequence_counter = 0
        
        # Network topology
        self.peers: Dict[str, tuple] = {}  # node_id -> (host, port)
        self.connected_peers: Dict[str, socket.socket] = {}
        
        # Consensus and coordination
        self.leader = None
        self.term = 0
        self.voted_for = None
        
        # Setup default handlers
        self._setup_default_handlers()
    
    def _setup_default_handlers(self):
        """Setup default message handlers"""
        self.message_handler.register_handler(MessageType.HEARTBEAT, self._handle_heartbeat)
        self.message_handler.register_handler(MessageType.ACKNOWLEDGE, self._handle_acknowledge)
        self.message_handler.register_handler(MessageType.REQUEST, self._handle_request)
        self.message_handler.register_handler(MessageType.ELECTION, self._handle_election)
        self.message_handler.register_handler(MessageType.COORDINATE, self._handle_coordinate)
        self.message_handler.register_handler(MessageType.BROADCAST, self._handle_broadcast)
    
    def start(self):
        """Start the node"""
        self.running = True
        
        # Create and bind socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.host, self.port))
        
        # Get actual port if auto-assigned
        if self.port == 0:
            self.port = self.socket.getsockname()[1]
        
        self.socket.listen(5)
        print(f"Node {self.node_id} started on {self.host}:{self.port}")
        
        # Start listener thread
        self.listener_thread = threading.Thread(target=self._listen_for_connections)
        self.listener_thread.start()
        
        # Start message processor
        self.processor_thread = threading.Thread(target=self._process_messages)
        self.processor_thread.start()
        
        # Start heartbeat
        self.heartbeat_thread = threading.Thread(target=self._heartbeat_loop)
        self.heartbeat_thread.start()
    
    def stop(self):
        """Stop the node"""
        self.running = False
        
        # Close connections
        for peer_socket in self.connected_peers.values():
            peer_socket.close()
        
        if self.socket:
            self.socket.close()
        
        print(f"Node {self.node_id} stopped")
    
    def add_peer(self, peer_id: str, host: str, port: int):
        """Add a peer to the network topology"""
        self.peers[peer_id] = (host, port)
        print(f"Node {self.node_id} added peer {peer_id} at {host}:{port}")
    
    def connect_to_peer(self, peer_id: str):
        """Establish connection to a peer"""
        if peer_id in self.connected_peers:
            return True
        
        if peer_id not in self.peers:
            print(f"Peer {peer_id} not in topology")
            return False
        
        host, port = self.peers[peer_id]
        try:
            peer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            peer_socket.connect((host, port))
            self.connected_peers[peer_id] = peer_socket
            print(f"Node {self.node_id} connected to peer {peer_id}")
            return True
        except Exception as e:
            print(f"Failed to connect to peer {peer_id}: {e}")
            return False
    
    def send_message(self, message: Message, reliable: bool = True):
        """Send a message to a peer"""
        if message.recipient not in self.peers:
            print(f"Unknown recipient: {message.recipient}")
            return False
        
        # Connect if not already connected
        if not self.connect_to_peer(message.recipient):
            return False
        
        try:
            # Add sequence number
            message.sequence_number = self.sequence_counter
            self.sequence_counter += 1
            
            # Send message
            peer_socket = self.connected_peers[message.recipient]
            data = message.to_bytes()
            
            # Send length first, then data
            length = len(data)
            peer_socket.send(length.to_bytes(4, byteorder='big'))
            peer_socket.send(data)
            
            # Handle acknowledgment if required
            if message.requires_ack and reliable:
                self.pending_acks[message.id] = message
            
            print(f"Node {self.node_id} sent {message.type.value} to {message.recipient}")
            return True
            
        except Exception as e:
            print(f"Failed to send message: {e}")
            # Remove broken connection
            if message.recipient in self.connected_peers:
                del self.connected_peers[message.recipient]
            return False
    
    def broadcast_message(self, message: Message):
        """Broadcast a message to all peers"""
        message.type = MessageType.BROADCAST
        for peer_id in self.peers:
            if peer_id != self.node_id:
                msg_copy = Message(
                    id=str(uuid.uuid4()),
                    type=message.type,
                    sender=self.node_id,
                    recipient=peer_id,
                    timestamp=time.time(),
                    data=message.data
                )
                self.send_message(msg_copy)
    
    def _listen_for_connections(self):
        """Listen for incoming connections"""
        while self.running:
            try:
                client_socket, address = self.socket.accept()
                # Handle each connection in a separate thread
                threading.Thread(
                    target=self._handle_client_connection,
                    args=(client_socket, address)
                ).start()
            except Exception as e:
                if self.running:
                    print(f"Error accepting connection: {e}")
    
    def _handle_client_connection(self, client_socket, address):
        """Handle messages from a connected client"""
        try:
            while self.running:
                # Read message length
                length_bytes = client_socket.recv(4)
                if not length_bytes:
                    break
                
                length = int.from_bytes(length_bytes, byteorder='big')
                
                # Read message data
                data = b''
                while len(data) < length:
                    chunk = client_socket.recv(length - len(data))
                    if not chunk:
                        break
                    data += chunk
                
                # Deserialize and queue message
                message = Message.from_bytes(data)
                self.message_queue.put(message)
                
        except Exception as e:
            print(f"Error handling client connection: {e}")
        finally:
            client_socket.close()
    
    def _process_messages(self):
        """Process incoming messages"""
        while self.running:
            try:
                message = self.message_queue.get(timeout=1)
                self.message_handler.handle_message(message, self)
                self.message_queue.task_done()
            except queue.Empty:
                continue
    
    def _heartbeat_loop(self):
        """Send periodic heartbeats"""
        while self.running:
            for peer_id in self.peers:
                if peer_id != self.node_id:
                    heartbeat = Message(
                        id=str(uuid.uuid4()),
                        type=MessageType.HEARTBEAT,
                        sender=self.node_id,
                        recipient=peer_id,
                        timestamp=time.time(),
                        data={"term": self.term, "leader": self.leader}
                    )
                    self.send_message(heartbeat, reliable=False)
            
            time.sleep(5)  # Heartbeat interval
    
    # Message Handlers
    def _handle_heartbeat(self, message: Message, node: 'DistributedNode'):
        """Handle heartbeat messages"""
        print(f"Node {self.node_id} received heartbeat from {message.sender}")
        
        # Update leader information if newer
        if message.data and message.data.get("term", 0) > self.term:
            self.term = message.data["term"]
            self.leader = message.data.get("leader")
    
    def _handle_acknowledge(self, message: Message, node: 'DistributedNode'):
        """Handle acknowledgment messages"""
        if message.data and message.data.get("ack_id") in self.pending_acks:
            del self.pending_acks[message.data["ack_id"]]
            print(f"Node {self.node_id} received ACK for message {message.data['ack_id']}")
    
    def _handle_request(self, message: Message, node: 'DistributedNode'):
        """Handle request messages"""
        print(f"Node {self.node_id} processing request from {message.sender}")
        
        # Process the request (simulate work)
        result = f"Processed: {message.data}"
        
        # Send response
        response = Message(
            id=str(uuid.uuid4()),
            type=MessageType.RESPONSE,
            sender=self.node_id,
            recipient=message.sender,
            timestamp=time.time(),
            data={"result": result, "request_id": message.id}
        )
        self.send_message(response)
    
    def _handle_election(self, message: Message, node: 'DistributedNode'):
        """Handle election messages (simplified leader election)"""
        print(f"Node {self.node_id} received election message from {message.sender}")
        
        candidate_id = message.data.get("candidate_id")
        candidate_term = message.data.get("term", 0)
        
        # Simple election: vote for candidate if term is higher
        if candidate_term > self.term and not self.voted_for:
            self.term = candidate_term
            self.voted_for = candidate_id
            
            # Send vote
            vote = Message(
                id=str(uuid.uuid4()),
                type=MessageType.RESPONSE,
                sender=self.node_id,
                recipient=message.sender,
                timestamp=time.time(),
                data={"vote": True, "term": self.term}
            )
            self.send_message(vote)
    
    def _handle_coordinate(self, message: Message, node: 'DistributedNode'):
        """Handle coordination messages"""
        print(f"Node {self.node_id} received coordination from {message.sender}")
        action = message.data.get("action")
        
        if action == "leader_announcement":
            self.leader = message.sender
            self.term = message.data.get("term", self.term)
            print(f"Node {self.node_id} acknowledges {message.sender} as leader")
    
    def _handle_broadcast(self, message: Message, node: 'DistributedNode'):
        """Handle broadcast messages"""
        print(f"Node {self.node_id} received broadcast: {message.data}")
    
    # High-level operations
    def request_work(self, peer_id: str, work_data: Any):
        """Request work from a peer"""
        request = Message(
            id=str(uuid.uuid4()),
            type=MessageType.REQUEST,
            sender=self.node_id,
            recipient=peer_id,
            timestamp=time.time(),
            data=work_data,
            requires_ack=True
        )
        return self.send_message(request)
    
    def announce_leadership(self):
        """Announce this node as leader"""
        self.leader = self.node_id
        self.term += 1
        
        announcement = Message(
            id=str(uuid.uuid4()),
            type=MessageType.COORDINATE,
            sender=self.node_id,
            recipient="all",
            timestamp=time.time(),
            data={"action": "leader_announcement", "term": self.term}
        )
        self.broadcast_message(announcement)

# Example usage and demonstration
def create_distributed_system():
    """Create a simple distributed system with multiple nodes"""
    nodes = []
    
    # Create nodes
    for i in range(3):
        node = DistributedNode(f"node-{i}", port=8000 + i)
        nodes.append(node)
    
    # Start all nodes
    for node in nodes:
        node.start()
        time.sleep(0.5)  # Small delay to ensure binding
    
    # Connect nodes to each other
    for i, node in enumerate(nodes):
        for j, other_node in enumerate(nodes):
            if i != j:
                node.add_peer(other_node.node_id, other_node.host, other_node.port)
    
    return nodes

def demonstrate_message_passing():
    """Demonstrate various message passing scenarios"""
    print("=== Creating Distributed System ===")
    nodes = create_distributed_system()
    
    try:
        # Wait for nodes to establish connections
        print("\n=== Waiting for connections to establish ===")
        time.sleep(3)
        
        # Demonstrate request-response
        print("\n=== Request-Response Pattern ===")
        nodes[0].request_work("node-1", {"task": "calculate_sum", "numbers": [1, 2, 3, 4, 5]})
        
        # Demonstrate broadcast
        print("\n=== Broadcast Pattern ===")
        broadcast_msg = Message(
            id=str(uuid.uuid4()),
            type=MessageType.BROADCAST,
            sender=nodes[0].node_id,
            recipient="all",
            timestamp=time.time(),
            data={"announcement": "System maintenance in 5 minutes"}
        )
        nodes[0].broadcast_message(broadcast_msg)
        
        # Demonstrate leader election
        print("\n=== Leader Election ===")
        nodes[2].announce_leadership()
        
        # Let the system run for a while
        print("\n=== System running... ===")
        time.sleep(10)
        
    finally:
        # Clean shutdown
        print("\n=== Shutting down system ===")
        for node in nodes:
            node.stop()

if __name__ == "__main__":
    demonstrate_message_passing()
