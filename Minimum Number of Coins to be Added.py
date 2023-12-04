https://leetcode.com/problems/minimum-number-of-coins-to-be-added/
https://www.youtube.com/watch?v=RAdaP-JcLA0

class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        
        res, max_range = 0, 0
        idx = 0
        while max_range < target:
            if idx < len(coins) and coins[idx] <= max_range + 1:
                max_range += coins[idx]
                idx += 1
            else:
                res += 1
                max_range += (max_range + 1)
        
        return res
