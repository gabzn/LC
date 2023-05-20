https://leetcode.com/problems/maximum-sum-circular-subarray/
https://www.youtube.com/watch?v=os4B7MlHAbs&t=860s  
  
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_max_sum, max_sum = 0, -math.inf
        cur_min_sum, min_sum = 0, math.inf
        total_sum = 0
        
        for num in nums:
            total_sum += num
            
            cur_max_sum = max(cur_max_sum + num, num)
            max_sum = max(max_sum, cur_max_sum)
            
            cur_min_sum = min(cur_min_sum + num, num)
            min_sum = min(min_sum, cur_min_sum)
        
        return max_sum if max_sum <= 0 else max(max_sum, total_sum - min_sum)
