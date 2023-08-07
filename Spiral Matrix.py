https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])
        res = []
        
        while left < right and top < bottom:
            # Going right
            for index in range(left, right):
                res.append(matrix[top][index])
            top += 1
            
            # Going down
            for index in range(top, bottom):
                res.append(matrix[index][right-1])
            right -= 1
            
            if not (left < right and top < bottom):
                break
                
            # Going left
            for index in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][index])
            bottom -= 1
            
            # Going up
            for index in range(bottom-1, top-1, -1):
                res.append(matrix[index][left])
            left += 1
        
        return res
