https://leetcode.com/problems/palindrome-partitioning/description/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtrack(i, current):
            if i == N:
                res.append(current[::])
                return
            
            for idx in range(i, N):
                sub_s = s[i: idx + 1]
                if sub_s == sub_s[::-1]:
                    current.append(sub_s)
                    backtrack(idx + 1, current)
                    current.pop()
            
        N = len(s)
        res = []
        backtrack(0, [])
        return res
--------------------------------------------------------------------------------
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
