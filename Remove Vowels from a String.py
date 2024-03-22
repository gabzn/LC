https://leetcode.com/problems/remove-vowels-from-a-string/

class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = 'aeiou'
        
        new_str = []
        for char in s:
            if char not in vowels:
                new_str.append(char)
        
        return ''.join(new_str)
