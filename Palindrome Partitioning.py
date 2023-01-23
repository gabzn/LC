https://leetcode.com/problems/palindrome-partitioning/description/
  
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        return self.backtrack(s, 0, [], [])

    def backtrack(self, s, start, current, res):        
        if start == len(s):
            res.append(current.copy())
            return res

        for idx in range(start, len(s)):
            if self.is_palindrome(s[start:idx + 1]):
                current.append(s[start:idx + 1])
                res = self.backtrack(s, idx + 1, current, res)
                current.pop()

        return res

    def is_palindrome(self, s):
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1

        return True
