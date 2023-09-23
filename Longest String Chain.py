https://leetcode.com/problems/longest-string-chain/

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        LEN = len(words)

        words.sort(key=lambda w: len(w))
        dp = [1 for _ in range(LEN)]
        res = 1
        
        for right in range(LEN):
            right_word = words[right]
            
            for left in range(right):
                left_word = words[left]
                
                if len(right_word) == len(left_word) or \
                   len(right_word) - len(left_word) != 1:
                    continue
                
                for i in range(len(right_word)):
                    if left_word == (right_word[:i] + right_word[i+1:]):    
                        dp[right] = max(dp[left] + 1, dp[right])
                        res = max(dp[right], res)

        return res
