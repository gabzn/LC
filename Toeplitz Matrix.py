https://leetcode.com/problems/toeplitz-matrix/

Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        def check_diagonal(r, c):
            # Base case when either r or c is out of bound.
            if (r+1) == R or (c+1) == C:
                return True
            
            # Check the current number with the next number in its diagonal.
            if matrix[r][c] != matrix[r+1][c+1]:
                return False
            
            return check_diagonal(r+1, c+1)
        
        R, C = len(matrix), len(matrix[0])
        # Check the first number of each row.
        for r in range(R):
            if check_diagonal(r, 0) == False:
                return False
        
        # Check the first number of each column.
        for c in range(1, C):
            if check_diagonal(0, c) == False:
                return False
            
        return True
