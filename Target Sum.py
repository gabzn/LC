https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(i, total):
            if i == len(nums):
                if total == target:
                    return 1
                return 0
            return dfs(i + 1, -nums[i] + total) + dfs(i + 1, nums[i] + total)
        return dfs(0, 0)
