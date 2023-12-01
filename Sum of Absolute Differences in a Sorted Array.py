https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        """
        left: ([i]-[0]) + ([i]-[1]) ... + ([i]-[i-1])
        right: ([i+1]-[i]) + ([i+2]-[i]) ... + ([LEN-1]-[i])        

        left: ([i] * i) - pref[i - 1]
        right: (pref[-1] - pref[i]) - ([i] * (LEN - 1 - i))
        
        res = left + right
        """    
        LEN = len(nums)
        
        pref = [nums[0]]
        for idx in range(1, LEN):
            pref.append(pref[-1] + nums[idx])
        
        result = []
        for idx, num in enumerate(nums):
            left = 0
            if idx > 0:
                left = (num * idx) - pref[idx - 1]
            
            right = 0
            if idx < LEN - 1:
                right = (pref[-1] - pref[idx]) - (num * (LEN - idx - 1))
            
            result.append(left + right)
            
        return result
