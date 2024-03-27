https://leetcode.com/problems/distinct-subsequences-ii/

class Solution:
    def distinctSubseqII(self, s: str) -> int:
        N = len(s)
        MOD = 10 ** 9 + 7
        """
        [x x x] A x    x      A
                j     i-1     i
                    
        dp[i] = (dp[i-1] * 2) - dp[j-1]
        
        s[j-1] + s[j] == s[j-1] + s[i]
        Need to remove dp[j-1] because we are counting it twice
        """
        s = '/' + s
        dp = [0] * (N + 1)
        dp[0] = 1
        
        prev_char_idx = [0] * 26
        
        for i in range(1, N + 1):
            char = s[i]
            char_idx = ord(char) - ord('a')
            j = prev_char_idx[char_idx]
            
            dp[i] = ((dp[i-1] * 2) - dp[j-1]) % MOD
            prev_char_idx[char_idx] = i
        
        # Subtract the empty subsequence
        return (dp[-1] - 1) % MOD
