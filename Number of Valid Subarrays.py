https://leetcode.com/problems/number-of-valid-subarrays/

class Solution:
    def validSubarrays(self, nums: List[int]) -> int:                        
        """
        1 4 2 5 3
        
        Find the next smaller 
        1
        1 4
        1 4 2
        1 4 2 5
        1 4 2 5 3
        
        4
        
        2
        2 5
        2 5 3
        
        5
        
        3
        """
        N = len(nums)
        
        next_smaller = [N] * N
        stack = []
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] > num:
                j = stack.pop()
                next_smaller[j] = i
            stack.append(i)
 
        return sum([next_smaller_index - i for i, next_smaller_index in enumerate(next_smaller)])
