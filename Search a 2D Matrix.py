https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        # First, binary search the row the target is in
        target_row = -1
        left, right = 0, ROWS - 1
        while left <= right:
            mid = (left + right) // 2
            
            row_mid = matrix[mid]
            if row_mid[0] <= target <= row_mid[-1]:
                target_row = mid
                break
            
            if row_mid[-1] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        if target_row == -1:
            return False
        
        # Once we found the row that target is in, we binary search on that row
        left, right = 0, COLS - 1
        while left <= right:
            mid = (left + right) // 2
            
            if matrix[target_row][mid] == target:
                return True
            
            if matrix[target_row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False
-----------------------------------------------------------------------------------------------
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # Go through each row and ONLY perform BS on the row of which target is in the range.
        # O(n*logn) runtime
        for row in matrix:
            left, right = 0, len(row) - 1
            
            if row[left] <= target <= row[right]:
                while left <= right:
                    mid = (left + right) // 2
                    if row[mid] == target:
                        return True
                      
                    if row[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
        return False
