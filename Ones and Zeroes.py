https://leetcode.com/problems/ones-and-zeroes/

class Solution:
    def findMaxForm(self, strs: List[str], max_zeroes: int, max_ones: int) -> int:            
        dp = [[0 for _ in range(max_zeroes + 1)] for _ in range(max_ones + 1)]
        
        for string in strs:
            ones, zeroes = string.count('1'), string.count('0')
            
            for row in range(max_ones, ones-1, -1):
                for col in range(max_zeroes, zeroes-1, -1):                   
                    dp[row][col] = max(dp[row][col], 1+dp[row-ones][col-zeroes])
        
        return dp[-1][-1]
