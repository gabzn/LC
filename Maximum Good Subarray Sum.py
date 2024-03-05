https://leetcode.com/problems/maximum-good-subarray-sum/

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)
    
        pref = [nums[0]]
        for i in range(1, N):
            pref.append(pref[-1] + nums[i])
        
        res = -inf
        pref_dict = {}
        
        for i, num in enumerate(nums):            
            for diff in [num - k, num + k]:
                if diff in pref_dict:
                    res = max(res, pref[i] - pref_dict[diff])
            
            if num not in pref_dict:
                if i == 0:
                    pref_dict[num] = 0
                else:
                    pref_dict[num] = pref[i - 1]
            else:
                pref_dict[num] = min(pref_dict[num], pref[i - 1])
                
        return res if res != -inf else 0
