https://leetcode.com/problems/count-the-number-of-special-characters-ii/

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        uppercases = {}
        lowercases = {}
        
        for i, char in enumerate(word):
            if char.islower():
                lowercases[char] = i
            
            if char.isupper() and char not in uppercases:
                uppercases[char] = i
        
        res = 0
        for char, i in lowercases.items():
            char_upper = char.upper()
            if char_upper in uppercases and i < uppercases[char_upper]:
                res += 1
        
        return res
