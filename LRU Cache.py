https://leetcode.com/problems/lru-cache/
  
from collections import defaultdict

class Node:
    def __init__(self, key=-1, val=-1, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = defaultdict(Node)
        
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def move_to_front(self, node):
        head_next = self.head.next
        self.head.next = node
        
        node.prev = self.head
        node.next = head_next
        head_next.prev = node
        
    def evict(self, node):
        node_next = node.next
        node_prev = node.prev
        
        node_prev.next = node_next
        node_next.prev = node_prev
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # key exists, get the node and val
        # Evict it first then move it to the front since we just accessed it
        res = self.cache[key]
        self.evict(res)
        self.move_to_front(res)
        return res.val     

    def put(self, key: int, value: int) -> None:
        # If the key already exists, update its value and move to front
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            
            # Before moving it to the front, we need to evict it first because we just accessed it
            self.evict(node)
            self.move_to_front(node)
            return
        
        # If the key doesn't exist and capacity is full
        # Evit the last node and delete it from the cache
        if self.capacity <= len(self.cache):
            last_used_node = self.tail.prev
            self.evict(last_used_node)
            del self.cache[last_used_node.key]
        
        # Put the new node into the cache and move it to the front
        node = Node(key, value)
        self.cache[key] = node
        self.move_to_front(node)
