https://leetcode.com/problems/maximum-number-of-points-with-cost/

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ROWS = len(points)
        COLS = len(points[0])
        
        dp = [[-1 for _ in range(COLS)] for _ in range(ROWS)]
        for j in range(COLS):
            dp[0][j] = points[0][j]
        
        """
        for i in range(1, ROWS):
            for j in range(COLS):
                max_from_previous_row = 0
            
                for x in range(COLS):
                    max_from_previous_row = max(max_from_previous_row, dp[i - 1][x] + points[i][j] - abs(j - x))
            
            dp[i][j] = max(dp[i][j], max_from_previous_row)
        
        if x <= j, (j - x) >= 0 AKA (j - x) is positive:
            dp[i - 1][x] + points[i][j] - (+(j - x))
            dp[i - 1][x] + points[i][j] - j + x
            dp[i - 1][x] + x + points[i][j] - j
        
        if x > j, (j - x) < 0 AKA (j - x) is negative:
            dp[i - 1][x] + points[i][j] - (-(j - x))
            dp[i - 1][x] + points[i][j] - (-j + x)
            dp[i - 1][x] + points[i][j] + j - x
            dp[i - 1][x] - x + points[i][j] + j
        """
        
        for i in range(1, ROWS):
            max_of_previous_row = -1
            
            for j in range(COLS):
                max_of_previous_row = max(max_of_previous_row, dp[i - 1][j] + j)
                dp[i][j] = max(dp[i][j], max_of_previous_row + points[i][j] - j)
            
            max_of_previous_row = -inf
            for j in range(COLS - 1, -1, -1):
                max_of_previous_row = max(max_of_previous_row, dp[i - 1][j] - j)
                dp[i][j] = max(dp[i][j], max_of_previous_row + points[i][j] + j)

        return max(dp[-1])
