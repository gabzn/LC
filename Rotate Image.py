https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        
        for r in range(N):
            for c in range(r, N):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
                
        for row in matrix:
            row.reverse()
