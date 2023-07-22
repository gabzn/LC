https://leetcode.com/problems/knight-probability-in-chessboard/

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        offsets = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, 1), (2, -1)]
        
        def is_on_board(x, y):
            return 0 <= x < n and 0 <= y < n
        
        def dp(x, y, k, memo):
            if k == 0:
                return 1 if is_on_board(x, y) else 0
            if (x, y, k) in memo:
                return memo[(x, y, k)]
            
            memo[(x, y, k)] = 0
            
            for offset_x, offset_y in offsets:
                new_x, new_y = x + offset_x, y + offset_y
                
                # Compute the total number of walkable paths and store it inside memo
                if is_on_board(new_x, new_y):
                    memo[(x, y, k)] += dp(new_x, new_y, k - 1, memo)
                    
            # Now we have all the walkable paths. We divide it out of all 8 paths
            memo[(x, y, k)] /= 8
            return memo[(x, y, k)]

        return dp(row, column, k, {})
