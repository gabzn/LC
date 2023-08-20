https://leetcode.com/problems/sorting-three-groups/
https://www.youtube.com/watch?v=ALMwLrMHURo&lc=UgyObdYYUwJu0TpjjXV4AaABAg.9tbsQgV3xZg9tbtg_GA2pG

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        LEN = len(nums)
        dp = [[0 for _ in range(4)] for _ in range(LEN + 1)]
        
        for index in range(1, LEN + 1):
            num = nums[index - 1]
            
            dp[index][1] = dp[index - 1][1] + (1 if num != 1 else 0)
            dp[index][2] = min(dp[index - 1][2], dp[index - 1][1]) + (1 if num != 2 else 0)
            dp[index][3] = min(dp[index - 1][3], dp[index - 1][2], dp[index - 1][1]) + (1 if num != 3 else 0)
    
        return min(dp[-1][1:])
