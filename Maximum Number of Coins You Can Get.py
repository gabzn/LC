https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        LEN = len(piles)
        piles.sort()
        res = 0
        
        l, r = 0, LEN - 1
        while r - l >= 2:
            res += piles[r - 1]
            r -= 2
            l += 1
        
        return res
