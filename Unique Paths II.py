https://leetcode.com/problems/unique-paths-ii/
  
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        
        # dp(x, y) returns the number of ways to get to [x][y]
        def dp(x, y, memo):
            if x == 0 and y == 0:
                return 1
            if x < 0 or y < 0 or obstacleGrid[x][y] == 1:
                return 0
            if (x, y) in memo:
                return memo[(x, y)]
            
            memo[(x, y)] = dp(x - 1, y, memo) + dp(x, y - 1, memo)
            return memo[(x, y)]
            
        return dp(len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1, {})    
