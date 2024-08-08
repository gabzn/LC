https://leetcode.com/problems/spiral-matrix-iii/

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, r: int, c: int) -> List[List[int]]:
        """
        right -> down
        down -> left
        left -> up
        up -> right
        
        right = [0, 1]
        down = [1, 0]
        left = [0, -1]
        up = [-1, 0]
        """
        TOTAL = rows * cols
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        i = 0
        res = []
        visited = set()
        
        while len(res) != TOTAL:
            offset_r, offset_c = DIRECTIONS[i]
            next_r, next_c = DIRECTIONS[(i + 1) % 4]
            
            # if (r + next_r, c + next_c) is in visited, that means we can keep going at the current direction
            while not visited or (r + next_r, c + next_c) in visited:
                visited.add((r, c))
                if 0 <= r < rows and 0 <= c < cols:
                    res.append([r, c])
                r += offset_r
                c += offset_c
            
            i = (i + 1) % 4
    
        return res
