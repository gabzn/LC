https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix_matrix = self.get_prefix_matrix(matrix)
        
    def sumRegion(self, r_start: int, c_start: int, r_end: int, c_end: int) -> int:
        r_start += 1
        c_start += 1
        r_end += 1
        c_end += 1
        
        return self.prefix_matrix[r_end][c_end] - self.prefix_matrix[r_end][c_start - 1] - self.prefix_matrix[r_start - 1][c_end] + self.prefix_matrix[r_start - 1][c_start - 1]
        
    def get_prefix_matrix(self, matrix):
        ROWS, COLS = len(matrix), len(matrix[0])
        
        prefix_matrix = [[0 for _ in range(COLS + 1)] for _ in range(ROWS + 1)]
        for r in range(ROWS):
            for c in range(COLS):
                prefix_matrix[r + 1][c + 1] = matrix[r][c] + prefix_matrix[r + 1][c] + prefix_matrix[r][c + 1] - prefix_matrix[r][c]
        
        return prefix_matrix
