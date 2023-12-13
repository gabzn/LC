https://leetcode.com/problems/special-positions-in-a-binary-matrix/

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ROWS, COLS = len(mat), len(mat[0])

        def is_special(r, c):
            for x in range(ROWS):
                if x != r and mat[x][c] == 1:
                    return False
            
            for y in range(COLS):
                if y != c and mat[r][y] == 1:
                    return False
            
            return True
        
        res = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 1 and is_special(r, c):
                    res += 1
        
        return res
