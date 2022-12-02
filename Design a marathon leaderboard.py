from collections import defaultdict

class Node:
    def __init__(self, id, prev=None, next=None) -> None:
        self.id = id
        self.prev = prev
        self.next = next

class DoublyList:
    def __init__(self) -> None:
        self.head = Node(-1)
        self.tail = Node(-1)

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def append(self, node):
        tail_prev = self.tail.prev

        tail_prev.next = node
        node.prev = tail_prev

        self.tail.prev = node
        node.next = self.tail

    def remove(self, node):
        node_prev = node.prev
        node_next = node.next

        node_prev.next = node_next
        node_next.prev = node_prev

class Leaderboard:
    def __init__(self, sensors, players) -> None:
        self.player_nodes = [Node(i) for i in range(players)]        
        self.sensors = sensors
        self.sensor_dict = defaultdict(DoublyList)
        self.latest_sensor = 0

    def consume(self, sensor_id, player_id):
        if sensor_id == 0:
            self.sensor_dict[sensor_id].append(self.player_nodes[player_id])
            return

        if sensor_id > self.latest_sensor + 1:
            print('Invalid sensor id.')
            return
        
        # Get this player first
        player_node = self.player_nodes[player_id]
    
        # Remove this player from its previous list
        prev_sensor_list = self.sensor_dict[sensor_id-1]
        prev_sensor_list.remove(player_node)

        # Append this player to the new list
        new_sensor_list = self.sensor_dict[sensor_id]
        new_sensor_list.append(player_node)

        # Update latest sensor if possible
        if self.latest_sensor < sensor_id:
            self.latest_sensor = sensor_id

    def display(self):
        res = []

        for key in range(self.latest_sensor, -1, -1):
            doubly_list = self.sensor_dict[key]

            player_node = doubly_list.head.next
            while player_node != doubly_list.tail:
                res.append(player_node.id)
                player_node = player_node.next
            
        return res

marathon = Leaderboard(10, 9)
marathon.consume(0, 2)
marathon.consume(0, 3)
print(marathon.display())
marathon.consume(0, 4)
print(marathon.display())
marathon.consume(1, 4)
marathon.consume(1, 3)
print(marathon.display())
