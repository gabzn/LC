https://leetcode.com/problems/ternary-expression-parser/

class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = []
        
        # Traverse the expression from right to left
        for char in reversed(expression):
            if char == ':':
                continue
                
            if stack and stack[-1] == '?':
                stack.pop()  # pop off the ?
                
                true_value, false_value = stack.pop(), stack.pop()
                stack.append(true_value if char == 'T' else false_value)        
            else:
                stack.append(char)
        
        return stack[0]
-------------------------------------------------------------------
class Solution:
    def parseTernary(self, expression: str) -> str:
        queue = deque()
        stack = [char for char in expression]
        
        while len(stack) != 1:
            char = stack.pop()
            if char == ':':
                continue
            
            if char == '?':
                is_true = True if stack.pop() == 'T' else False
                
                true_value, false_value = queue.popleft(), queue.popleft()
                stack.append(true_value if is_true else false_value)
                
                while queue:
                    stack.append(queue.popleft())
                continue
                
            queue.appendleft(char)
            
        return ''.join(stack)
