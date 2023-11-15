https://leetcode.com/problems/unique-length-3-palindromic-subsequences/
https://www.youtube.com/watch?v=WF06WjcePAw

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        leftmost, rightmost = {}, {}
        
        for idx, char in enumerate(s):
            if char not in leftmost:
                leftmost[char] = idx
            else:
                rightmost[char] = idx
        
        res = 0
        for char in leftmost:
            if char in rightmost:
                palindromes = set([s[idx] for idx in range(leftmost[char] + 1, rightmost[char])])
                res += len(palindromes)
        
        return res
