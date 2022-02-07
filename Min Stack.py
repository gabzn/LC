Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

  MinStack() initializes the stack object.
  void push(int val) pushes the element val onto the stack.
  void pop() removes the element on the top of the stack.
  int top() gets the top element of the stack.
  int getMin() retrieves the minimum element in the stack.
  
  
 class MinStack(object):
    
    def __init__(self):
        """
        define two lists.
        one for inputs
        the other one for the current min
        """
        self.input_stack = []
        self.min_stack = []

    def push(self, val):
        self.input_stack.append(val)
        
        """
        If the stack is not empty, compute the new min and put it on the min_stack
        The new min can be either the input or the topmost in min_stack.
        """
        if self.min_stack:
            current_min = min(val, self.min_stack[-1])
            self.min_stack.append(current_min)
            return
        
        self.min_stack.append(val)
        
    def pop(self):
        self.input_stack.pop(-1)
        self.min_stack.pop(-1)
        
    def top(self):
        return self.input_stack[-1]
        

    def getMin(self):
        return self.min_stack[-1]
