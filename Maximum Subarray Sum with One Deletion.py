https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        LEN = len(arr)
        
        dp = [[_ for _ in range(2)] for _ in range(LEN)]
        dp[0][0] = arr[0]
        dp[0][1] = arr[0]
        res = arr[0]
        
        for i in range(1, LEN):
            num = arr[i]
            dp[i][0] = max(dp[i-1][0] + num, num)
            dp[i][1] = max(dp[i-1][0], dp[i-1][1] + num)
            res = max(res, dp[i][0], dp[i][1])
        
        return res
