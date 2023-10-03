https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res, max_i, max_i_minus_j = 0, 0, 0
        
        """
        Step 1: At each iteration, we treat the current number as new k to compute the result
        
        Step 2: Then, we treat it as j to maximize (i - j)
                To maximum (i - j), we need to minimize j
        
        Step 3: Lastly, if we were able to maximize (i - j) by having a smaller j,
                i will not be updated
        """
        for k in nums:
            res = max(res, max_i_minus_j * k) 
            max_i_minus_j = max(max_i_minus_j, max_i - k)
            max_i = max(max_i, k)
            
        return res
