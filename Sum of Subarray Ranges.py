https://leetcode.com/problems/sum-of-subarray-ranges/

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        """
        sum of subarray range = sum of subarray max - sum of subarray min
        https://leetcode.com/problems/sum-of-subarray-minimums/
        """
        LEN = len(nums)
        
        stack = []
        ############ Start - prev and next smaller ##################
        next_smaller = [(LEN, None) for _ in range(LEN)]
        for idx in range(LEN):
            num = nums[idx]
            
            while stack and nums[stack[-1]] > num:
                i = stack.pop()
                next_smaller[i] = (idx, num)
            
            stack.append(idx)
        
        stack.clear()
        
        prev_smaller = [(-1, None) for _ in range(LEN)]
        for idx in range(LEN - 1, -1, -1):
            num = nums[idx]
            
            while stack and nums[stack[-1]] >= num:
                i = stack.pop()
                prev_smaller[i] = (idx, num)
            
            stack.append(idx)
        
        stack.clear()
        ############ End - prev and next smaller ##################

        ############ Start - prev and next bigger ##################        
        next_bigger = [(LEN, None) for _ in range(LEN)]
        for idx in range(LEN):
            num = nums[idx]
            
            while stack and nums[stack[-1]] < num:
                i = stack.pop()
                next_bigger[i] = (idx, num)
            
            stack.append(idx)
        
        stack.clear()
        
        prev_bigger = [(-1, None) for _ in range(LEN)]
        for idx in range(LEN - 1, -1, -1):
            num = nums[idx]
            
            while stack and nums[stack[-1]] <= num:
                i = stack.pop()
                prev_bigger[i] = (idx, num)
                
            stack.append(idx)
        ############ End - prev and next bigger ##################        
        
        res = 0
        
        for idx in range(LEN):
            small_left = prev_smaller[idx][0]
            small_right = next_smaller[idx][0]
            sub_min = (nums[idx] * ((idx - small_left) * (small_right - idx)))
            
            big_left = prev_bigger[idx][0]
            big_right = next_bigger[idx][0]
            sub_max = (nums[idx] * ((idx - big_left) * (big_right - idx)))
            
            res += (sub_max - sub_min)
        
        return res
---------------------------------------------------------------------
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        LEN = len(nums)
        
        res = 0
        
        for i in range(LEN):
            largest = smallest = nums[i]
            
            for j in range(i, LEN):
                largest = max(largest, nums[j])
                smallest = min(smallest, nums[j])
                
                res += largest - smallest
        
        return res
