https://leetcode.com/problems/implement-stack-using-queues/
  
from collections import deque

class MyStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.appendleft(x)

    def pop(self) -> int:
        for ind in range(len(self.queue) - 1):
            val = self.queue.popleft()
            self.push(val)
            
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0
    
# class MyStack:
#     def __init__(self):
#         self.queue = deque()

#     def push(self, x: int) -> None:
#         self.queue.appendleft(x)

#     def pop(self) -> int:
#         return self.queue.popleft()

#     def top(self) -> int:
#         return self.queue[0]

#     def empty(self) -> bool:
#         return len(self.queue) == 0
