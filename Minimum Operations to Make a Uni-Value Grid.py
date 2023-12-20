https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        # flatten the grid
        nums = []
        for r in range(ROWS):
            for c in range(COLS):
                nums.append(grid[r][c])
        
        # sort numbers and find the median
        nums.sort()
        median = nums[len(nums) // 2]
        
        res = 0
        for num in nums:
            diff = abs(median - num)
            if diff % x == 0:
                res += (diff // x)
            else:
                return -1
        
        return res
