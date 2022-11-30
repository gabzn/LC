https://leetcode.com/problems/design-browser-history/

class Node:
    def __init__(self, url=None, prev=None, next=None):
        self.url = url
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node()
        self.tail = Node()
        self.cur = Node(homepage)
        self.insert(self.head, self.cur, self.tail)

    def insert(self, prev, cur, tail):
        prev.next = cur
        cur.prev = prev
        
        tail.prev = cur
        cur.next = tail
            
    def visit(self, url: str) -> None:
        new_node = Node(url)
        self.insert(self.cur, new_node, self.tail)
        self.cur = new_node
        
    def back(self, steps: int) -> str:
        while self.cur.prev != self.head and steps:
            self.cur = self.cur.prev
            steps -= 1
            
        return self.cur.url

    def forward(self, steps: int) -> str:
        while self.cur.next != self.tail and steps:
            self.cur = self.cur.next
            steps -= 1
        
        return self.cur.url
----------------------------------------------------------------------------------------------------------------------------------------------------------------
class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.back_stack = []
        self.forward_stack = []

    def visit(self, url: str) -> None:
        # Store previous page to some data structure for back
        self.back_stack.append(self.homepage)
        
        # Update current homepage to url
        self.homepage = url

        # Clear all forward history
        self.forward_stack.clear()

    def back(self, steps: int) -> str:
        # Store current page to some data structure for forwarding
        self.forward_stack.append(self.homepage)
        
        while self.back_stack and steps:
            self.forward_stack.append(self.back_stack.pop())
            steps -= 1
            
        self.homepage = self.forward_stack.pop()
        return self.homepage
             
    def forward(self, steps: int) -> str:
        # Store current page to some data structure for back
        self.back_stack.append(self.homepage)
        
        while self.forward_stack and steps:
            self.back_stack.append(self.forward_stack.pop())
            steps -= 1

        self.homepage = self.back_stack.pop()
        return self.homepage
