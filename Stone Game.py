https://leetcode.com/problems/stone-game/
https://leetcode.com/problems/predict-the-winner/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        def dp(l, r, memo):
            if l == r:
                return piles[l]
            if (l, r) in memo:
                return memo[(l, r)]
            
            alice_picking_left = piles[l] - dp(l+1, r, memo)
            alice_picking_right = piles[r] - dp(l, r-1, memo)
            
            memo[(l, r)] = max(alice_picking_left, alice_picking_right)
            return memo[(l, r)]
        
        return dp(0, len(piles) - 1, {}) > 0
