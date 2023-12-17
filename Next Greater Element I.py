https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_to_next_greater = {}
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                prev_num = stack.pop()
                num_to_next_greater[prev_num] = num
            
            stack.append(num)
        
        while stack:
            num_to_next_greater[stack.pop()] = -1
        
        res = []
        for num in nums1:
            res.append(num_to_next_greater[num])
        
        return res
-------------------------------------------------------------------------------------------------
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
