https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        LEN = len(nums)
        res = 0
        
        for i in range(LEN):
            for j in range(i, LEN):
                sub_array = nums[: i] + nums[j+1:]
                
                is_increasing = True
                for k in range(len(sub_array) - 1):
                    if sub_array[k] >= sub_array[k + 1]:
                        is_increasing = False
                        break
                
                if is_increasing:
                    res += 1
        
        return res
