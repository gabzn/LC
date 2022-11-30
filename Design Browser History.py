https://leetcode.com/problems/design-browser-history/
  
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
