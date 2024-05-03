https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:        
        N = len(nums)
        
        nums.sort()
        res = 0
        left = 0
        for right in range(N):            
            while nums[right] - nums[left] > 2 * k:
                left += 1

            res = max(res, right - left + 1)
    
        return res
