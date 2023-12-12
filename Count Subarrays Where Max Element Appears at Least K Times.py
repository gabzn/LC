https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/
https://www.youtube.com/watch?v=hKCLdPg1WPo

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        MAX_NUM = max(nums)
        
        res = 0
        left = max_num_count = 0
        for right, num in enumerate(nums):
            if num == MAX_NUM:
                max_num_count += 1
            
            while max_num_count >= k:
                if nums[left] == MAX_NUM:
                    max_num_count -= 1
                left += 1
                
            res += left
        return res
------------------------------------------------------------------------------
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        LEN = len(nums)
        MAX_NUM = max(nums)
        
        # Get the indices of all the max num
        indices_of_max_num = []
        for idx, num in enumerate(nums):
            if num == MAX_NUM:
                indices_of_max_num.append(idx)
        
        if len(indices_of_max_num) < k:
            return 0
        
        res = max_count = 0
        for right in range(LEN):
            if nums[right] == MAX_NUM:
                max_count += 1
            
            if max_count >= k:
                left = (max_count - k)
                res += indices_of_max_num[left] + 1
                
        return res
