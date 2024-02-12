https://leetcode.com/problems/largest-divisible-subset/

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        LEN = len(nums)
        nums.sort()
        
        dp = [[1, -1] for _ in range(LEN)]
        max_len = 1
        ending_idx = 0
        
        for right in range(LEN):
            for left in range(right):
                if nums[right] % nums[left] == 0 and dp[left][0] + 1 > dp[right][0]:
                    dp[right][0] = dp[left][0] + 1
                    dp[right][1] = left
                    
                    if dp[right][0] > max_len:
                        max_len = dp[right][0]
                        ending_idx = right
        
        res = []
        while ending_idx != -1:
            res.append(nums[ending_idx])
            ending_idx = dp[ending_idx][1]
        
        return res
