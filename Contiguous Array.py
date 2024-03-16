https://leetcode.com/problems/contiguous-array/

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        N = len(nums)
        
        prefix_map = {}
        prefix_map[0] = -1
        
        res = 0
        running_sum = 0
      
        for right in range(N):
            if nums[right] == 1:
                running_sum += 1
            else:
                running_sum -= 1
            
            if running_sum in prefix_map:
                left = prefix_map[running_sum]
                res = max(res, right - left)
            else:
                prefix_map[running_sum] = right
        
        return res
