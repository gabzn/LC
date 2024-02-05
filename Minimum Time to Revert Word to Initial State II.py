https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-ii/
https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-i/

class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        LEN = len(word)
        res = 0
        
        for i in range(k, LEN, k):
            res += 1
            
            if word[i:] == word[:LEN - i]:
                return res
        
        return res + 1        
