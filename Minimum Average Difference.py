https://leetcode.com/problems/minimum-average-difference/

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        N = len(nums)
        
        total = sum(nums)
        running_sum = 0
        res = 0        
        min_diff = inf
        
        for i in range(N):
            running_sum += nums[i]
            left = running_sum // (i + 1)
            right = (total - running_sum) // max(N - i - 1, 1)
            
            diff = abs(left - right)
            if diff < min_diff:
                min_diff = diff
                res = i
        
        return res
