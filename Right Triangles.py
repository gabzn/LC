https://leetcode.com/problems/right-triangles/

class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        r = Counter()
        c = Counter()
        res = 0
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    r[i] += 1
                    c[j] += 1
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    res += (r[i] - 1) * (c[j] - 1)

        return res
