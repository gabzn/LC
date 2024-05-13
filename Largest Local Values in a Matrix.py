https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        N = len(grid)
        res = [[0 for _ in range(N - 2)] for _ in range(N - 2)]
        
        for i in range(N - 2):
            for j in range(N - 2):
                val = 0
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        val = max(val, grid[x][y])
                res[i][j] = val
        
        return res
