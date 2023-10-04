https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        def compute_prefix_max(lst):
            pref = [0]
            for i in range(1, len(lst)):
                pref.append(max(pref[-1], lst[i-1]))
            return pref
        
        prefix_max = compute_prefix_max(nums)
        suffix_max = compute_prefix_max(nums[::-1])[::-1]
        
        res = 0
        
        # Fix i and k, treat each num in nums as new j
        for j in range(1, len(nums) - 1):
            res = max(res, (prefix_max[j] - nums[j]) * suffix_max[j])
        
        return res
--------------------------------------------------------------------------------------------------
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res, max_i, max_i_minus_j = 0, 0, 0
        
        """
        Step 1: At each iteration, we treat the current number as new k to compute the result
        
        Step 2: Then, we treat it as j to maximize (i - j)
                To maximum (i - j), we need to minimize j
        
        Step 3: Lastly, if we were able to maximize (i - j) by having a smaller j,
                i will not be updated
        """
        for k in nums:
            res = max(res, max_i_minus_j * k) 
            max_i_minus_j = max(max_i_minus_j, max_i - k)
            max_i = max(max_i, k)
            
        return res
