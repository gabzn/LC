https://leetcode.com/problems/tallest-billboard/

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        # dp(i) returns the tallest billboard we can install at index i when the height difference is difference
        def dp(i, difference, memo):
            if i == len(rods):
                return 0 if difference == 0 else -math.inf
            if (i, difference) in memo:
                return memo[(i, difference)]
            
            memo[(i, difference)] = max(dp(i + 1, difference, memo), \
                                        dp(i + 1, difference + rods[i], memo) + rods[i], \
                                        dp(i + 1, difference - rods[i], memo))
            return memo[(i, difference)]        
        return dp(0, 0, {})
