https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/
  
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, res = 0, math.inf
        
        for r in range(len(nums)):
            if r - l + 1 == k:
                res = min(res, nums[r] - nums[l])
                l += 1
            
        return res
