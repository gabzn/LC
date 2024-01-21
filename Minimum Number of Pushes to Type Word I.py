https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/

class Solution:
    def minimumPushes(self, word: str) -> int:
        LEN = len(word)
        
        res, multiplier = 0, 1
        d, m = divmod(LEN, 8)

        while d:
            res += (multiplier * 8)
            multiplier += 1
            d -= 1
        
        res += (multiplier * m)        
        return res
