https://leetcode.com/problems/count-complete-subarrays-in-an-array/

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        LEN = len(nums)
        
        unique_nums = len(set(nums))
        res = 0
        
        # Check every subarray
        for l in range(LEN):
            # If the number of unique number is 1, every num is an ans
            if unique_nums == 1:
                res += (LEN - l)
                continue
            
            # Exit early if the number of remaining is not enough to have unique_nums
            if LEN - l < unique_nums:
                break
                
            # Add the current number to the set
            subarray_unique = {nums[l]}
            
            for r in range(l+1, LEN):
                subarray_unique.add(nums[r])
                
                if len(subarray_unique) == unique_nums:
                    res += (LEN - r)
                    break
    
        return res
