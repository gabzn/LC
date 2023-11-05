https://leetcode.com/problems/find-champion-i/

class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        for i in range(n):
            team = grid[i]
            if team.count(1) == n - 1:
                return i
