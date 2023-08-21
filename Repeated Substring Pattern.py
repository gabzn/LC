https://leetcode.com/problems/repeated-substring-pattern/

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        LEN = len(s)
        index, sub_str = 0, ''
        
        while index < LEN:
            sub_str += s[index]
            if sub_str == s:
                return False
            
            temp_sub_str = sub_str
            while len(temp_sub_str) < LEN:
                temp_sub_str += sub_str
                
            if temp_sub_str == s:
                return True
            
            index += 1
