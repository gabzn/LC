https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/

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
