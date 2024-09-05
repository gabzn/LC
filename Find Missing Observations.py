https://leetcode.com/problems/find-missing-observations/

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:        
        """
            (a + b) // (n + m) = d
                        n + m  = c
            (a + b) // c       = d
                       (a + b) = d * c
                            b  = (d * c) // a
        """
        m = len(rolls)
        a = sum(rolls)
        c = (m + n) * mean
        b = c - a
        if b <= 0 or b / n > 6 or b // n == 0:
            return []
        average, remainder = divmod(b, n)
        res = [average] * n
        for i in range(remainder):
            res[i] += 1
        return res
