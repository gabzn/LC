https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        LEN = len(stones)
        
        dp = [set() for _ in range(LEN)]
        dp[0].add(1)
        
        for r in range(1, LEN):
            current_unit = stones[r]
            
            for l in range(r):
                prev_unit = stones[l]
                diff = current_unit - prev_unit
                
                if diff in dp[l]:
                    dp[r].add(diff - 1)
                    dp[r].add(diff)
                    dp[r].add(diff + 1)
        
        return True if dp[-1] else False
