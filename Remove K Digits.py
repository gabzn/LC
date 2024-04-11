https://leetcode.com/problems/remove-k-digits/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        N = len(num)
        
        """
        Maintain a monotonic increasing stack
             i-1 i
        1 2 3 4  2
        
        when stack[-1] > n, we always want to pop the topmost element on the stack
        1 2 3 2 is smaller than 1 2 3 4
        """
        stack = []
        for n in num:
            
            while k and stack and int(stack[-1]) > int(n):
                stack.pop()
                k -= 1
            
            stack.append(n)
        
        while k and stack:
            stack.pop()
            k -= 1
        
        res = ''.join(stack).lstrip('0')
        return res if res else '0'
