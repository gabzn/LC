https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/

class Solution:
    def minSwaps(self, s: str) -> int:
        N = len(s)
        res = opening = closing = 0
        left = 0
        right = N - 1
        
        while left < right:
            b = s[left]
            if b == '[':
                opening += 1
            else:
                closing += 1
            
            if closing > opening:
                while left < right and s[right] != '[':
                    right -= 1
                opening += 1
                closing -= 1
                res += 1
                
            left += 1
        
        return res
