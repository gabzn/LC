https://leetcode.com/problems/predict-the-winner/
https://www.youtube.com/watch?v=g5wLHFTodm0

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        LEN = len(nums)
        
        def dp(l, r, memo):
            if l == r:
                return nums[l]
            if (l, r) in memo:
                return memo[(l, r)]
            
            # Basically we want both players to get their best scores
            # For example, we let player 1 pick left. Next, we want player 2 to pick a number.
            # Both players always pick the best num. In the end we look at the score difference to determine who wins
            picking_left = nums[l] - dp(l+1, r, memo)
            picking_right = nums[r] - dp(l, r-1, memo)
            
            memo[(l, r)] = max(picking_left, picking_right)
            return memo[(l, r)]
        
        return dp(0, LEN-1, {}) >= 0
