https://leetcode.com/problems/minimum-operations-to-write-the-letter-y-on-a-grid/

class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        def is_in_y(x, y):
            # Left diagonal
            if x == y and x <= HALF:
                return True
            
            # Right diagonal
            if x + y == N - 1 and x <= HALF:
                return True            
            
            # Middle
            if HALF <= x < N and y == HALF:
                return True
                        
            return False
        
        def change(y_val, others):
            ops = 0
                        
            for i in range(N):
                for j in range(N):
                    if is_in_y(i, j) and grid[i][j] != y_val:
                        ops += 1
                        continue
                    
                    if not is_in_y(i, j) and grid[i][j] != others:
                        ops += 1
                    
            return ops
        
        N = len(grid)
        HALF = N // 2
        res = inf

        for y_val in range(3):
            for others in range(3):
                if y_val == others:
                    continue
                res = min(res, change(y_val, others))
        
        return res
