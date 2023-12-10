https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/

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

#    NO GOOD SOLUTION
#         indices_of_max_num = []
#         for idx, num in enumerate(nums):
#             if num == MAX_NUM:
#                 indices_of_max_num.append(idx)
        
#         if len(indices_of_max_num) < k:
#             return 0
        
#         res = 0
#         for right in range(k-1, len(indices_of_max_num)):
#             left = (right - k + 1)    
#             res += (indices_of_max_num[left] + 1)
                
#         return res
