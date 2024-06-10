https://leetcode.com/problems/substrings-that-begin-and-end-with-the-same-letter/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        pref = defaultdict(int)
        res = 0
        
        for char in s:
            pref[char] += 1
            res += pref[char]
        
        return res
