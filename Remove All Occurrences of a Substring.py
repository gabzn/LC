https://leetcode.com/problems/remove-all-occurrences-of-a-substring/

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        P = len(part)
        stack = []
                
        for char in s:
            stack.append(char)
            
            while (len(stack) >= P) and ("".join(stack[-P::]) == part):
                for _ in range(P):
                    stack.pop()
        
        return ''.join(stack)
