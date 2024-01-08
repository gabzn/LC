https://leetcode.com/problems/leftmost-column-with-at-least-a-one/

class Solution:
    def leftMostColumnWithOne(self, matrix: 'BinaryMatrix') -> int:
        ROWS, COLS = matrix.dimensions()
        
        res = inf
        
        for row in range(ROWS):
            left, right = -1, COLS
            
            while left + 1 != right:
                mid = (left + right) // 2
                
                if matrix.get(row, mid) == 1:
                    right = mid
                    res = min(res, right)
                else:
                    left = mid
                        
        return res if res != inf else -1
------------------------------------------------------------------------------------------------
class Solution:
    def leftMostColumnWithOne(self, matrix: 'BinaryMatrix') -> int:
        ROWS, COLS = matrix.dimensions()
        
        res = inf
        x, y = 0, COLS - 1
        
        while x < ROWS and y > -1: 
            if matrix.get(x, y) == 1:
                res = min(res, y)
                y -= 1
            else:
                x += 1
                
        return res if res != inf else -1
