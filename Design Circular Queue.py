https://leetcode.com/problems/design-circular-queue/
  
class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.max_size = k
        self.cur_size = 0
        self.front = 0
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = value
        self.cur_size += 1
        
        return True
        
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.front = (self.front + 1) % self.max_size
        self.cur_size -= 1
        
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.queue[self.front]
        
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.queue[self.rear]
        
    def isEmpty(self) -> bool:
        return self.cur_size == 0
    
    def isFull(self) -> bool:
        return self.cur_size == self.max_size    
