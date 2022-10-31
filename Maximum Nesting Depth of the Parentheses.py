https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
  
class Solution:
    def maxDepth(self, s: str) -> int:
        """
        If we see a left bracket, we know this is a depth of 1
        If we see a right bracket, we know this depth has ended.
        
        Basically we are just counting the number of left brackets and right brackets
        """
        depth, max_depth = 0, 0
        
        for char in s:
            if char == '(':
                depth += 1
            if char == ')':
                depth -= 1
                
            max_depth = max(max_depth, depth)
            
        return max_depth
