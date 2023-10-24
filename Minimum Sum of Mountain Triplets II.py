https://leetcode.com/problems/minimum-sum-of-mountain-triplets-ii/
https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        LEN = len(nums)
        
        def compute_prefix_min(lst: List[int]) -> List[int]:
            pref = [10**8]
            
            for idx in range(1, LEN):
                pref.append(min(pref[-1], lst[idx - 1]))
                    
            return pref
        
        res = inf
        
        pref_min = compute_prefix_min(nums)
        suff_min = compute_prefix_min(nums[::-1])[::-1]
        
        for j in range(1, LEN - 1):
            i = pref_min[j]
            k = suff_min[j]
            
            if nums[j] > i and nums[j] > k:
                res = min(res, i + nums[j] + k)
                
        return res if res != inf else -1
