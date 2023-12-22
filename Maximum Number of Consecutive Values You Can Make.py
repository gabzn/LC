https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/
https://www.youtube.com/watch?v=3ONSGo28_Z0

https://leetcode.com/problems/patching-array/
https://leetcode.com/problems/minimum-number-of-coins-to-be-added/

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        LEN = len(coins)
        
        coins.sort()
        res = 1
        
        for coin in coins:
            if res >= coin:
                res += coin
                            
        return res
