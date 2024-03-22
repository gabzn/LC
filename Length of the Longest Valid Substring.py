https://leetcode.com/problems/length-of-the-longest-valid-substring/
https://www.youtube.com/watch?v=6nNYfhthYB8

class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        N = len(word)
        
        forbidden_set = set(forbidden)
        res = 0
        right = N - 1
        
        for left in range(N - 1, -1, -1):
            for i in range(left, min(left + 10, right + 1)):
                if word[left: i + 1] in forbidden_set:
                    right = i - 1
                    break
                
            res = max(res, right - left + 1)
        
        return res
