https://leetcode.com/problems/valid-word/

class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        
        v = c = False
        for char in word:
            if char in '@#$':
                return False
            if char.isalpha():
                if char.lower() in 'aeiou':
                    v = True
                else:
                    c = True
                
        return v and c
