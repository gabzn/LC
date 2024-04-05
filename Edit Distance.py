https://leetcode.com/problems/edit-distance/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N = len(word1)
        M = len(word2)
        
        word1 = '/' + word1
        word2 = '/' + word2
    
        # dp[i][j] = the minimum # of operations to convert word1[:i] to word2[:j].
        dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
        
        for i in range(1, N + 1):
            dp[i][0] = i
            
        for j in range(1, M + 1):
            dp[0][j] = j
        
        for i in range(1, N + 1):   
            for j in range(1, M + 1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    delete_i = dp[i-1][j] + 1
                    replace_i = dp[i-1][j-1] + 1
                    insert_i = dp[i][j-1] + 1
                    dp[i][j] = min(delete_i, replace_i, insert_i)
        
        return dp[N][M]
