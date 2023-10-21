https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10 ** 9 + 7
        
        @cache
        def dp(position, steps_remaining):
            if steps_remaining == 0:
                return 1 if position == 0 else 0
            
            res = 0
            
            # stay
            res += dp(position, steps_remaining - 1)
            
            # move left
            if position - 1 >= 0: 
                res += dp(position - 1, steps_remaining - 1)
            
            # move right
            if position + 1 < arrLen:
                res += dp(position + 1, steps_remaining - 1)
                        
            return res % MOD
        
        return dp(0, steps)
