https://leetcode.com/problems/minimum-adjacent-swaps-to-make-a-valid-array/

class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        N = len(nums)
        max_num = -1
        min_num = 10 ** 6
        
        leftmost_min = -1
        rightmost_max = -1
        for idx, num in enumerate(nums):
            # Find the min and its index
            if (num == min_num and leftmost_min == -1) or (num < min_num):
                leftmost_min = idx
                min_num = num
            
            # Find the max and its index
            if (num == max_num and idx > rightmost_max) or (num > max_num):
                rightmost_max = idx
                max_num = num
        
        if leftmost_min > rightmost_max:
            return (leftmost_min - 1) + (N - rightmost_max - 1)
        else:
            return leftmost_min + (N - rightmost_max - 1)
