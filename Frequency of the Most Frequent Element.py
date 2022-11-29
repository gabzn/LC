https://leetcode.com/problems/frequency-of-the-most-frequent-element/
  
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:        
        nums.sort()
        
        max_freq = 1
        window_sum = 0
        l, r = 0, 0   
        
        while r < len(nums):    
            window_sum += nums[r]
            
            # nums[r] * (r-l+1) gives us the total sum if we were to change every number to [r]
            while nums[r] * (r-l+1) > window_sum + k :
                window_sum -= nums[l]
                l += 1
            
            max_freq = max(r-l+1, max_freq)    
            r += 1
             
        return max_freq
