https://leetcode.com/problems/minimum-increment-operations-to-make-array-beautiful/

class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        LEN = len(nums)
        
        dp = []
        for num in nums:
            dp.append(max(0, k - num))
          
        """
        dp[i] = the minimum number of operations needed to make
        all subarrays before i beautiful + the # of operations to make nums[i] >= k.
        """
        for i in range(3, LEN):
            dp[i] = dp[i] + min(dp[i - 3], dp[i - 2], dp[i - 1])
        
        return min(dp[LEN - 3], dp[LEN - 2], dp[LEN - 1])
