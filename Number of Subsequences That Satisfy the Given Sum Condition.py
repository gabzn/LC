https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = (10**9) + 7
        LEN = len(nums)
        
        nums.sort()
        res, r = 0, LEN - 1
        
        for l in range(len(nums)):
            while r >= l and nums[r] + nums[l] > target:
                r -= 1
            if r < l:
                break
            
            res += pow(2, r - l) % MOD
                  
        return res % MOD
-----------------------------------------------------------------------------
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        def find_right_bound(smallest, left, right):
            
            while left + 1 != right:
                mid = (left + right) // 2
                if nums[mid] + smallest > target:
                    right = mid
                else:
                    left = mid
        
            return left
            
        MOD = (10**9) + 7
        LEN = len(nums)
        
        nums.sort()
        res, r = 0, LEN - 1
        
        for l in range(len(nums)):
            r = find_right_bound(nums[l], l-1, LEN)
            if r < l:
                break
                
            res += pow(2, r - l) % MOD
                  
        return res % MOD
