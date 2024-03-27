https://leetcode.com/problems/subarray-product-less-than-k/

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        N = len(nums)
        
        res = 0
        product = 1
        left = 0
        
        for right in range(N):
            product *= nums[right]
            
            while left < right and product >= k:
                product //= nums[left]
                left += 1
            
            if product < k:
                res += (right - left + 1)
        
        return res
---------------------------------------------------------------------------
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
