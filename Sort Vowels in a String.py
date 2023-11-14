https://leetcode.com/problems/sort-vowels-in-a-string/

class Solution:
    def sortVowels(self, s: str) -> str:
        def is_vowel(char):
            return char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' \
                or char == 'A' or char == 'E' or char =='I' or char == 'O' or char == 'U'
        
        vowels = []
        res = []
        
        for char in s:
            if is_vowel(char):
                vowels.append(char)
        
        vowels.sort(reverse=True)
        for char in s:
            if is_vowel(char):
                res.append(vowels.pop())
            else:
                res.append(char)
        
        return ''.join(res)
