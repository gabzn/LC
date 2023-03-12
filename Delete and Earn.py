https://leetcode.com/problems/delete-and-earn/
  
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points, max_num = collections.defaultdict(int), 0
        
        for num in nums:
            points[num] += num
            max_num = max(max_num, num)
        
        return self.dp(points, max_num, {})
    
    # dp(i) gives us the max points we can get if we pick i
    def dp(self, points, i, memo):
        if i == 0 or i == 1:
            return points[i]
        
        if i not in memo:
            memo[i] = max(points[i] + self.dp(points, i - 2, memo), self.dp(points, i - 1, memo))
        
        return memo[i]
-----------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_num, points = 0, collections.defaultdict(int)
        
        for num in nums:
            points[num] += num
            max_num = max(max_num, num)
        
        # dp[i] tells us the max pts we can get picking the i num
        dp = [0] * (max_num + 1)
        dp[1] = points[1]      # A bit tricky, but if there's no 1 the default is 0
        
        for i in range(2, max_num + 1):
            dp[i] = max(dp[i - 2] + points[i], dp[i - 1])
        
        return dp[-1]
