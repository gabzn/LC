https://leetcode.com/problems/apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/

class Solution:
    def minOperations(self, k: int) -> int:
        res = inf

        for val in range(1, k):
            additions = val - 1
            multiplications = int(ceil(k / val)) - 1
            res = min(res, additions + multiplications)
                
        return res if res != inf else 0
