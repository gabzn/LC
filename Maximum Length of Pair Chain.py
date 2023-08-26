https://leetcode.com/problems/maximum-length-of-pair-chain/

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        LEN = len(pairs)
        dp = [1] * LEN
        pairs.sort(key=lambda pair: pair[0])
        
        for r in range(LEN):
            for l in range(r):
                if pairs[r][0] > pairs[l][1]:
                    dp[r] = max(dp[r], 1 + dp[l])
    
        return max(dp)
