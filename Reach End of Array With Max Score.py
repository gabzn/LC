https://leetcode.com/problems/reach-end-of-array-with-max-score/

class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        N = len(nums)
        
        dp = [[0, 0] for _ in range(N)]
        dp[0][1] = res = nums[0] * (N - 1)
        
        prev_max = nums[0]
        i = 0
        
        for j in range(1, N - 1):
            num = nums[j]
            dp[j][0] = (j - i) * prev_max + dp[i][0]
            if num > prev_max:
                prev_max = num
                i = j
            
            dp[j][1] = dp[j][0] + (((N - 1) - j) * num)
            res = max(res, dp[j][1])

        return res
