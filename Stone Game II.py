https://leetcode.com/problems/stone-game-ii/

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        LEN = len(piles)
        
        def dp(index, m, is_alice_turn, memo):
            if index == LEN:
                return 0
            if (index, m, is_alice_turn) in memo:
                return memo[(index, m, is_alice_turn)]
            
            res = 0 if is_alice_turn else math.inf
            stones = 0
            
            for x in range(1, 2 * m + 1):
                if index + x > LEN:
                    break
                
                stones += piles[index + x - 1]
                if is_alice_turn:
                    res = max(res, stones + dp(index+x, max(m, x), False, memo))
                else:
                    res = min(res, dp(index+x, max(m, x), True, memo))
            
            memo[(index, m, is_alice_turn)] = res
            return res
            
        return dp(0, 1, True, {})
