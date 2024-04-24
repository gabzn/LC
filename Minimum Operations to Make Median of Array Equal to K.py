https://leetcode.com/problems/minimum-operations-to-make-median-of-array-equal-to-k/

class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        N = len(nums)
        
        nums.sort()
        res = 0
        # Set the median to k
        if nums[N // 2] > k or nums[N // 2] < k:
            res += abs(nums[N // 2] - k)
            nums[N // 2] = k
        
        # Look at the left side of the median and make sure everything on the left of median is <= median
        for i in range(N // 2 - 1, -1, -1):
            if nums[i] > nums[i + 1]:
                res += nums[i] - nums[i + 1]
                nums[i] = nums[i + 1]
        
        # Look at the right side of the median and make sure everything on the right of median is >= median
        for i in range(N // 2 + 1, N):
            if nums[i] < nums[i - 1]:
                res += nums[i - 1] - nums[i]
                nums[i] = nums[i - 1]
        
        return res
