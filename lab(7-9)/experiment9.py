# Define a class to represent a node in a distributed system
class Node:
    def __init__(self, id):
        self.id = id    # Unique identifier for the node
        self.request_queue = []
# example)    # Queue to track requests (not used in this simple example)

# Simulate a request to enter the critical section
    def request_cs(self, timestamp):
        print(f"Node {self.id} requests CS at time {timestamp}")
        return f"REQ from {self.id} at {timestamp}"  # Return a request message as a string

# Simulate receiving a reply from another node
    def receive_reply(self, from_id):
        print(f"Node {self.id} received REPLY from {from_id}")
        #--- Simulation Starts Here ---

# Create two nodes
node1 = Node(1)
node2 = Node(2)

# Both nodes request to enter the critical section with different timestamps
req1 = node1.request_cs(5)
req2 = node2.request_cs(4)

# Decide which node gets access based on the request message (lexicographic comparison)
# NOTE: This is a simplified comparison; in real systems, timestamps would be compared directly
if req1 > req2:
    node2.receive_reply(1)  # Node 2 gets the CS, Node 1 sends REPLY
else:
    node1.receive_reply(2)  # Node 1 gets the CS, Node 2 sends REPLY
