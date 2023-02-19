https://leetcode.com/problems/subarray-product-less-than-k/
  
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        res, l, product= 0, 0, 1
        for r in range(len(nums)):
            product *= nums[r]
        
            while l <= r and product >= k:
                product //= nums[l]
                l += 1
            
            res += r - l + 1
            
        return res
