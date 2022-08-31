Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Input: ransomNote = "a", magazine = "b"
Output: false
  
Input: ransomNote = "aa", magazine = "ab"
Output: false
  
Input: ransomNote = "aa", magazine = "aab"
Output: true
  
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        # Loop through magazine to find the occurence of each letter, and put it in a dict.
        magazine_occurrence_dict = dict()
        for letter in magazine:
            if letter not in magazine_occurrence_dict:
                magazine_occurrence_dict[letter] = 1
            else:
                magazine_occurrence_dict[letter] += 1
        
        # Loop through ransomNote to see if each letter:
        #     1: is in the dict
        #     2: exhausts the occurrence yet
        for letter in ransomNote:
            if letter not in magazine_occurrence_dict:
                return False
            if letter in magazine_occurrence_dict and magazine_occurrence_dict[letter] <= 0:
                return False
            magazine_occurrence_dict[letter] -= 1
        
        return True
