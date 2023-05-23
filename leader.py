import time
from threading import Thread

class Node(Thread):
    def __init__(self, node_id, num_nodes):
        super(Node, self).__init__()
        self.node_id = node_id
        self.num_nodes = num_nodes
        self.leader_id = None
        self.election_in_progress = False

    def send_message(self, receiver_id, message):
        time.sleep(0.5)  # Simulate network delay
        receiver = nodes[receiver_id]
        receiver.receive_message(self.node_id, message)

    def receive_message(self, sender_id, message):
        if message == 'ELECTION':
            self.handle_election(sender_id)
        elif message == 'LEADER':
            self.handle_leader(sender_id)

    def handle_election(self, sender_id):
        if not self.election_in_progress:
            self.election_in_progress = True
            print(f"Node {self.node_id}: Received ELECTION message from Node {sender_id}. Forwarding the message.")
            for node_id in range(self.node_id + 1, self.num_nodes):
                self.send_message(node_id, 'ELECTION')
            self.send_message(sender_id, 'LEADER')

    def handle_leader(self, leader_id):
        self.leader_id = leader_id
        print(f"Node {self.node_id}: Received LEADER message from Node {leader_id}. My leader is Node {leader_id}.")
        for node_id in range(self.node_id + 1, self.num_nodes):
            self.send_message(node_id, 'LEADER')

    def run(self):
        if self.node_id == 0:
            self.start_election()
    
    def start_election(self):
        self.election_in_progress = True
        print(f"Node {self.node_id}: Starting election.")
        for node_id in range(self.node_id + 1, self.num_nodes):
            self.send_message(node_id, 'ELECTION')

        # Wait for the election to complete
        time.sleep(2)

        if not self.leader_id:
            print(f"Node {self.node_id}: I am the leader.")
            self.leader_id = self.node_id
            for node_id in range(self.node_id + 1, self.num_nodes):
                self.send_message(node_id, 'LEADER')

# Örnek kullanım
num_nodes = 5
nodes = []

# Node'ları oluşturma
for node_id in range(num_nodes):
    node = Node(node_id, num_nodes)
    nodes.append(node)

# Node'ları başlatma
for node in nodes:
    node.start()

# Bekleme
for node in nodes:
    node.join()

# Sonuçları kontrol etme
for node in nodes:
    print(f"Node {node.node_id}: Leader is Node {node.leader_id}.")
