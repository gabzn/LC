https://leetcode.com/problems/longest-arithmetic-subsequence/

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        LEN = len(nums)
        dp = {}
        
        for right in range(LEN):
            for left in range(right):
                difference = nums[right] - nums[left]
                
                if (left, difference) in dp:
                    dp[(right, difference)] = 1 + dp[(left, difference)]
                else:
                    dp[(right, difference)] = 2
        
        return max(dp.values())
