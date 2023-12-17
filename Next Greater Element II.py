https://leetcode.com/problems/next-greater-element-ii/

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        original_len = len(nums)
        last_element_idx = original_len - 1
        
        # Duplicate nums
        idx = 0
        while idx < last_element_idx:
            nums.append(nums[idx])
            idx += 1
                
        res = [-1] * original_len
        stack = []
        
        for idx, num in enumerate(nums):
            while stack and num > stack[-1][1]:
                prev_idx, _ = stack.pop()
                
                if prev_idx < original_len:
                    res[prev_idx] = num
            
            stack.append((idx, num))
              
        return res
