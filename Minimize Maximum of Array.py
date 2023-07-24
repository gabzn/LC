https://leetcode.com/problems/minimize-maximum-of-array/

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        running_sum = res = nums[0]
        
        # Distribute the running_sum among the nums we've seen
        for index in range(1, len(nums)):
            running_sum += nums[index]
            res = max(res, math.ceil(running_sum / (index + 1)))

        return res
