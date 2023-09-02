https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        def count(s, mod):
            return Counter([char if index % mod == 0 else None for index, char in enumerate(s)])
            
        return count(s1, 2) == count(s2, 2) and count(s1, 1) == count(s2, 1)
