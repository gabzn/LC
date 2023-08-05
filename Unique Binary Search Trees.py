https://leetcode.com/problems/unique-binary-search-trees/

class Solution:
    def numTrees(self, n: int) -> int:

        def dp(start, end, memo):
            if start < 1 or end > n or start >= end:
                return 1
            if (start, end) in memo:
                return memo[(start, end)]
            
            res = 0
            for index in range(start, end + 1):
                res += dp(start, index - 1, memo) * dp(index + 1, end, memo)
                
            memo[(start, end)] = res
            return res
        
        return dp(1, n, {})
