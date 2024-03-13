https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        N = len(nums)
        
        res = 0
        i = 0
        
        while i < N:
            if nums[i] == 0:
                i += 1
                continue
            
            negative_num_count = 0
            first_negative_idx = -1
            j = i
            
            while j < N and nums[j] != 0:
                negative_num_count += (nums[j] < 0)
                
                # Find the index of the first negative number in this window
                if nums[j] < 0 and first_negative_idx == -1:
                    first_negative_idx = j
                
                if negative_num_count % 2 == 0:
                    res = max(res, j - i + 1)
                else:
                    if first_negative_idx != -1:
                        res = max(res, j - first_negative_idx)
        
                j += 1
            i = j
        
        return res
