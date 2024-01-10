https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        LEN = len(nums)
        
        res = 0
      
        for left in range(LEN):
            # The start of new subarray and this new num will be the GCD
            divisor = nums[left]
            
            for right in range(left, LEN):
                # Check every subarray of started with nums[left], and update the GCD
                divisor = gcd(divisor, nums[right])
                
                if divisor == k:
                    res += 1
                if divisor < k:
                    break
                    
        return res
