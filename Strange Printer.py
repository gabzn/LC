https://leetcode.com/problems/strange-printer/

class Solution:
    def strangePrinter(self, s: str) -> int:
        LEN = len(s)
        
        def dp(left, right, memo):
            if left > right:
                return 0
            if (left, right) in memo:
                return memo[(left, right)]
            
            # We can always print each char 1 turn at a time
            res = 1 + dp(left+1, right, memo)
            
            current_char = s[left]
            for index in range(left+1, right+1):
                next_char = s[index]
                if current_char == next_char:
                    res = min(res, dp(left, index-1, memo) + dp(index+1, right, memo))
            
            memo[(left, right)] = res
            return res
            
        return dp(0, LEN-1, {})
