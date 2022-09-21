https://leetcode.com/problems/search-a-2d-matrix/
  
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
  Integers in each row are sorted from left to right. 
  The first integer of each row is greater than the last integer of the previous row.
  
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

# Solution #1
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
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Solution #2
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top_row, bottom_row = 0, len(matrix) - 1
        
        # First perform BS on the rows to find the row of which target is in range.
        while top_row <= bottom_row:
            mid = (top_row + bottom_row) // 2    
            mid_row = matrix[mid]            
            if mid_row[0] <= target <= mid_row[-1]:
                break
                
            if mid_row[0] < target:
                top_row = mid + 1
            else:
                bottom_row = mid - 1
                
        if top_row > bottom_row:
            return False
        
        # Then perform another BS on the target row to find the target.
        # O(2logn)
        target_row = matrix[(top_row + bottom_row) // 2]
        left, right = 0, len(target_row) - 1
        while left <= right:
            mid = (left + right) // 2
            if target_row[mid] == target:
                return True
              
            if target_row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
