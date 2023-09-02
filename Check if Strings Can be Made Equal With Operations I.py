https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        def swap(s):
            return sorted(s[::2]), sorted(s[1::2])
            
        return swap(s1) == swap(s2)
