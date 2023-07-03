https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
                
        differences = 0
        for index in range(len(s1)):
            if s1[index] != s2[index]:
                differences += 1
                if differences > 2:
                    return False
        
        return Counter(s1) == Counter(s2)
