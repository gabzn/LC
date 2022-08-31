Given a string s consisting of lowercase English letters, return the first letter to appear twice.

https://leetcode.com/problems/first-letter-to-appear-twice/
  
Input: s = "abccbaacz"
Output: "c"
  
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        letter_set = set()
        
        for letter in s:
            if letter in letter_set:
                return letter
            letter_set.add(letter)
            
        return None
