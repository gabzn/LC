https://leetcode.com/problems/number-of-ways-to-earn-points/

class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        LEN = len(types)
        MOD = 10 ** 9 + 7
        
        @cache
        def dp(i, points):
            if i == LEN:
                return 1 if points == target else 0
            
            res = 0
            count, point = types[i]
            
            for num in range(count + 1):
                p = num * point
                if points + p <= target:
                    res += dp(i + 1, points + p)
            
            return res % MOD
        
        return dp(0, 0)
