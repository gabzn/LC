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
