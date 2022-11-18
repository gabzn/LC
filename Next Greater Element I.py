https://leetcode.com/problems/next-greater-element-i/
  
from collections import defaultdict

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res, stack = [-1] * len(nums1), []        
        num_ind_dict = self.convert_list_to_dict(nums1)
        
        for num in nums2:
            while stack and num > stack[-1]:
                topmost_val = stack.pop()
                topmost_val_ind = num_ind_dict[topmost_val]
                res[topmost_val_ind] = num
                
            if num in num_ind_dict:
                stack.append(num)
        
        return res

    def convert_list_to_dict(self, nums):
        num_ind_dict = defaultdict(int)
        for index, num in enumerate(nums):
            num_ind_dict[num] = index  
        
        return num_ind_dict
    
#         res = []
#         num_ind_dict = defaultdict(int)
        
#         for index, num in enumerate(nums2):
#             num_ind_dict[num] = index
        
#         for num in nums1:
#             ind_in_num2 = num_ind_dict[num]
#             previous_len = len(res)
            
#             for i in range(ind_in_num2+1, len(nums2)):
#                 if nums2[i] > num:
#                     res.append(nums2[i])
#                     break
            
#             if previous_len == len(res):
#                 res.append(-1)
                
#         return res
