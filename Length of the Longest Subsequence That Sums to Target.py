https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/

class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        LEN = len(nums)
        cache = [[None for _ in range(target + 1)] for _ in range(LEN + 1)]
        
        def dp(i, remaining):     
            if remaining == 0:
                return 0
            if i == LEN:
                return -inf            
            if cache[i][remaining]:
                return cache[i][remaining]
            
            # Skip
            res = dp(i + 1, remaining)
            
            # Pick
            if remaining - nums[i] >= 0:
                res = max(res, 1 + dp(i + 1, remaining - nums[i]))
            
            cache[i][remaining] = res
            return res
        
        res = dp(0, target)
        return res if res > 0 else -1
