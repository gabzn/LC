https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0
        
        for num in nums:
            if num < k:
                res += 1
        
        return res
