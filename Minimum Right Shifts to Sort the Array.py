https://leetcode.com/problems/minimum-right-shifts-to-sort-the-array/

class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        LEN = len(nums)
        min_num, min_index = nums[0], 0
        
        # Find the min number and its index
        for idx, num in enumerate(nums):
            if num < min_num:
                min_num = num
                min_index = idx
        
        # Loop through the array starting at min_num
        # and make sure every element after the min_num is increasing
        j = (min_index + 1) % LEN
        
        while j != min_index:
            if j == 0:
                if nums[-1] > nums[j]:
                    return -1
            else:
                if nums[j-1] > nums[j]:
                    return -1
            
            j = (j + 1) % LEN
        
        if min_index == 0:
            return 0
        return LEN - min_index
