https://leetcode.com/problems/largest-submatrix-with-rearrangements/

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        res = 0
        
        # Find the max height on each baseline row
        max_heights_on_each_col = [0 for _ in range(COLS)]
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c]:
                    max_heights_on_each_col[c] += 1
                else:
                    max_heights_on_each_col[c] = 0
            
            # Sort the baseline by their heights
            max_heights_sorted = sorted(max_heights_on_each_col, reverse=True)
            for length, height in enumerate(max_heights_sorted):
                res = max(res, (length + 1) * height)
                          
        return res
