https://leetcode.com/problems/count-the-number-of-special-characters-i/

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        chars = set()
        
        for char in word:
            if char.upper() in word and char.lower() in word:
                chars.add(char)
        
        return len(chars) // 2
