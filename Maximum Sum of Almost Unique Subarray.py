https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/

class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:        
        LEN = len(nums)
        
        # Compute prefix sum
        pref = [0]
        for num in nums:
            pref.append(pref[-1] + num)

        # Check all subarrays of size k to see if each has at least m unique numbers
        ans = 0
        for right in range(k-1, LEN):
            left = right - k + 1
            
            unique_nums = len(set(nums[left: right+1]))
            if unique_nums >= m:
                subarray_sum = pref[right+1] - pref[left]
                ans = max(subarray_sum, ans)
                
        return ans
----------------------------------------------------------------------
class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        pref = [0]
        for num in nums:
            pref.append(pref[-1] + num)
        
        res = 0
        r = k
        while r < len(pref):
            l = r - k + 1
            
            if len(set(nums[l-1: r])) >= m:
                res = max(res, pref[r] - pref[l-1])
            
            r += 1
        
        return res
