https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-i/

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        N, M = len(nums), len(pattern)
        
        res = 0
        
        for right in range(M, N):
            left = right - M
            
            is_a_match = True
            k = 0
            
            for k, pat in enumerate(pattern):
                if pat == 1 and nums[left + k + 1] <= nums[left + k]:
                    is_a_match = False
                    break
                    
                if pat == 0 and nums[left + k + 1] != nums[left + k]:
                    is_a_match = False
                    break
                    
                if pat == -1 and nums[left + k + 1] >= nums[left + k]:
                    is_a_match = False
                    break
            
            if is_a_match:
                res += 1
        
        return res
