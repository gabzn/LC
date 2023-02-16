https://leetcode.com/problems/max-consecutive-ones/
  
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, ones = 0, 0
        
        for num in nums:
            if num == 1:
                ones += 1
            else:
                ones = 0
            
            res = max(res, ones)
            
        return res
