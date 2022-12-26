https://leetcode.com/problems/minimum-size-subarray-sum/
  
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        LEN = len(nums)
        min_size = math.inf
        l, r, running_sum = 0, 0, 0
        
        # Pretty standard sliding window problem.
        # Two pointers from the beginning. 
        # If the window sum is >= target, update the size 
        # chop off the leftmost val from the sum
        # move right to its right
        while r < LEN:
            running_sum += nums[r]
            
            while running_sum >= target:
                min_size = min(min_size, r - l + 1)
                running_sum -= nums[l]
                l += 1
        
            r += 1
             
        return 0 if min_size == math.inf else min_size 
