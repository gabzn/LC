https://leetcode.com/problems/determine-if-string-halves-are-alike/

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = 'aeiouAEIOU'
        count = 0
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] in vowels:
                count += 1
            if s[r] in vowels:
                count -= 1
            l += 1
            r -= 1
        
        return count == 0
