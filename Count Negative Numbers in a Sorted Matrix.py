https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
  
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        
        for row in grid:
            l, r = 0, len(row) - 1
            
            while l <= r:
                m = (l + r) // 2
                
                if row[m] >= 0:
                    l = m + 1
                else:
                    res += r - m + 1
                    r = m - 1
        
        return res
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        res = 0
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] < 0:
                    res += 1

        return res
