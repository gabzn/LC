https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        q, r = divmod(time, n - 1)
        if q % 2 == 1:
            return n - r
        else:
            return r + 1
