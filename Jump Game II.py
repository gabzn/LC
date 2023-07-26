https://leetcode.com/problems/jump-game-ii/

class Solution:
    def jump(self, nums: List[int]) -> int:
        LEN = len(nums)
        res = 0
        furthest_reach_from_index, cur_end = 0, 0
        
        for index in range(LEN - 1):
            furthest_reach_from_index = max(furthest_reach_from_index, index + nums[index])
            
            if index == cur_end:
                cur_end = furthest_reach_from_index
                res += 1
        
        return res
-----------------------------------------------------------------
class Solution:
    def jump(self, nums: List[int]) -> int:
        LEN = len(nums)
        dp = [math.inf for _ in range(LEN)]
        dp[0] = 0
        
        for index in range(LEN):
            for furthest_index in range(1, nums[index] + 1):
                if index + furthest_index < LEN:
                    dp[index + furthest_index] = min(1 + dp[index], dp[index + furthest_index])
        
        return dp[-1]
---------------------------------------------------------------------------------------
class Solution:
    def jump(self, nums: List[int]) -> int:
        LEN = len(nums)
        
        def dp(index, memo):
            if index == LEN - 1:
                return 0
            if index in memo:
                return memo[index]
            
            memo[index] = LEN - 1
            for i in range(1, nums[index] + 1):
                if index + i <= LEN - 1:
                    memo[index] = min(memo[index], 1 + dp(index + i, memo))
            
            return memo[index]
        
        return dp(0, {})
