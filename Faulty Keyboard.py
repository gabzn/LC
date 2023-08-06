https://leetcode.com/problems/faulty-keyboard/

class Solution:
    def finalString(self, s: str) -> str:
        chars = []
        
        for char in s:
            if char == 'i':      
                chars.reverse()
            else:
                chars.append(char)
                
        return ''.join(chars)
