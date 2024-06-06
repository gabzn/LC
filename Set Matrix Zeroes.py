https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        M = len(matrix)
        N = len(matrix[0])

        for x in range(M):
            for y in range(N):
                if matrix[x][y] == 0:
                    for next_x in range(M):
                        if matrix[next_x][y] != inf and matrix[next_x][y] != 0:
                            matrix[next_x][y] = inf

                    for next_y in range(N):
                        if matrix[x][next_y] != inf and matrix[x][next_y] != 0:
                            matrix[x][next_y] = inf

        for x in range(M):
            for y in range(N):
                if matrix[x][y] == inf:
                    matrix[x][y] = 0
