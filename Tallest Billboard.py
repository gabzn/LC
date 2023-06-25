https://leetcode.com/problems/tallest-billboard/
https://leetcode.com/problems/tallest-billboard/discuss/3676384/Brute-to-Memoization-Total-Explanation

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        
        # We want the difference to be 0
        def dp(i, difference, memo):
            if i == len(rods):
                return 0 if difference == 0 else -math.inf
            if (i, difference) in memo:
                return memo[(i, difference)]
            
            memo[(i, difference)] = max(dp(i + 1, difference, memo),
                                        dp(i + 1, difference + rods[i], memo) + rods[i],
                                        dp(i + 1, difference - rods[i], memo))
            return memo[(i, difference)]        
        return dp(0, 0, {})
