https://leetcode.com/problems/baseball-game/

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        scores = 0
        
        for operation in operations:
            if operation == 'C':
                scores -= stack.pop()
            elif operation == 'D':
                score = stack[-1] * 2
                
                scores += score
                stack.append(score)
            elif operation == '+':
                score = stack[-1] + stack[-2]
                
                scores += score
                stack.append(score)
            else:
                score = int(operation)
                
                scores += score
                stack.append(score)
        
        return scores
