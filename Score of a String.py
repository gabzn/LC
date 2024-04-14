https://leetcode.com/problems/score-of-a-string/

class Solution:
    def scoreOfString(self, s: str) -> int:
        N = len(s)
        return sum(abs(ord(s[i]) - ord(s[i-1])) for i in range(1, N))
