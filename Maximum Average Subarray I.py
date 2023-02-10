https://leetcode.com/problems/maximum-average-subarray-i/
  
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l, running_sum, res = 0, 0, -math.inf
        
        for r in range(len(nums)):
            running_sum += nums[r]
            
            if r - l + 1 > k:
                running_sum -= nums[l]
                l += 1
            
            if r - l + 1 == k:
                average = running_sum / k
                res = max(res, average)
                    
        return res
