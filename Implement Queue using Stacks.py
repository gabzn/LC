https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.stack = []
        self.placeholder = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        
        while len(self.stack) > 1:
            val = self.stack.pop()
            self.placeholder.append(val)
        
        res = self.stack.pop()
        
        while self.placeholder:
            self.push(self.placeholder.pop())
        
        return res
            
    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0  
---------------------------------------------------------------------------------------------------------------------------------------------------------------
class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        self.stack.reverse()
        val = self.stack.pop()
        self.stack.reverse()
        return val

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0
