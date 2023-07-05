https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res, l = 0, 0
        num_of_zeroes = 0
        
        for r in range(len(nums)):
            # If the current number is 0, increase the count
            if nums[r] == 0:
                num_of_zeroes += 1
                    
            # While the current window has 2 zeroes, 
            # we want to move the left pointer until the leftmost zero is gone.
            while num_of_zeroes == 2:
                if nums[l] == 0:
                    num_of_zeroes -= 1
                l += 1
                    
            res = max(res, r - l)
        
        return res
