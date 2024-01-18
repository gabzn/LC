https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/

class Solution:
    def makeStringsEqual(self, s: str, t: str) -> bool:        
        s_counter = Counter(s)
        t_counter = Counter(t)
        
        if s_counter == t_counter:
            return True
        
        if (len(t_counter) == 1 and '0' in t_counter) or (len(s_counter) == 1 and '0' in s_counter):
            return False
        
        return True
