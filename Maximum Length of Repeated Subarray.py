https://leetcode.com/problems/maximum-length-of-repeated-subarray/
  
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        LEN1, LEN2 = len(nums1), len(nums2)
        dp = [[0 for _ in range(LEN2 + 1)] for _ in range(LEN1 + 1)]
        res = 0
        
        for x in range(1, LEN1 + 1):
            for y in range(1, LEN2 + 1):
                if nums1[x - 1] == nums2[y - 1]:
                    dp[x][y] = 1 + dp[x - 1][y - 1]
                    res = max(res, dp[x][y])
                    
        return res  
