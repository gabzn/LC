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
